3
sieffy
•
4y ago

What version of Mac OS I’m on Big Sur and people are saying this method won’t work for anything that’s newer than catalina

3
Interesting-Egg306
•
4y ago

I'm trying to figure this out too on a client's MacBook Pro running Monterey. Haven't found a solution yet.

3
9 more replies
Excellent_Hold_117
•
2y ago

This worked. Keep getting the RDM pop up though...Is there a way to make those stop?

2
1 more reply
kickintheeye1
•
4y ago

If you replace the hard drive will it get rid of RM?

2
8 more replies
tonyle3k
•
4y ago

anyone got this working for Monterey?

2
ABGinTech
•
4y ago

Have you found a working solution for Monterey?

4
19 more replies
Realistic-Frame-4162
•
4y ago

I got high sierra and literally turned modem off while on last loading screen when logo comes on and it worked. Only been cpl hours but haven’t got any notifications either

2
5 more replies
Necessary_Age4828
•
3y ago

Thank you so much for writing this! Saved my ass today!

I was afraid it was actually "Game over" for me and the laptop. Apprently it was bought for one company registered in Apple, and later passed over to another company and it demanded for me to configure Remote Management with no other option, even thought he server wasnt reachable and probably will never be, since we dont have access to internal network of the past company. Dont ask me why their mdm was configured only for internal network.

2
thenewquestions
•
2y ago

Posting because this was the top hit in google search. I had a Macbook air early 2020 model with the intel i3 chip and Ventura Os that I purchased second hand on FB marketplace. Upon getting home, I went through the setup without paying much attention to it assuming it would all work fine.

I loaded my wifi info, and then clicked "ok" when it notified me that the laptop was owned by "such and such school district" not really knowing what It meant. It then installed a bunch of remote management stuff and finally ended up at a login screen, waiting for a username and password that I didnt have.

I went on a google-thon trying to fix the issue. There is so much useless info on this topic its unbelievable. What finally ended up working for me was CONTACTING the person I bought the macbook from. They worked at the school district that "owned" the mac. They missed disabling this one before reselling.

After I confirmed that they removed the device from their system, I used the recovery assistant (boot mac, hold command + R key), opened Disk Utility and erased the Macintosh HD (not base os data). After erasing it, I was able to reinstall Ventura from the option within the recovery assistant. Once the setup was complete, I re-entered my WIFI info, and the mac recognized that the mac was "released" from ownership and I was able to load my apple ID in as one would expect. No issues from that point.

If I wasnt so lucky in being able to contact the owner, my next step would be to install Monteray Os from a bootable drive, and do the installation with WIFI modem OFF. Select "this computer does not use the internet" under "other network options" when it asks for your wifi info during initial setup. This should bypass the ownership deal. Its not possible to do this "turn off the wifi" trick with Ventura. It needs a network connection.

Good luck!

2
bimodaltuna
•
2y ago

For everyone who came far and got the access to the MB but cannot make the notifications stop:

Found this on a thread online, worked like a charm for me(MBP 2019)

"Editing the hosts file appears to have worked all by itself. There's no need to reboot into Recovery Mode, disable SIP or FileVault, or move/disable the plists controlling the daemons related to device enrollment and management. You can edit the hosts file in Terminal while logged in normally, although not using those "echo" commands (even typing 'sudo echo "0.0.0.0 albert.apple.com" >> hosts' gave the error 'permission denied: hosts'). I googled editing the hosts file, and the trick appears to be to use the nano editor:

Type in terminal: sudo nano /private/etc/hosts. Enter admin password when prompted.

Use Arrow key on your keyboard to move the cursor to the last line and type the following lines:

0.0.0.0 iprofiles.apple.com 0.0.0.0 mdmenrollment.apple.com 0.0.0.0 deviceenrollment.apple.com

Press Control + X from keyboard to Exit.

Now you will be asked to asked whether you want to save and to enter Y for yes and N for No. Type Y [be sure to do this!]

Check to see whether the enrollment calls are being blocked by typing 'sudo profiles show -type enrollment'

You should see an error like this:

(34000) Error Domain=MCCloudConfigurationErrorDomain Code=34000 "The device failed to request configuration from the cloud." UserInfo={NSLocalizedDescription=The device failed to request configuration from the cloud., CloudConfigurationErrorType=CloudConfigurationFatalError}

That should be all there is to it! Many thanks to all those on gist.github.com who proposed various solutions."

