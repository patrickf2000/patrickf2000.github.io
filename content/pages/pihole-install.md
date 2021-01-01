title: Pi-Hole Installation
status: hidden
save_as: howto/pihole-install.html

### Installing Pi-Hole

Pi-hole is a DNS filtering system. Or as some people call it, a black hole. Incoming or outgoing connectings that are on the Pi's blacklist are simply dropped. Pi-hole is free, open source, and easy to use.

Let's dive into this. First, download and install Pi-Hole: `sudo curl -sSL https://install.pi-hole.net | bash`.

Click "Ok" through the first few screens. When you come to the screen asking about network interfaces, choose `wlan0`:

[IMAGE HERE]

On the next screen, it will ask about your DNS provider. I'm not sure how much it actually matters, so just go with Google (the default):

[IMAGE HERE]

The next screen will ask you about ad blocking lists. That's another cool thing about Pi-hole; other than blocking domains of your choice, it can also block ad sites. By default, both were selected; you can just leave it as is.

[IMAGE HERE]

The next screen will ask about what protocols to use. You can just leave this as is.

The following screen will ask about the static IP address. *Answer no* here. As you remember, the Pi serves domains in the 192.168.4 range. Your home router takes care of the rest.

[IMAGE HERE]

On the next screen, we specify that range:

[IMAGE HERE]

The next screen asks about the gateway; this is simply the Pi's IP address:

[IMAGE HERE]

Make sure the settings look like the image below. If so, you can continue.

[IMAGE HERE]

Click through the next screen. The one after will ask if you want to install the web interface. Click yes to this. It will make it much easier to configure if you do that. The screen following will ask if you want to install lighttpd server. Click yes to this.

The next screen will ask about logging queries. I would say this depends on what you are trying to do. I would just leave it on by default, but if you have a reason not to, that is certainly okay. The web interface does require a password to login, so if you're the only one with the password... You're the only that can see. Actually, I think you change this setting later on through the interface. The screen afterward will ask what level of logging you wish.

When everything is complete, you will see a screen with some information. *Important*: Make sure you take note of the generated password near the bottom. You will need this to log in.

### Blocking DNS Bypassing

This step is only necessary if you are trying to set this up as a parental control device. Remember the step where we chose our DNS server? In some cases, you can go around Pi-hole by changing this setting. The following commands will prevent this from happening and make sure that any requests go through the Pi.

```
sudo iptables -A PREROUTING -t nat -p udp --destination-port 53 -j REDIRECT --to-ports 53
sudo iptables -A PREROUTING -t nat -p tcp --destination-port 53 -j REDIRECT --to-ports 53
sudo iptables-save | sudo tee /etc/iptables/rules.v4
```

### Pi-Hole Configuration

Okay, now go to `http://192.168.4.1/admin`, click the login button on the left sidebar, and login. This is web interface for Pi-hole.

[IMAGE HERE]

Once you're logged in, click on "settings" in the sidebar, and click on the DHCP tab. Check the box title "DHCP server enabled". You can ignore the red flashing warning; you don't have to do anything to your home router. Nothing on your home network will be affected. The Pi creates a little bubble that only affects computer connected to it. If you don't believe me, go to another computer connected to your home network, and trying logging in to Pi-hole. It won't work.

[IMAGE HERE]

At this point, you can start adding sites you want blocked. Click on the blacklist tab, and you should see a screen like below. When you add domains, one useful thing might be to add the domain, then add it again with that box "Add domain as wildcard" checked. This will prevent access to subdomains.

[IMAGE HERE]

### Clearing DNS Cache

### Conclusion
