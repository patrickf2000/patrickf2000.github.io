title: Lila Compiler Development
status: hidden
save_as: pages/lila-log.html

The development logs for my Lila compiler and language.

### 12/13/2020

Not much today. I started on a very rough draft for a standard library.

Basically, here's the idea. Originally, I was going to make a standard library a more or less optional thing- my idea wasn't to confine the language to a standard other than the language itself. I'm thinking I may change my stance on that. Programming will become a _nightmare_ if the user has to deal with different APIs on every platform, or even the same platform if they want to use the C library vs the Lila library. My solution to that is create a set of standards that any Lila program can use. To the program itself, it won't matter what library, API, or platform they are on; the user can compile and link however they want. In the case of the C library, the function calls will be to equivalent C functions. Maybe eventually I can implement inlining to eliminate function call overheads. Or maybe explicit inlining- that's an idea. Otherwise, the calls may be pure Lila functions, or even something else.

This week is the last week of school, so I'm not sure how much time I'll have to develop this. But I'll post if I do either decide on something or do it.

### 12/12/2020

Originally, this project was named "Dash". A friend came up with the name, and I really really like it, but I decided to change it for a few reasons. First, I think I tried releasing it too early. Its pretty complete, and can do a few non-trival things, but I should not have posted on it as early as I did. That said, I am glad that I made it open source when I did. The second reason is that I'm thinking about some non-trivial syntax changes (mainly inspired by Pascal and Ada), so if I change it enough, it really needs to be something different. The final reason kind of builds onto the second. The name Dash is somewhat similar to Quik, which is partly why I went with it. However, I feel like it gives an impression of something the language is not, and if I change it enough, I won't be similar to Quik.

I also decided to drop my work with porting it to my custom assembler. That is still a long-term goal, but my current assembler is kind of a mess and not really that stable. I have the base of new one written in Ada in storage so to speak, so when I resume work on that, and if it works out, I will probably port it to that. I also dropped the work because I really wanted to get started with other architectures.

That said, the work and everything wasn't all wasted. I created two branches for the original Dash stable branch and the last state of the development branch before the rename. I created new development and stable branches and renamed everything. I also updated all the documentation.