-Odysseus the goat(found the goat's comment on apple.stackexchange)

2
9 more replies
[deleted]
•
2y ago

Any way to make this work on Sonoma? 14.3.1? The very first screen is "Activate Mac" which requires internet.

2
Lorinloewe4444
•
2y ago

Worked like a charm thanks

1
Objective-Pea-4569
•
2y ago

The MDM finally took over my device. I can’t get past it. I can’t click on anything. I can’t even shut my device down. It is totally frustrating.

1
[deleted]
•
4y ago
Related Answers Section
Related Answers
Disable remote management on Mac
Meaning of MDM lock on Mac
Remote support options for Mac
How to connect to Mac mini remotely
MacBook locked by organization solutions
New to Reddit?

Create your account and connect with a world of communities.

Continue with Email
By continuing, you agree to our User Agreement and acknowledge that you understand the Privacy Policy.
More posts you may like
Bypassing Employer's MacBook's Remote Mgmt
r/macbook
•
2y ago
Bypassing Employer's MacBook's Remote Mgmt
28 comments
deviceatlas
•
Promoted
Cookie deprecation is going to mean advertisers miss out on a tonne of data...making device data all the more valuable. Enter DeviceAtlas...
deviceatlas.com
Read More
Is it me or macOS Catalina is the only one having this?
r/hackintosh
•
4mo ago
Is it me or macOS Catalina is the only one having this?
26 upvotes · 14 comments
remote management??
r/mac
•
1y ago
remote management??
16 comments
Fresh OS install and I'm now stuck on "Remote Management" screen
r/mac
•
4y ago
Fresh OS install and I'm now stuck on "Remote Management" screen
188 upvotes · 150 comments
How to know if your MAC has MDM Profile installed
r/mac
•
3y ago
How to know if your MAC has MDM Profile installed
89 upvotes · 85 comments
Does anyone know how to remove remote management from the iphone 14?
r/iphone
•
2y ago
Does anyone know how to remove remote management from the iphone 14?
21 comments
How to remote access windows PC from my MacBook
r/mac
•
8mo ago
How to remote access windows PC from my MacBook
7 upvotes · 13 comments
WTH is this and how do i bypass it? i'm a mac noob
r/MacOS
•
7mo ago
WTH is this and how do i bypass it? i'm a mac noob
335 upvotes · 146 comments
Macbook Setup
r/macbook
•
2mo ago
Macbook Setup
32 comments
My 2017 MacBook 12 was slow and overheating on Ventura… a clean install fixed everything
r/mac
•
17d ago
My 2017 MacBook 12 was slow and overheating on Ventura… a clean install fixed everything
132 upvotes · 30 comments
Remove nail polish without nail polish remover
r/lifehacks
•
3y ago
Remove nail polish without nail polish remover
483 upvotes · 41 comments
painful lump on nipple 6months post op
r/TopSurgery
•
9mo ago
painful lump on nipple 6months post op
2
7 upvotes · 4 comments
Is my iPhone no MDM or bypassed?
r/applehelp
•
2mo ago
Is my iPhone no MDM or bypassed?
3 comments
Brand new MacBook Pro (M5 Pro) has severe network issues
r/MacOS
•
9d ago
Brand new MacBook Pro (M5 Pro) has severe network issues
25 comments
The recovery service could not be contacted - MacBook Pro 2017
r/mac
•
1y ago
The recovery service could not be contacted - MacBook Pro 2017
7 upvotes · 31 comments
Trying to use migration assistant but keeps saying “unable to connect to MacBook Pro”
r/mac
•
3mo ago
Trying to use migration assistant but keeps saying “unable to connect to MacBook Pro”
6 upvotes · 4 comments
[Cisco] Doesn't MAC Authentication Bypass kind of defeat the purpose of 802.1x?
r/networking
•
13y ago
[Cisco] Doesn't MAC Authentication Bypass kind of defeat the purpose of 802.1x?
10 upvotes · 15 comments
Get a Mac they said. It'll clean up your setup they said...🫣
r/mac
•
4mo ago
Get a Mac they said. It'll clean up your setup they said...🫣
645 upvotes · 91 comments
How to treat thiss it irritated a lott
r/IndianSkincareAddicts
•
2mo ago
SPOILER
How to treat thiss it irritated a lott
3 upvotes · 3 comments
I want to recover data from my broken MacBook Pro 2015
r/mac
•
1y ago
I want to recover data from my broken MacBook Pro 2015
5 upvotes · 16 comments
Why do my clothes have marks on them after washing machine?
r/laundry
•
1y ago
Why do my clothes have marks on them after washing machine?
4
2 upvotes · 6 comments
Remote access a Mac for a month without being physically present near it
r/MacOS
•
4mo ago
Remote access a Mac for a month without being physically present near it
57 upvotes · 111 comments
Marshall minor III. The right earpud stopped working
r/marshall
•
2y ago
Marshall minor III. The right earpud stopped working
9 upvotes · 14 comments
Brand new M4 MacBook Pro - MagSafe stopped working after 3 months (USB-C charging works)
r/mac
•
1mo ago
Brand new M4 MacBook Pro - MagSafe stopped working after 3 months (USB-C charging works)
6 upvotes · 20 comments
Valve Anti Cheat was unable to verify that your machine is secure
r/DotA2
•
2y ago
Valve Anti Cheat was unable to verify that your machine is secure
22 upvotes · 54 comments
VIEW POST IN
日本語
Français
Public
TOP POSTS
Reddit
reReddit: Top posts of September 5, 2021
Reddit
reReddit: Top posts of September 2021
Reddit
reReddit: Top posts of 2021
Reddit Rules
Privacy Policy
User Agreement
Accessibility
Reddit, Inc. © 2026. All rights reserved.
Collapse Navigation
RESOURCES
About Reddit
Advertise
Developer Platform
Reddit Pro
BETA
Help
Blog
Careers
Press
Best of Reddit
Reddit Rules
Privacy Policy
User Agreement
Accessibility
Reddit, Inc. © 2026. All rights reserved.