title: Shift Register Program
status: hidden

This is the code for the post on [binary counting with shift registers](/memory-and-counting-in-hardware.html).

A few points of interest:

- If you have a different Arduino or whatever, make sure to change the pin numbers. See the post on how to set them correctly.   
- The `data_block` arrays after the pin sets are two examples you can play with to understand how shift registers work. These are run through the shift registers before counting begins.   
- So where did that 65536 come from? This is a 16-bit binary counter, which means we can count up to 2^16 = 65536. By the way, this is an unsigned counter.   


So how did we get the number given that its a short? We had to separate it into bytes. If you look in the for loop where we count up to 65536, you will notice we broke it down into two byte values. The first byte (`byte half1`) is equal to the current number shifted right 8 times. This gets the first 8 bits of the short, which is written to the second shift register. The second byte is simply set equal to the short itself. Because its a smaller value, the first 8 bits are dropped by the compiler, leaving us only with the low 8 bits. These are written to the first shift register.

Finally, even though the delays are small, it will take a long long time to count all the way up to 65536. Be prepared to wait if you want to see the entire loop iteration. I took the picture in the original post before I began writing anything, and it was at 663. Now, its been over half an hour, I've written the post and this page, and its at around 34000. And its used about a quarter of that cell phone battery's charge.

I wonder how long it would take to do an integer.... :)

Here's the code:

```
int latchPin = 3;
int clockPin = 4;
int dataPin = 2;

const int LENGTH = 4;

byte data_block1[LENGTH];
byte data_block2[LENGTH];

void setup() {
  Serial.begin(9600);
  
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);

  digitalWrite(latchPin, LOW);
  digitalWrite(clockPin, LOW);
  digitalWrite(dataPin, LOW);

  // Holds data
  data_block1[0] = 0xFF;
  data_block1[1] = 0x0F;
  data_block1[2] = 0xF0;
  data_block1[3] = 0x00;

  data_block2[0] = 0xFF;
  data_block2[1] = 0xF0;
  data_block2[2] = 0x0F;
  data_block2[3] = 0x00;
}

void writeOut(byte shiftData) {
  int pinState = 0;
  
  for (int i = 7; i>=0; i--) {
    digitalWrite(clockPin, LOW);

    if (shiftData & (1 << i)) {
      pinState = 1;
    } else {
      pinState = 0;
    }

    digitalWrite(dataPin, pinState);

    digitalWrite(clockPin, HIGH);
    digitalWrite(dataPin, LOW);
  }
}

void loop() {
  for (int i = 0; i<LENGTH; i++) {
    digitalWrite(latchPin, LOW);
    writeOut(data_block1[i]);
    writeOut(data_block2[i]);
    digitalWrite(latchPin, HIGH);

    delay(500);
  }

  delay(1000);

  for (short i = 0; i<65536; i++) {
    byte half1 = i >> 8;
    byte half2 = i;

    digitalWrite(latchPin, LOW);
    writeOut(half1);
    writeOut(half2);
    digitalWrite(latchPin, HIGH);

    delay(100);
  }
}
```