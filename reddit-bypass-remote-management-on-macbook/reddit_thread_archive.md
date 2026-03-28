
**Posted by:** u/Scutched  
**Subreddit:** r/mac  
**Date:** 2021-09-05 08:28 UTC  
**Score:** 230 upvotes | **Comments:** 247  
**Source:** https://www.reddit.com/r/mac/comments/pi9beh/bypass_remote_management_on_macbook_pro_after/

---

## Original Post

I go through this everytime I do a clean install on my macbook. And I forget everytime. I just spent 90 mins reading the posts on this that got me nowhere, until I remembered. People keep mentioning getting to the internet setup screen and just saying that you don't have an internet connection. That has never worked.What I realize is that eventhough I have done a format of the drive my macbook is still remembering my wifi network and password. If I turn off wifi in the recovery mode it comes back on in the setup. That is what activates the Remote Management.

The fix is: you have to turn off your wifi from your modem so there is no way the laptop can connect to the old network, or any previously saved network. Turn off the modem if you have to. That works like a charm. Then don't connect to any wifi during the setup and you are fine.This was on a 2012 Macbook pro after I did a clean install of Catalina.

However, I have never been able to get rid of the "device enrollment" notification nag that pops up at least once a day in the upper right hand corner. I tried one of the fixes out there, but it didn't work for me. I just click it to close it. I am just used to it.

---

## Comments

---
**borisdann** | Score: 8 | 2023-10-10 08:47 UTC

My M1 MBP was stuck on Remote Management when logged in and there is no way to close the prompt. This happened when upgrading my Mac from Ventura to Sonoma.

**Note**: This only works on Monterey and newer versions. Tried Sonoma and Ventura but no option to skip the Internet connection, it is mandatory!

Here is my workaround for cases when you are in office and can't turn off the WiFi.

1. Make a macOS bootable USB
2. Boot your Mac in Recovery mode, open Disk Utility app and erase the Mac.
3. Connect bootable USB to Mac and choose the USB as the starup device to install macOS.
4. You have to activate the Mac before installation which needs Internet connection. At this time, enable mobile hotspot on your phone and connect your Mac to this mobile hotspot. (\*\*\* Very important\*\*\*)
5. The installation will begin and you will see a progress bar. When the screen goes back, press any key to show the progress. (\*\*\*Internet connection is required\*\*\*)
6. When the progress bar reaches to 100% and apple icon shows, turn off the hotspot on your phone immediately.
7. When choose a network window appears, choose without network and proceed to finish the setup process.

  ---
  **[deleted]** | Score: 2 | 2025-05-12 05:05 UTC

  This worked for me on a 2020 MacBook Air Apple M1. I used my Late 2013 macbook pro to get Bug Sir Installer. Used a 1TB SSD as the Boot Disk. Set the 2020 MacBook Air to Big Sur and upgraded to Sequoia 15.4.1. Got 1 remote management notification so far and will try terminal commands to turn it off.

    ---
    **JetLifeShaun** | Score: 1 | 2025-08-05 14:22 UTC

    Any luck with this ?

  ---
  **Aggravating-Step-534** | Score: 1 | 2024-05-29 09:51 UTC

  j'ai essayé et ça marche merci pour l'astuce

    ---
    **Sea_Suggestion7915** | Score: 1 | 2025-09-15 16:48 UTC

    Happy cake day

---
**R1kid07** | Score: 8 | 2025-02-16 10:53 UTC

Adding what worked for me.

Ran through the steps from this post:  
[https://www.reddit.com/r/mac/comments/pi9beh/comment/irku82d/?utm\_source=share&amp;utm\_medium=web3x&amp;utm\_name=web3xcss&amp;utm\_term=1&amp;utm\_content=share\_button](https://www.reddit.com/r/mac/comments/pi9beh/comment/irku82d/?utm_source=share&amp;utm_medium=web3x&amp;utm_name=web3xcss&amp;utm_term=1&amp;utm_content=share_button)

then as soon as I could open terminal I ran the following commands:

sudo chmod 77 /etc/hosts  
  
`echo "0.0.0.0 iprofiles.apple.com" &gt;&gt; /etc/hosts`  
`echo "0.0.0.0 mdmenrollment.apple.com" &gt;&gt; /etc/hosts`  
`echo "0.0.0.0 deviceenrollment.apple.com" &gt;&gt; /etc/hosts`

so far things are looking good.

  ---
  **Individual_Theme_527** | Score: 1 | 2025-08-13 10:12 UTC
