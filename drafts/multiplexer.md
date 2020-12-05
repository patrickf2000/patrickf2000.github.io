Title: Understanding the Multiplexer
Date: 2020-08-19 09:38
Category: None

A few weeks ago I wrote about my VHDL arithmetic logic unit (ALU) I was designing. At the time, everything except the shift instructions were implemented. I am happy to say those are now done (and shifters make a whole lot more sense now). However, I am not going to talk about that today. In order to understand how a shifter or the ALU as a whole works, we must understand how a multiplexer works. I touched on multiplexers briefly in the ALU post, but today I am going to describe them in more detail. And the reason is because they can be a little confusing at first, and I found that a lot of explanations on the internet were more confusing then helpful.

A multiplexer basically takes a certain number of inputs, and given a selector input, returns one specific output. Its basically a switch. I often hear the analogy of a railroad yard. There are multiple lines in a junction that all converge on the main line. However, a switch can only connect one line to the main line at a time. That's basically what a mutliplexer does.

Take a look at this image:

[IMG mux_state0]

This is a very simple circuit. There are two inputs up top, each connected to an AND gate and an OR gate. The outputs of the AND and OR gates are connected to the multiplexer. The switch at the bottom is the selector; it decides which input is allowed through. The little round circle to the far right is the output.

At the moment, the output is low. Now watch what happens when we toggle the selector:

[IMG mux_state1]

The output is now high. So what happened?

Look at the two inputs. One is low and one is high. Now consider the truth tables of an AND gate and an OR gate. An AND gate is true only when both inputs are high. Only one input is high, so it evaluates to false. Now consider the OR gate. OR gate is true as long as one or both of the inputs are high. If both inputs are low, the gate returns false. Again, one of the inputs are high, so OR evalutes to true.

Each of the gates are connected to the multiplexer. The reason the multiplexer's result was initially false was because the AND gate was being allowed through. The AND gate currently evaluates to false. However, when we toggle the selector, the output becomes true because the OR gate is true. If we had switched the AND and OR gates around, the opposite would have happened. The result would have been true until the selector was toggled, in which case it would have become false. Basically, a multiplexer allows you to decide which result you want to allow through.

This is how the ALU works on a high level. All the functions are connected to a mutliplexer.
