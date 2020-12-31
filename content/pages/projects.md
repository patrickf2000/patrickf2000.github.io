title: Projects
status: hidden

I do most of my learning through interesting side projects. Some of them are only that, but a few have grown up to become useful tools (to me at least...). This is not an all-inclusive list, these are just my best and favorite projects.

## Lila

Lila is a compiler and programming language. The language is a descedent of my Quik language. I actually considered keeping that name because I like it so much, but it was starting to get over used. Oh well. I really like the name "Lila" too. I actually was going to use something else similar to "Lila", but for certain reasons I couldn't.

The compiler is written completely in Rust, and only uses the standard library. Currently, it supports the x86-64 and most of the RISC-V architectures, and it is ready for other architectures. At the time of writing (December 2020), I'm making some core syntax and runtime changes, so I made the repository private.

I'm going to try to keep a log of development. You can find it [here](pages/lila-log.html).

Here's a screenshot of the language:

![Photo]({attach}images/dash.png)

## AS

A simple assembler for the x86-64 architecture. It is capable of generating relocatable ELF objects, which can be linked (using the system linker) as an executable or a library. You can also link it to other libraries, including the C library. It supports a number of instructions and uses the Intel syntax (the AT&T syntax is a horror).

The primary purpose (other than being a great learning experience) is to be the assembler for my Dash compiler.

## Quik

This was my original programming language and compiler. There are- yes- three versions on Github. The oldest was actually an interpreter; it was my first major language tool. The second was my first attempt at an actual compiler. The third was also a compiler. The different between the two compilers is the third was done relatively more correctly; it had an abstract syntax tree and an intermediate layer for generating assembly. The original compiler used a rough AST and went straight to 32-bit assembly code.

I'm proud of these projects, even though they represent a different time and place.

## Extcc

This was fork of Quik 3 that I briefly worked on. Its honestly a mess, and I don't touch it anymore. Extcc was meant to be an easy-to-extend C compiler. I will say though, I am happy with how far it did get.

## Javac

Despite its name, its not an actual Java compiler. This was a fun learning experiment to generate JVM-compatible code. This was one of my favorite projects just because it was so thrilling when I finally got it to work. And yes, it has awful code. I wrote this before I learned you can serialize structures and output them straight to binary.

I will eventually have to do another JVM-related project...

## QuikVM

There are actually two QuikVMs- one written in C++, and the other written in Haskell. These were my first attempts at writing application-level virtual machines- kind of like the Java VM.

## CppEditor

My personal text and code editor. Okay, actually it is on and off depending on the distro I'm using. I started this project back in either 2016 or 2017- I think early 2017. Originally, it was a learning experience and a fun project. I ended up going down the feature-creep path, so in 2018, I forked it and cleaned up a lot of crap out of it. I also ended up changing the license, which is why the Git history and the license only goes back to 2018. Over this past summer, I began working on it again so I could have a text editor like the old Gedit I could use anywhere.

Here's an older screenshot. Actually, its really not much different now. The only thing you can't see is the explorer panel to the side:
![Photo]({attach}images/cppeditor.png)


## CppSheets

This honestly is one of my favorite projects of all time. Its my spreadsheet program which I worked on and off for over a year. Some of the features:

- Multi-document interface, with multiple pages per workbook   
- Cell and text formatting   
- Custom file format and basic MS Excel (xlsx) support   
- Excel-like formulas
- Basic graphing

Here's a screenshot:
![Photo]({attach}images/CppSheets_linux.png)


## CppExplorer

For some reason- and I do not know why- in terms of views and stars, this is my most popular project, even though I haven't worked on it in two years. This is a Linux file explorer; its very similar to modern file explorers you find on Linux. It has a side pane with places and mounted drives, icon and list views, tabs, and a lot more. This was a really fun project back in the day.

Here's a screenshot:
![Photo]({attach}images/cppexplorer_base.png)

## CppMediaPlayer

Another personal program of mine; I use this on and off depending on the distribution. This is a simple video/music player.

![Photo]({attach}images/cppmediaplayer.png)

## Notepad

A simple, ad-free Android notepad. I wrote this a few days after I got my Android smartphone a few years back, and I've been using it ever since.

![Photo]({attach}images/notepad.jpg)

## Other

There's a lot of other stuff, both on Github and unpublished. Some of the other things I've written are:

- A simple HTTP web server
- A graphical backup program
- A simple web browser (uses the Qt webengine)
- A Linux log file viewer
- A PyQt text editor
- A cparser written in Ada
- A few smaller compilers

