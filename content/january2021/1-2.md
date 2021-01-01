Title: Raspberry Pi Router and Filter
Date: 2021-01-02 09:38
Category: None

Raspberry Pi's have a reputation for being one of the most versatile computers out there. And for a good reason- they are cheap, portable, tiny, and they run Linux. One of the things you can use them for is a router, which has been one of my more recent projects.

Okay, I'm not talking about a router for your house, although I've heard you can do that. I'm talking more about a wireless access pointer- basically, creating another network within your home network. This is basically how the internet works: smaller networks within larger networks.

Why would you want to do this? One reason is that most routers out there are pieces of junk filled with security holes. Doing this can provide an extra layer of protection. Another reason would be as a content filtering device. There are applications that can filter ads, bad websites, and more. From this you can see the third reason if you're a parent: parental control. I'm doing it for two reasons. One, an experiment. Two, I get distracted easily.

Its actually more the distraction thing. As great as it is, the internet is also a major sinkhole. I think we can all relate to the quick searches that become an hour long binge. Or that task you sit down at your computer to do and never really do. The damage internet distractions can do is a real thing. Don't believe me? Read _The Shallows_ by Nicholas Carr. After that, listen to the Joe Rogan podcast with Tristan Harris.

Before you say that this is an extreme way to do it, let me say its really not. Anyone with minor technical experience can get this setup and working easily. Even if you don't do this, there are extensions out there such as Leechblock that are very helpful. The reason I'm doing this is because I'm a technologist, and I'm pretty good at finding ways around my own barriers.

I've been using this method for a few weeks now, and its been really helpful.

### My Setup

Due to the absolute unusability of the so-called media room in my house, the router is in my bedroom. And its a win for everyone. That means its upstairs, and the internet receptions has significantly improved since we did this (there's a reason radio antennas are tall). But for me, it means I can plug all stuff into the router. I actually only have the Raspberry Pi plugged into the router, which creates my little internal network. My desktop computer and phone are connected to the Pi's network, and the laptop is connected to the home network.

The reason for that is that I block literally everything on the Pi router. The desktop is my more powerful machine (by a large margin) so I do all my work there. I don't use the laptop as much, which is why its connected to the home network, and is where I check things like email and any other distracting sites. But that doesn't mean I can go on a binge from the laptop. I have Leechblock in the browser. Yeah, extreme.

When I say distracting website, I don't just mean things like Youtube and Reddit. Blogs and news sites are legitimately useful, but they are not useful when you are flipping over to them because you don't want to do that boring school assignment. The logic behind this approach isn't to stay off the internet. Its to control it. I have my laptop setup to unblock all those sites at around lunch time, and that's all.




### Conclusion
