title: Lila Compiler Development
status: hidden
save_as: pages/lila-log.html

The development logs for my Lila compiler and language.

### 12/20/2020

I've been exploring and doing a few other things over the past few days, so nothing new until today.

The biggest thing is that I'm temporarily making the repository private again. I started making some breaking changes to the syntax, so I don't want anyone using it just yet until I solidify a few things. I will probably post about it because I still intend it to be an open source thing, but until I decide how I want the syntax to go, it will be private. The unit tests all pass, but the standard library is basically broken. If you're interested, email me.

I've been writing a lot about the RISC-V work lately, so here's an update on that. For the most part, the core integer ISA is all implemented, but the floating-point stuff still needs some work. I never thought this would be a huge deal, but RISC-V has no instruction to move data between float registers, so I'm working on a separate layer to optimize that out (specific to RISC-V). Since most of RISC-V is working, I'll probably be pausing until I do some of the syntax work, but none of that should affect the architectures.

### 12/16/2020

Yet another big day. I ended up more or less taking the day other than a meeting; its been an exhausting semester. It may sound weird to some, but these projects are actually a really good way for me to deal with burn out.

I got a huge amount of RISC-V work done. All the integer, short, and byte tests now pass. The arrays took the longest to get working; the alignment and stack layout for RISC-V is a little weird. x86 and Arm both start at the top- but not literally, the first variables location in relation to the base pointer is the stack size minus the base pointer (in other words, if your stack is of size 24 and your variable is 4 long, it would start at 20 or 4- 20 if on Arm, 4 if on x86). On RISC-V, this holds true except for 8 byte variables. If the stack starts at 24, the first variable starts at 24. I'm planning on writing some posts on RISC-V, maybe tomorrow.

In the process of doing this work, I spent the majority of the time in the RISC-V emulator. Its a little annoyingly slow, but its not prohibitive. Fortunately, once you get the hang of Rust, you can do a pretty fair amount of work in between compiling and count on everything working. Especially on the LTAC layer where its pretty much just a 1:1 translation between the IR and the final assembly. The pain point is when I have to run the tests. They take about 10 minutes to fully run (at this point, I'm up to like 120 of the 188 or so).

Most of the new code is in the development branch now.

### 12/15/2020

Today was kind of a big day. I got a fair amount of RISC-V work done. Okay, maybe not huge... Very few of the integer tests pass. But still, code generation for all the signed int-32 math and logical operations are now supported. I am excited though; RISC-V is a new architecture for me.

RISC-V is very interesting. In a lot of ways, its similar to Arm, but in some ways its completed different. Arm is like x86 in that it uses the same instructions for all sizes; you just change the registers based on your needs. RISC-V takes the opposite approach; separate instructions for each size, but always the same registers. This actually makes things a little easier in some ways. RISC-V is interesting though when it comes to immediates. I'll write a post on this later.

### 12/14/2020

I did manage to squeeze in a few hours later in the day and this evening (I'm still working a little as I write this). I decided to get started on the different CPU architecture ports. I definitely want to target Arm64 and RISC-V and maybe MIPS. I did get some of the initial code working for the Arm64 port; basically, the backend is all set up, and it generate assembly for and compile hello world and a few very simple programs.

I also laid the base for the RISC-V backend and got the Hello World program working. RISC architectures are fairly similar, so I think once I have one in place, adding others will be fairly straightforward. I debated on how to approach doing these backends, and I'm thinking for all the RISC ones at least, I'm going to get all the basic backends in place, then break down the work in sections. So basically, let's say I do a set of operations on Arm; I will get that working, then move on and do the same thing on the other architectures. That way, they will all be more or less at the same pace.

For the curious, I'm using Qemu emulators to do development. My Arm64 emulator actually works quite well; its running Ubuntu 20, which helps with the linking paths. I just started with RISC-V and it seems pretty slow. Hopefully its usable, but at first glance, it took a long to build. Its running Fedora 33.

### 12/13/2020

Not much today. I started on a very rough draft for a standard library.

Basically, here's the idea. Originally, I was going to make a standard library a more or less optional thing- my idea wasn't to confine the language to a standard other than the language itself. I'm thinking I may change my stance on that. Programming will become a _nightmare_ if the user has to deal with different APIs on every platform, or even the same platform if they want to use the C library vs the Lila library. My solution to that is create a set of standards that any Lila program can use. To the program itself, it won't matter what library, API, or platform they are on; the user can compile and link however they want. In the case of the C library, the function calls will be to equivalent C functions. Maybe eventually I can implement inlining to eliminate function call overheads. Or maybe explicit inlining- that's an idea. Otherwise, the calls may be pure Lila functions, or even something else.

This week is the last week of school, so I'm not sure how much time I'll have to develop this. But I'll post if I do either decide on something or do it.

### 12/12/2020

Originally, this project was named "Dash". A friend came up with the name, and I really really like it, but I decided to change it for a few reasons. First, I think I tried releasing it too early. Its pretty complete, and can do a few non-trival things, but I should not have posted on it as early as I did. That said, I am glad that I made it open source when I did. The second reason is that I'm thinking about some non-trivial syntax changes (mainly inspired by Pascal and Ada), so if I change it enough, it really needs to be something different. The final reason kind of builds onto the second. The name Dash is somewhat similar to Quik, which is partly why I went with it. However, I feel like it gives an impression of something the language is not, and if I change it enough, I won't be similar to Quik.

I also decided to drop my work with porting it to my custom assembler. That is still a long-term goal, but my current assembler is kind of a mess and not really that stable. I have the base of new one written in Ada in storage so to speak, so when I resume work on that, and if it works out, I will probably port it to that. I also dropped the work because I really wanted to get started with other architectures.

That said, the work and everything wasn't all wasted. I created two branches for the original Dash stable branch and the last state of the development branch before the rename. I created new development and stable branches and renamed everything. I also updated all the documentation.
