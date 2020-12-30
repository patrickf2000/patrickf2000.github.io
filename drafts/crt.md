Title: Crt0
Date: 2020-12-27 12:15
Category: Electronics

Under most circumstances, your program starts with main. Okay, probably like 99%. The other 1% is for the compiler people who function in a different realm...

In most languages, your program begins with the main function. In C and most C-like languages, it will look something like this:

```
int main(int argc, char *argv[]) {
    return 0;
}
```

When your program starts, it will begin at this function. `argc` and `argv` are for the command-line arguments. `argv` is an array of strings of the size in the `argc` variable. Once your program does all its fun stuff, it will come back and return 0. Or whatever number.

Fun fact: The program doesn't actually start at main. When you are building an executable, the linker searches for a function called `_start`. The start function does a little work and calls main. Once main returns to the start function, start will return whatever value you returned (in this case, 0) to the operating system. 0 is generally used to indicate a successful exit, and any number can mean anything else.

If you're using Bash (and probably most shells for that matter), you can see the program's return by typing `echo $?`. Compile that code snippet, run it, and run `echo $?`. What do you see? 0. Now change `return 0` to something like `return 5`. Or whatever, it doesn't actually matter. Now compile and run it again, and check the return value. It should be 5.

### What is Crt0?

So why do we not write `_start` in our programs? There are a couple of reasons.

First, it is very architecture specific. The stack and the command line arguments have to be set up in a way specific to whatever instructions and memory model your CPU uses. Secondly, the C library or whatever your language's standard library is may require some initial set up. Once your program runs, there may be some final tasks that have to be done before the program exists. `_start` takes care of all this, and allows the user to write a program that can be run everywhere and with most libraries without having to worry about all this.

`_start` is stored in a small object file called "crt0.o". On many systems, it may actually have a different name called "crt1.o" but that doesn't really matter for our purposes (on Fedora at least, its crt1). When your compiler builds an executable, it links all your objects with the crt1 objects on your system. Although I say on your system, in reality as long as the CPU architecture is the same, it will run anywhere.

### Why Do I Care?

You're probably curious as to why I'm concerned about this. If you're a compiler developer, using the C library is actually really easy. Just generate the assembly, build an object file, and link it with the C library and the crt files, and you will never know a difference from an ordinary C program. All my compilers up till now have basically worked in this way.


