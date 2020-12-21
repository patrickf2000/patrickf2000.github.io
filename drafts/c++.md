Title: My Love and Hate of C++
Date: 2020-08-19 09:38
Category: None

If I've ever had a true love-hate relationship with something, its C++. If you scroll through my projects, you may be surprised, and rightfully so. There's so much C++ stuff there, and I constantly find myself using it. In a work capacity, I still use it, but as far as indepdent projects go, I've begun to move away. This post is just meant to be my take on the subject.

I want to qualify that I don't absolutely hate the language. Even in my indepdent projects, I still think C++ is the best bar none for GUI projects. Qt and C++ are really the best.

### Complexity

This is my biggest dislike of C++. And I don't mean in the sense that the language is huge. Its huge, but I don't think its ridiculous really until you get to around the C++14 standard. The C++20 standard is something else... Let's not go into that :). There does have to be a fine line between simplicity and usability. On one end of the spectrum, you have C and Go that are almost too small (C is good for OS and hardware related things, but once you get into userspace, I think its just too small). And on the other end you have D which is just a monster.

When I say complexity, I'm talking about code bases. This can be a problem with any language, but I think its especially one with C++. I've worked on C++ projects that have grown into these huge things that only a handful of people actually understand and become incredibly fragile to the point that any real improvements can't be done. I had this happen in one of my side projects. My last compiler implemented in C++ was between 5-6000 lines of code at its peak. Another older one was around 4500 lines. I admit, in comparison to a lot out there, that isn't as much, but it did get to the point where I didn't feel I could do anything with the projects without literally everything breaking. In contrast, my new compiler is written in Rust and is about 8400 lines in size, and I've had no issues making huge changes to it.

Complexity is becoming a huge issue in computer science- huge projects that only a handful of people understand. As the new generation of programmers like myself are entering the industry, that will be a problem where you just can't do anything with some of the code out there. From a hardware standpoint, it will also become an issue since raw speed isn't increasing in the way it use to. Actually, I'll have to do a post on that at some point.

### Preprocessor

This is the one area I'm really glad the C++20 standard is addressing. This used to not bother me until I started working on a large project where a slight change in certain headers would lead to basically the entire thing rebuilding. I guess things don't bother you until you see the reality...

Okay, I understand why this happens, but there are better ways than that. Most modern languages use the concept of modules (and even some older ones- Ada has an amazing module system). And this is great because you can make changes that won't trigger basically complete rebuilds, linking errors, and all kinds of other issues.

### Variables

This is a more subjective think that applies to C-family languages as a whole, and its not something that would keep me from using a language.

Languages like Pascal, Ada, and I think Fortran require all variables to be declared at the start of a function.