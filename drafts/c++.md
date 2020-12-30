Title: On Object Oriented Programming
Date: 2020-08-19 09:38
Category: None

I have a feeling I'm going to step on some toes with this post... Before I get into it, I want to make it very clear that these are just personal opinions, and if I achieve nothing else with this post, I hope to provoke some thought. I'm not trying to create outrage.

### Background

I grew up with C++. Almost literally; I started using it in 2014, and until fairly recently (probably the last year or so), it was my everyday language. At first, I thought it was the language- just look at my Github profile. Lots and lots of C++. I also started using Java fairly early on as well. I drifted away from that, and have only used it in college assignments and one Android app since then.

What changed me on C++ was some recent programming projects. When I got into compiler development, I used C++ for my initial compilers (the two Quik compilers, and my extcc compiler). At the time, it seemed like a good idea. Using the OOP features of C++, I created a pretty intricate AST and low-level IR. The extcc compiler for a time was my single largest project in terms of lines of code. At its peak, it was something like 5-6000 lines.

My first turn-off came earlier this year when I was trying to redesign the low-level IR. So some quick background. You can write a pretty capable compiler with just four components: the lex/parser, the abstract syntax tree (AST), the low-level IR, and the code generator. In practice, you would probably have a transformation component, and maybe multiple parsing components. The AST is used to represent the code structure, and the low-level IR is used to represent generated code- CPU instructions. The benefits of this IR is that it allows instruction-level optimizations and super easy portion to other architectures. And it makes the overall code generation much more easier.

The low-level IR in extcc was originally from my last Quik compiler. I made several mistakes in designing that IR; basically, rather than being a linear list of instruction representations, it was basically a fairly deep try that was hard to use and manipulate (hey, I was learning). The problem was that because of the OOP nature, I couldn't just go and change one thing (really, it was just a few changes that needed to be made to flatten things out). Changing one node or updating a field in a higher node screwed the whole thing up. Eventually, I just ripped out the entire IR and began rewriting a new one. The problem was that I ran into issues with the AST and the parser, and at that point I just shelved the project. I would have been rewriting the whole thing at that point.

I did try to resurrect my last Quik compiler, but I ran into the same issue. You change one class (unless its one near the bottom of the inheritence tree), and that creates a mess no sane human can interpret. I was personally proud of both of those compilers, but the few bad design choices I made just locked me out. It would have meant a complete rewrite of everything.

A few months ago, I started a new compiler project, and its been fun ever since. I wrote this compiler in Rust, which has no OOP- or at least what you would call OOP is significantly different. Like my previous compilers, there is an AST and a low-level IR. But both are significantly more in depth than either of my previous ones, and they require a fraction of the amount of code. The low-level IR is something I'm especially proud of. I've been able to go throught and make some core changes to the internal IRs without breaking the whole thing. I actually went yesterday and changed how arrays are represented by the low-level IR. There are things that still need cleaning up, but it was a fairly painless process. And before you ask, the compiler is big; its currently around 8800 lines of code and supports x86-64 and the integer ISA of RISC-V.

### OOP And Design

I believe that object oriented programming is a bad thing. That's not to say we shouldn't have structure in our programs. But I believe OOP is one of the worst way to do things and encourages bad programming and bad software. There's a lot of discussion in the ways OOP is considered bad, but I think it most manifests itself when it comes to design.

I want to make it clear that idea behind grouping variables and functions the way classes do is a good one. In my opinion, the bad aspect of OOP comes with inheritence. You have your base class, then you inherit to make a new class, and then you can inherit again, and again. And not to mention, you can several of these long trees of inheritence. This was the method I've used with my AST, and its a model I've seen other projects use. You basicaly have a base AST node (a base class). Then you might have another class that inherits from it to become an operator. Then you can inherit from the operator class to have an add, subtract, multiply, or divide operator. This is just one example.

Now what happens if you want to go change something? In some instances, this might not be so bad, but if it were something like a function or a variable in a higher class, you have to make sure to catch it in all the lower classes or weird things will happen.

If you want to redo this entire structure, you're probably screwed. You basically have to redesign the entire class structure, then go through your program and change everything there. In many cases, its a complete rewrite at that point.

It gets more complicated if its a large project many people work on. It gets to the point where no one knows what everything does. The result: no improvements get done because everyone is scared to touch the code, and instead, everyone just adds a new class to do what they need to do.

OOP really locks you into your design choices. This is a bad thing in programming. Even if you sit down and plan everything out in advance, you will inevitably run into issues, or decide that something would work better if designed a different way.