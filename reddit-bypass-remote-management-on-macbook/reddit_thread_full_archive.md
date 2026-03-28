# Bypass remote management on Macbook pro after clean install Catalina - solved

**Posted by:** u/Scutched  
**Subreddit:** r/mac  
**Date:** 2021-09-05 08:28 UTC  
**Score:** 234 upvotes | **Comments:** 247  
**Source:** https://www.reddit.com/r/mac/comments/pi9beh/bypass_remote_management_on_macbook_pro_after/

---

## Original Post

I go through this everytime I do a clean install on my macbook. And I forget everytime. I just spent 90 mins reading the posts on this that got me nowhere, until I remembered. People keep mentioning getting to the internet setup screen and just saying that you don't have an internet connection. That has never worked.What I realize is that eventhough I have done a format of the drive my macbook is still remembering my wifi network and password. If I turn off wifi in the recovery mode it comes back on in the setup. That is what activates the Remote Management.

The fix is: you have to turn off your wifi from your modem so there is no way the laptop can connect to the old network, or any previously saved network. Turn off the modem if you have to. That works like a charm. Then don't connect to any wifi during the setup and you are fine.This was on a 2012 Macbook pro after I did a clean install of Catalina.

However, I have never been able to get rid of the "device enrollment" notification nag that pops up at least once a day in the upper right hand corner. I tried one of the fixes out there, but it didn't work for me. I just click it to close it. I am just used to it.

---

## Comments

> *Comments are ordered by top score. Indentation reflects nesting depth.*

---
**borisdann** | Score: 7 | 2023-10-10 08:47 UTC

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
**R1kid07** | Score: 7 | 2025-02-16 10:53 UTC

Adding what worked for me.

Ran through the steps from this post:  
[https://www.reddit.com/r/mac/comments/pi9beh/comment/irku82d/?utm\_source=share&utm\_medium=web3x&utm\_name=web3xcss&utm\_term=1&utm\_content=share\_button](https://www.reddit.com/r/mac/comments/pi9beh/comment/irku82d/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

then as soon as I could open terminal I ran the following commands:

sudo chmod 77 /etc/hosts  
  
`echo "0.0.0.0 iprofiles.apple.com" >> /etc/hosts`  
`echo "0.0.0.0 mdmenrollment.apple.com" >> /etc/hosts`  
`echo "0.0.0.0 deviceenrollment.apple.com" >> /etc/hosts`

so far things are looking good.

  ---
  **Individual_Theme_527** | Score: 1 | 2025-08-13 10:12 UTC

  It worked for me too
  
  
  Sequoia System

    ---
    **Remote-Newt4733** | Score: 1 | 2025-09-30 12:57 UTC

    could you use mac normally after that? icloud,internet,downloading apps etc?

      ---
      **Individual_Theme_527** | Score: 1 | 2025-10-10 16:27 UTC

      Estou usando a 2 meses e o resultado é satisfatório, uso tudo normalmente mas demorou um pouco ate eu conseguir deixar o sistema 100%

---
**jKaz** | Score: 6 | 2021-09-28 23:47 UTC

Did you figure out how to remove the notifications to connect to remote management after?

  ---
  **Scutched** | Score: 20 | 2021-09-29 00:26 UTC

  This is what I was gonna try. But I haven't had the ambition. The Device enrollment popup only comes up once a day. I have Catalina, so I hope this works too. Seems I read that it did or I wouldn't have saved it.
  
  If you have Catalina and it works, let me know. It is formatted more clearly in the link.
  
  [https://apple.stackexchange.com/questions/297293/turning-off-device-enrollment-notifications-on-macbook-pro](https://apple.stackexchange.com/questions/297293/turning-off-device-enrollment-notifications-on-macbook-pro)
  
  This works for macOS Big Sur to Disable MDM notifications
  
  "Restart in Recovery Mode Restart your Mac then hold down the Command & R keys together until you're in the Recovery Mode menu (Command+R)
  
  Click on Utilities (top menu bar) then select: Startup Security Utility
  
  A 3-choices popup appears: select (No security) (there is no confirmation button to press)
  
  Restart again in Recovery Mode (Command+R)
  
  Click on Utilities (top menu bar) then select Terminal
  
  type in: mount then press enter/return
  
  A list of things will show up once you enter in (mount) in Terminal Write down the disk associated with /Volumes/Macintosh HD (mine was /dev/disk2s5) Note: it's not /, and it's not /Volumes/Macintosh HD - Data
  
  Next, in Terminal, write: umount /Volumes/Macintosh\\ HD
  
  then: mkdir /Volumes/Macintosh\\ HD
  
  then: mount -t apfs -rw /dev/disk2s5 /Volumes/Macintosh\\ HD
  
  then: cd /Volumes/Macintosh\\ HD/System/Library/LaunchAgents
  
  then: mkdir xtemp
  
  then: mv com.apple.ManagedClientAgent.\* xtemp/
  
  then: mv com.apple.mdmclient.\* xtemp/
  
  then: cd ../LaunchDaemons
  
  then: mkdir xtemp
  
  then: mv com.apple.ManagedClient.\* xtemp/
  
  then: mv com.apple.mdmclient.\* xtemp/
  
  then: csrutil authenticated-root disable (this will Turn off Signed System Volume SSV)
  
  then lastly: bless --folder /Volumes/Macintosh\\ HD/System/Library/CoreServices --bootefi --create-snapshot (this will Save the current disk status in the boot snapshot)
  
  Now you can restart your Mac, DEP notification is disabled."

    ---
    **jKaz** | Score: 9 | 2021-10-18 18:04 UTC

    
    I needed up choosing a different response from that post, it was really easy and I think it worked
    
    my formatting is trash but its like 3 replies down from the link you sent
    
    
    
    First, block your Mac from reaching the domain iprofiles.apple.com. I use LittleSnitch as my firewall, so I blocked it there, but you can also use your hosts file like:
    
    sudo echo "0.0.0.0 iprofiles.apple.com" >> /etc/hosts
    Then, I checked the current enrollment profile
    
    sudo profiles show -type enrollment
    This will show you the current enrollment configuration your Mac has, you can even block the domain mentioned in ConfigurationURL just to be safe.
    
    After than, I proceed to delete the profile, in my regular session, not recovery, although it would probably also work in recovery:
    
    sudo profiles remove -all
    Keep in mind that this command will delete all other profiles you may have, in my case, I didn't more.
    
    Finally, you can check for the enrollment profile again, I would get an error saying that it could not retrieved given that I blocked the domain from where it's retrieved:
    
    sudo profiles show -type enrollment
    Error fetching Device Enrollment configuration: (34000) Error Domain=MCCloudConfigurationErrorDomain Code=34000 "The device failed to request configuration from the cloud." UserInfo={NSLocalizedDescription=The device failed to request configuration from the cloud., CloudConfigurationErrorType=CloudConfigurationFatalError}
    And the notification is gone for good. I'll report back in the next OS upgrade to see if it comes back.

      ---
      **lilylikesfood** | Score: 1 | 2025-02-09 19:11 UTC

      Hi! 
      So is this the way just block the notification? Or it’s also the way to stop my laptop from being locked by remote management? Thanks…
      My laptop got locked by remote management and I’m trying to figure out how to solve this…… 
      Im struggling a lot it would be amazing if you can still answer me😭😭😭 thank u so much 😭😭😭

        ---
        **jKaz** | Score: 1 | 2025-02-09 20:57 UTC

        Not sure. It happened to me when i tried reformatting a laptop I bought from a company closing sale after I reformatted.
        
        So I would definitely give it a try
        
        Let me Know tho

      ---
      **J220493** | Score: 1 | 2025-07-05 02:27 UTC

      Does it works with a MacBook completely erased? I’m stuck here
      
      https://preview.redd.it/v0l41wn8vyaf1.jpeg?width=1080&format=pjpg&auto=webp&s=b7f7f80890be3c79792b989a116fedead972adf3

        ---
        **jKaz** | Score: 1 | 2025-07-05 07:28 UTC

        Dis you disconnect from internet before you wiped?

          ---
          **J220493** | Score: 1 | 2025-07-11 21:24 UTC

          Yes, it didn’t work. I followed other tutorial and this is 100% functional. 
          
          https://youtu.be/vtFi-y3H2Lg?si=wHn7AlEzyf6iIVXm

            ---
            **Independent-Fox6865** | Score: 1 | 2025-07-15 14:39 UTC

            This method works for OS as latest as  Sequoia 

      ---
      **Atari1337** | Score: 1 | 2023-02-19 19:18 UTC

      Thank you so much.
      
      You are a godsend.

      ---
      **XthemastaX** | Score: 1 | 2023-10-11 03:51 UTC

      Never thought it would work on Sonoma with a 15 in 2019 MacBook Pro, but it did. Thanks. I used this command before on Ventura as well

        ---
        **seeking_3rd_wife** | Score: 1 | 2024-09-28 03:44 UTC

        > `sudo profiles show -type enrollment`
        > `Error fetching Device Enrollment configuration: Client is not DEP enabled.`
        
        This is what I get, and I still see a red dot on my Preferences... how can I completely get rid of that too?

      ---
      **who_knocks** | Score: 1 | 2024-02-02 03:58 UTC

      Thank you so much, this worked for me

    ---
    **SangieRedwolf** | Score: 2 | 2022-03-11 14:14 UTC

    This is awesome! The final bless command fails saying I don't have write access. I rebooted and the launch agents/daemons haven't been moved :(

    ---
    **FunkMonster98** | Score: 2 | 2023-05-13 02:23 UTC

    This still totes works! Thanks so much. MacBook Pro 2017, 15-inch. macOS Ventura.

      ---
      **[deleted]** | Score: 1 | 2024-12-28 15:18 UTC

      I’m trying to do mines rn. Can you list the step by step when to disconnect the internet to bypass the remote management, because it keeps saying I need internet to continue. I have the same laptop and I have Ventura

      ---
      **scottwils** | Score: 1 | 2023-08-30 00:41 UTC

      If you ever reset your nv-ram or run an OS update running an unsigned OS will brick your boot volume.

        ---
        **Remomakesmusic** | Score: 1 | 2024-12-22 20:14 UTC

        How do you resign the os

    ---
    **mbjacket81** | Score: 2 | 2025-03-27 15:19 UTC

    This was the only thing that worked for me to get off of my previous company's MDM profile.  I bought the MacBook from the previous company and they removed the MacBook from their MDM management but I continued to get this message.  Fortunately of all the things I have tried, your steps was the only thing that actually worked!  Thank you!

    ---
    **CatCandid1660** | Score: 1 | 2024-01-18 21:22 UTC

    Thank you much! it worked.

  ---
  **Excellent_Hold_117** | Score: 1 | 2024-02-24 17:33 UTC

  Do the pop ups matter? does that mean it's still under remote management? or as long as you cancel enrollment ur good?

---
**wanyewayne** | Score: 5 | 2022-04-26 14:28 UTC

I just found a way that doesn't require turning off the modem. When the internet options come (don't choose a network) up there's an 'other network settings' button. When I clicked it there were three options and I chose the option "My computer does not connect to the internet". This bypassed the managed settings and I'm up and running after a reinstall. After restarting, no managed setting message came up. Macbook pro 2017 running High Sierra 10.13.6

  ---
  **m_vo** | Score: 3 | 2022-10-11 19:05 UTC

  I managed to bypass the RM login by turning off my router during the reboot process. This allowed me to set up my Mac. Once you connect to wifi did the RM settings come back up?

  ---
  **covenantad33** | Score: 2 | 2023-07-06 16:46 UTC

  You are my hero! Thank youuuuuuu

  ---
  **SignificantPull** | Score: 2 | 2024-06-16 00:25 UTC

  Thank you! This worked with Ventura

  ---
  **Kitty_cat_6000** | Score: 1 | 2024-07-01 14:36 UTC

  Omg, thank you so much!! Bless you! 🙏 💖

  ---
  **Informal-Step-5149** | Score: 1 | 2024-12-17 06:36 UTC

  I don't have this option on my laptop. Is there another way for Ventura?

  ---
  **JordanSkole** | Score: 1 | 2022-12-29 00:14 UTC

  Amazing!! Thank you!!!

---
**unitegondwanaland** | Score: 4 | 2023-11-12 23:31 UTC

If you are currently running Sonoma which requires network connectivity during the entire setup process AND your computer shipped with an earlier release, here is my solution.

&#x200B;

1. Boot into recovery mode (Command + R).

2. Using the Disk Utility, erase the local disk so we force a reload of the OS that shipped with your computer.

3. Restart the computer and Perform a NVRAM reset (Option + Control + P + R) to wipe any memory of wifi networks.

4. Restart the computer into recovery mode again (Command + R).

5. Select install OS. When prompted, connect to wifi using only a hot spot on your phone or another wifi source that you can control on-demand. This is the only wifi you want your computer to remember so that it cannot automatically join another remembered wifi network.

6. When the OS download operation is complete, the computer will reboot. When this happens, you need to immediately turn off the hot spot or wifi connection.  You will be prompted to select a wifi network to complete OS setup. Here you can choose “other options” and specify that this computer has no network connection. Continue through the remaining prompts to finish setup.

7. The remainder of the install process will continue and complete after 10-15 minutes. The user that you create during setup will be used later in this process.

8. Once you get to the login page, ensure that wifi is still turned off. If it isn’t, turn it off now.

9. Restart the computer in recovery mode (Command + R).

10. Open Utilities > Startup Security Utility and enter the admin user credentials when prompted. Set the policy to “Reduced Security”, “Medium Security”, or “No Security” depending on the computer and your preference for security. Also, while you are here, you can enable booting from external media (like USB) if you want. Close the security utility.

11. Still in recovery mode, open the terminal and type `csrutil disable`.

12. Restart the computer normally. Do not enter recovery mode. Ensure wifi is STILL OFF.

13. Open terminal from Applications > Utilities and run the following list of commands to disable the MDM agent.

* `sudo mount -uw /`
* `sudo mkdir /System/Library/LaunchAgentsDisabled`
* `sudo mkdir /System/Library/LaunchDaemonsDisabled`
* `sudo mv /System/Library/LaunchAgents/com.apple.ManagedClientAgent.agent.plist /System/Library/LaunchAgentsDisabled`
* `sudo mv /System/Library/LaunchAgents/com.apple.ManagedClientAgent.enrollagent.plist /System/Library/LaunchAgentsDisabled`
* `sudo mv /System/Library/LaunchDaemons/com.apple.ManagedClient.cloudconfigurationd.plist /System/Library/LaunchDaemonsDisabled`
* `sudo mv /System/Library/LaunchDaemons/com.apple.ManagedClient.enroll.plist /System/Library/LaunchDaemonsDisabled`
* `sudo mv /System/Library/LaunchDaemons/com.apple.ManagedClient.plist /System/Library/LaunchDaemonsDisabled`
* `sudo mv /System/Library/LaunchDaemons/com.apple.ManagedClient.startup.plist /System/Library/LaunchDaemonsDisabled`

&#x200B;

14. Still in terminal, run the following to remove the “enroll” notifications.
* `sudo rm /var/db/ConfigurationProfiles/Settings/.cloudConfigHasActivationRecord`
* `sudo rm /var/db/ConfigurationProfiles/Settings/.cloudConfigRecordFound`
* `sudo touch /var/db/ConfigurationProfiles/Settings/.cloudConfigProfileInstalled`
* `sudo touch /var/db/ConfigurationProfiles/Settings/.cloudConfigRecordNotFound`
* `sudo launchctl disable system/com.apple.ManagedClient.enroll`
* `sudo launchctl disable system/com.apple.mdmclient.daemon`
* `sudo launchctl disable system/com.apple.mdmclient`
* `sudo launchctl disable system/com.apple.devicemanagementclient.teslad`

&#x200B;

15. Restart the computer in recovery mode (Command + R).
16. Open the terminal so we can edit the hosts file to block any attempt to register the computer with an MDM provider.
* `cd ../../etc`
* `echo "0.0.0.0 albert.apple.com" >> hosts`
* `echo "0.0.0.0 iprofiles.apple.com" >> hosts`
* `echo "0.0.0.0 mdmenrollment.apple.com" >> hosts`
* `echo "0.0.0.0 deviceenrollment.apple.com" >> hosts`
* `echo "0.0.0.0 gdmf.apple.com" >> hosts`.  //This will disable your Mac from checking and getting any updates. Not required but is an option.

&#x200B;

17. Finish by typing `csrutil enable`

18. Reboot.

19. Log in as your admin user and enable wifi.

20. Open the terminal again at Applications > Utilities to check that your MDM enrollment is not occurring.
* `sudo profiles status -type enrollment` (Should see “No” on both types.)
* `sudo profiles show -type enrollment` (Should receive an error that the device enrollment server is unavailable)

&#x200B;

21. Your Catalina (or other OS version) is now ready to use or update if you want a newer release like Sonoma.

22. Download the Sonoma release from another machine to your USB and install it with WiFi off.

23. Once the install completes, repeat step #20 and confirm you get the same response.

Supporting Resources: 
- https://gist.github.com/sghiassy/a3927405cf4ffe81242f4ecb01c382ac?permalink_comment_id=2791310
- https://gist.github.com/henrik242/65d26a7deca30bdb9828e183809690bd

ENJOY!

Update: I've installed the first two updates for Sonoma (now on 14.2) and still am not MDM managed. :-)

  ---
  **Camp_1993** | Score: 3 | 2024-06-12 15:20 UTC

  Hey! Do you know, if I made an admin account to run this, then after I was all done, made another account as admin and deleted the original account, would it mess with things?
  
  Also what happens when you upgrade from settings instead of a boot key?

  ---
  **TheGuvnorrr** | Score: 2 | 2023-11-24 15:58 UTC

  Hi I’m currently running 14.1.1. I have data that needs backing up on my Mac. Also it’s not allowing me to get onto recovery mode for some reason. Is there any possibility of backing up the Mac before figuring out why I can’t boot into recovery mode

  ---
  **REAL_datacenterdude** | Score: 2 | 2025-04-29 04:36 UTC

  I was doing great with this until I got to step 15, and when doing the first echo, got the dreaded “hosts: Read-only file system”
  
  Tried csrutil disable and rebooted back into Recovery mode, tried again, same result.  Kinda stuck there.
  
  Not sure where to go from here.  I’ve succesfully unlocked it and installed Ubuntu previously but wanted to give this a shot.  Any tricks up your sleeve?

    ---
    **unitegondwanaland** | Score: 2 | 2025-04-29 04:45 UTC

    Try superuser do. (sudo) with your echo command

      ---
      **REAL_datacenterdude** | Score: 2 | 2025-04-29 04:53 UTC

      Unfortunately that had no effect. :(

      ---
      **REAL_datacenterdude** | Score: 2 | 2025-04-29 05:03 UTC

      Is there any reason I couldn’t do these in booted macOS as opposed to in Recovery terminal?  Seem like pretty straightforward commands

        ---
        **unitegondwanaland** | Score: 2 | 2025-04-29 12:26 UTC

        You're welcome to try but that step is there to beat the MDM registration. If you're offline, it's possible you can do it though

          ---
          **REAL_datacenterdude** | Score: 2 | 2025-04-30 03:02 UTC

          I wanted to give a success update and how I got there, in case anyone else runs across this mega-popular thread and hits the same issue.
          
          So, the way I overcame it was to boot back into the OS, insure wifi remains OFF, and manually edit the /etc/hosts file directly in nano with the same entries, as opposed to doing the echo commands as you laid out in step 15 & 16.
          
          That was it.  I was able to successfully update Mojave, then upgrade to Sequoia.  All of the iCloud stuff works just fine, with the sole exception of iMessages, which I'm still looking into.
          
          Thanks for the awesome step-by-step guide with commands! At the end of the day, my phone is always sitting next to me, and if I need to text, I can do it there.  So, not having Messages on desktop is an enormous 1WP that IDGAF about, to be blunt.
          
          It should look like this when you're done.
          
              dcds-mbp:~ dcd$ cat /etc/hosts
              ##
              # Host Database#
              # localhost is used to configure the loopback interface
              # when the system is booting.  Do not change this entry.
              ##
              127.0.0.1 localhost
              255.255.255.255 broadcasthost
              ::1             localhost
              0.0.0.0 albert.apple.com
              0.0.0.0 iprofiles.apple.com
              0.0.0.0 mdmenrollment.apple.com
              0.0.0.0 gdmf.apple.com

  ---
  **Sweet-Clue** | Score: 1 | 2024-06-29 15:52 UTC

  This worked for me and upgraded to Sonoma. Issue I have is logging into imessages. Doesn't seem to want to login for some reason.

  ---
  **Accomplished-Rub734** | Score: 1 | 2024-12-06 06:09 UTC

  so brillant! This solved my situation (very complicated) installing the Catalina (as pre-installed on the laptop) and then upgraded to Sonoma 15.2 directly from Settings/Upgrades. Is important to turn off the wifi or to remove the auto join from the wifi connect, in this why you have the control. Grateful forever!

    ---
    **unitegondwanaland** | Score: 1 | 2024-12-06 19:33 UTC

    Glad it helped! FWIW, I've been installing all of the updates and am now on Sequoia, still with no issues. Cheers.

  ---
  **JulioCesarSalad** | Score: 1 | 2024-12-13 04:11 UTC

  Just tried this on my M1 Pro, but recovery mode is only offering to reinstall Sonoma (computer was on sequoia before this)
  
  Do you know how I can force it into reloading the original OS?

    ---
    **unitegondwanaland** | Score: 1 | 2024-12-13 04:21 UTC

    My steps only were tested on a MacBook that originally shipped with Catalina because Catalina was the last OS that didn't require Internet connectivity to install.

      ---
      **JulioCesarSalad** | Score: 1 | 2024-12-13 04:51 UTC

      Ah, since your opening paragraph only says “shipped with an earlier release” I thought a Monterrey-original would have been fine

  ---
  **mo_roboh** | Score: 1 | 2025-02-05 19:34 UTC

  Worked in 2025 ty

    ---
    **unitegondwanaland** | Score: 1 | 2025-02-05 19:46 UTC

    w00000t!

  ---
  **lilylikesfood** | Score: 1 | 2025-03-18 15:27 UTC

  Hi! 
  I’m so stressed now bcz my laptop is locked…
  So if we do this, would the data be erased? I haven’t had any backup… plz help… thank you….

  ---
  **Affectionate-Ad2269** | Score: 1 | 2025-04-22 09:05 UTC

  i have a macbook 2020 running big sur with the remote management lock. i want to update to sequoia. will your steps work for this?

    ---
    **unitegondwanaland** | Score: 1 | 2025-04-22 20:41 UTC

    I don't know. I can only guarantee that it works with the scenario that I mentioned (from Sonoma and probably earlier). That was the last OS known to allow updates without wi-fi.

  ---
  **Reasonable-Log-7811** | Score: 1 | 2025-07-17 23:13 UTC

  the entire process listed here functions for me in Monterey, but i get an error 66 denied when trying `sudo mount -uw /`
  
  Can someone walk me through what this function is doing?

  ---
  **LightWeightSniper** | Score: 1 | 2025-08-08 00:41 UTC

  Any update for sequoia?

    ---
    **unitegondwanaland** | Score: 2 | 2025-08-08 00:46 UTC

    Sorry. The only solution I have is the one I posted.

      ---
      **LightWeightSniper** | Score: 1 | 2025-08-08 15:19 UTC

      I just installed sonoma on my 2019 16 inch MBP. imma keep you posted after i try this

      ---
      **LightWeightSniper** | Score: 1 | 2025-08-08 15:31 UTC

      Can we change the serial number of Mac using opencore or any other software?

    ---
    **starstar2023** | Score: 2 | 2026-02-05 22:11 UTC

    Did you find a solution?

      ---
      **LightWeightSniper** | Score: 1 | 2026-02-05 22:12 UTC

      I haven’t but i think you can use OPLC and regenerate the serial number or spoof the MacBook to another model

        ---
        **starstar2023** | Score: 1 | 2026-02-05 23:01 UTC

        Did you get stuck on the remote management enroll window and can't get pass it during setup?

          ---
          **LightWeightSniper** | Score: 1 | 2026-02-05 23:02 UTC

          Reset it again and don’t connect to internet.  Make sure you use macos ventura for that.  It didn’t cause any problems there for me

            ---
            **starstar2023** | Score: 1 | 2026-02-05 23:18 UTC

            My mistake was that I updated to sequioa then I start it getting the remote management window. Computer was working for 4 years just fine.  I the erase and reinstall it but it only gave me install os sequioa. Then I did it again comand + R then I erase and installed everything again without internet by not connecting to wifi. Then I did it a 3rd time by disconnecting router when the computer start it but now Im stuck in the window to enroll doesnt give an option to cancel or ignore. How do I go back to ventura? I didnt make a start up disk.

              ---
              **LightWeightSniper** | Score: 1 | 2026-02-05 23:24 UTC

              If you got access to another mac. Good. Or else i would say go and download the old macos from internet recovery and manually update to big sur or smth by downloading the image from safari directly. Then using OPLC try regenerating the serial number (I’ve tried the spoofing option, it worked for my 2016 15inch to spoof to 2019 15). I’ve tried that s/n option myself tbh. Then it might bypass it.  I guess.

                ---
                **starstar2023** | Score: 1 | 2026-02-05 23:31 UTC

                Thank you. Yes I have another computer that has battery issues and is running on macos Monterey. How long does it take to make a bootable usb installer and will Monterey work? Thank you for your help and  been trying for 2 days now.

                  ---
                  **LightWeightSniper** | Score: 1 | 2026-02-05 23:32 UTC

                  Anything above bigsur will be fine from OPLC.   And don’t thank me yet :)

  ---
  **EfficientMasturbater** | Score: 1 | 2026-03-11 13:42 UTC

  Hey man! You may have upgraded your hardware by now but just wondering about any luck you've had upgrading the OS if you have? I followed your instructions well over a year ago and was so thankful for you writing this out. Getting a tonne of apps being deprecated though now lol

    ---
    **unitegondwanaland** | Score: 1 | 2026-03-13 23:41 UTC

    Still on the same MacBook Pro and currently still doing upgrades without issues. Currently on Tahoe 26.3.1

  ---
  **Pen-Salty** | Score: 1 | 2023-11-13 09:35 UTC

  I was follow g this guide but when I did sudo profiles show -type enrolment it popped back up, how can I remove that??

    ---
    **unitegondwanaland** | Score: 1 | 2023-11-13 10:49 UTC

    Steps 14-16 should handle that. If you've wiped your disk from the beginning, that should be no problem. If not, I am not certain of the issue but stops 14-16 are supposed to handle the notifications.

  ---
  **Pen-Salty** | Score: 1 | 2023-11-15 08:55 UTC

  After completing all steps and receiving positive results after logging into iCloud I double checked the last 2 commands and on the second one I reconnected to the school :(

    ---
    **unitegondwanaland** | Score: 3 | 2023-11-15 10:58 UTC

    Interesting. I'm still clean but I also installed Sonoma offline and I didn't think that mattered at this stage but maybe it still does. Were you online when you did the Sonoma install after you restored with your original shipped OS?
    
    I've since updated my instructions to require the Sonoma install offline as it seems it is likely trying to configure MDM again.

  ---
  **Camp_1993** | Score: 1 | 2023-12-13 20:42 UTC

  hello! would you happen to know why I am getting "Volume could not be mounted:Permission Denied" after typing the first line "sudo mount -uw /"

    ---
    **unitegondwanaland** | Score: 1 | 2023-12-13 21:01 UTC

    csrutil is enabled?

      ---
      **Camp_1993** | Score: 1 | 2023-12-13 21:03 UTC

      It says I disabled it but I’ll check again. When I exit terminal I can just exit it right? Or is there a “proper” way to exit so the changes are saved. Sorry, new to Mac

        ---
        **unitegondwanaland** | Score: 1 | 2023-12-13 21:10 UTC

        Yup, you can close the window, no issues. csrutil being enabled is the only reason I can think of why that wouldn't work or you didn't use sudo.

          ---
          **Camp_1993** | Score: 2 | 2023-12-13 23:01 UTC

          yeah I keep getting the error " mount\_apfs: volume could not be mounted: permission denied" then on the next line it reads "mount: / failed with 66"
          
          any clue?

            ---
            **SteakMinimum5956** | Score: 1 | 2024-03-10 12:40 UTC

            How to got this resolved? I am stuck at this as well!

  ---
  **Camp_1993** | Score: 1 | 2023-12-14 03:24 UTC

  Hello I was finally able to get it done! Thank you. Last question. When you say you were able to install the latest two updates on Sonoma. Did you do those through the software updates available? Or did you use a usb for those as well?

    ---
    **unitegondwanaland** | Score: 2 | 2023-12-14 03:28 UTC

    I removed the hosts entry blocking updates and checked for updates from System > General. I stayed on WiFi the whole time, no issues. You may still want to do periodic time machine backups though.

  ---
  **vardelda** | Score: 1 | 2023-12-20 14:41 UTC

  >Sonoma
  
  u/unitegondwanaland  "...AND your computer shipped with an earlier release".  How does this change things?  Mine shipped with Sonoma and I have not yet successfully made it through.

    ---
    **unitegondwanaland** | Score: 2 | 2023-12-20 14:44 UTC

    Because you can get past this issue if you start with an earlier release that doesn't require Internet to install. Sonoma was the first release AFAIK that requires an internet connection and it cannot be bypassed.

  ---
  **Drop-Adept** | Score: 1 | 2024-02-28 03:37 UTC

  i’m trying to do this but I don’t understand some parts 😭😭any chance you’ll make a tutorial video?

---
**bobani214** | Score: 3 | 2022-12-03 18:21 UTC

Hey man, thanks for helping me! I did this once, but recently formatted and forgot the process. 

I know how to block the remote management notifications! Please do not be alarmed if you don’t know how to use the terminal. Please type the following once you load up terminal. 

First type the following to ensure that your laptop is being remote managed. It will display information as to which company the laptop belongs to. 

~ sudo profiles show -type enrollment

If information about the company pops up, proceed to the next step.

Close your terminal and open it up again. Type the following. Please do not include the “~” symbol.

~ cd .. 
~ cd .. 
~ cd etc 
~ sudo echo “0.0.0.0 i profiles.apple.com”

This will prevent any remote management notifications from being sent to your laptop. If you try running the first command above ^^ youll notice that it will no longer show information in regards to the company. I hope this helps :)

  ---
  **Scutched** | Score: 1 | 2022-12-15 14:26 UTC

  I'll give it a try. Thanks for checking back in with this info.
  
  It's a much smaller set of commands, if it works.

  ---
  **Scutched** | Score: 1 | 2022-12-15 14:38 UTC

  Are these commands you type in after you've installed the operating system and booted to the desktop? Or are you using the terminal commands before you even install the operating system?

  ---
  **Scutched** | Score: 1 | 2022-12-19 21:17 UTC

  >\~ sudo profiles show -type enrollment
  
  When I typed this 
  
  \~ sudo profiles show -type enrollment 
  
  I got "permission denied."

    ---
    **morphiaz** | Score: 1 | 2022-12-20 17:14 UTC

    >sudo profiles show -type enrollment
    
    You have to type:
    
    `sudo profiles show -type enrollment`  
    
    
    Without the til.

      ---
      **Scutched** | Score: 1 | 2022-12-24 19:15 UTC

      >sudo profiles show -type enrollment
      
      I typed without the waving line and saw the owner sending the annoying things and the popup popped up in the upper right hand corner. Then I closed the terminal. Then I reopened the terminal and typed:  
      
      
      cd (which did nothing other than a hard break after hitting ENTER)  
      cd (which did nothing other than a hard break after hitting ENTER)  
      cd etc (which did nothing other than a hard break after hitting ENTER)  
      
      
      Then I copied sudo echo “0.0.0.0 i [profiles.apple.com](https://profiles.apple.com)” from your post and pasted that into the terminal and hit ENTER. It asked for my password. After I typed it and hit enter this popped up: “0.0.0.0 i [profiles.apple.com](https://profiles.apple.com)”  
      
      
      Then I closed an reopened the terminal and copied and pasted   
      sudo profiles show -type enrollment  
      
      
      It showed the owner and the popped up in the upper right corner indicating that nothing changed.  
      
      
      What did I mistype or do wrong from your directions?  
      Thanks

        ---
        **last_minute_life** | Score: 1 | 2023-02-04 13:43 UTC

        You mistyped the 0.0.0.0 line. It's iprofiles.apple.com not i profiles.apple.com

          ---
          **Scutched** | Score: 1 | 2023-02-05 04:54 UTC

          >sudo profiles show -type enrollment
          
          Ok I typed exactly this:sudo echo “0.0.0.0 [iprofiles.apple.com](https://iprofiles.apple.com)”
          
          But when I do the enrollment test the Device Enrollment box still pops up in the upper right hand corner.
          
          I am unclear about typing cd because I am not sure what the two dots are afterwards. Should I be typing:cd ..and then enter? I have tried it all the different ways. I have tried with the dots and without. I am assuming I should be typing the cds, then a space, then two dots and then hitting the ENTER key. Like this:  
          cd .. ENTER.     
          cd .. ENTER.     
          cd etc ENTER.    
          sudo echo “0.0.0.0 [iprofiles.apple.com](https://iprofiles.apple.com)” ENTER
          
          It asks for my password and takes the command, but then still shows the company Device Enrollment when I test it.Can you think of anything else to try? Are you in Catalina?Do I need to be opening the terminal any special way? With nothing else opened for instance? Does that make a difference? Do I need to boot to recovery to run it?I am the only user account and the administrator.

            ---
            **Scutched** | Score: 1 | 2023-02-05 05:07 UTC

            Sorry, I am losing track of who I should be responding to. I appreciate the help from others who are not bobani214, but have you who have responded successfully got the Device Enrollment box in the upper right hand corner to go away, or are you just checking my following of the directions? (which is appreciated.)  
            Has anyone followed bobani214 directions and they worked for you?

            ---
            **last_minute_life** | Score: 1 | 2023-02-05 13:00 UTC

            The "cd" comand means "change directory".
            The .. means the one above. 
            
            When you open the terminal, you are in /users/<yourname> (or something like that) and you want to get to /etc, so you are changing directory: up, up, then down into etc.
            
            You can skip all the "cd .." commands with just "cd /etc"

              ---
              **Scutched** | Score: 1 | 2023-02-13 20:38 UTC

              Thanks, I did All that stuff And could not get the device enrollment to go away. Since those commands gave me the information on the school who had control of the laptop I decided to email them. They were kind enough to just remove the device management for me.

                ---
                **last_minute_life** | Score: 1 | 2023-02-13 21:32 UTC

                That's probably the best solution :)

                ---
                **[deleted]** | Score: 1 | 2023-08-16 20:34 UTC

                Thanks for the suggestion! I called the Service Desk at my old company on the sticker on my laptop, and they created a ticket for me and are having their team remotely remove Remote Management. Whew, problem solved.

                  ---
                  **Scutched** | Score: 1 | 2023-08-16 23:53 UTC

                  Great. Yeah, they are probably rarely stolen. Just sold with disabling the Remote Management stuff.

  ---
  **Scutched** | Score: 1 | 2023-02-05 05:02 UTC

  Ok I typed exactly this:   
  sudo echo “0.0.0.0 iprofiles.apple.com”  
  But when I do the enrollment test the Device Enrollment box still pops up in the upper right hand corner.  
  I am unclear about typing cd because I am not sure what the two dots are afterwards. Should I be typing:cd ..and then enter? I have tried it all the different ways. I have tried with the dots and without. I am assuming I should be typing the cds, then a space, then two dots and then hitting the ENTER key. Like this:  
  cd .. ENTER.  
  cd .. ENTER.  
  cd etc ENTER.  
  sudo echo “0.0.0.0 iprofiles.apple.com” ENTER  
  It asks for my password and takes the command, but then still shows the company Device Enrollment when I test it.Can you think of anything else to try? Are you in Catalina?Do I need to be opening the terminal any special way? With nothing else opened for instance? Does that make a difference? Do I need to boot to recovery to run it?I am the only user account and the administrator.

    ---
    **umeshrav** | Score: 1 | 2023-02-10 13:53 UTC

    >echo “0.0.0.0 iprofiles.apple.com”
    
    echo will just prints a message in console. Not sure what this command will do other than just printing the message.

---
**kabobinator** | Score: 3 | 2022-09-22 05:35 UTC

Hi everyone, I was troubleshooting this issue and was actually able to bypass it by 1) Turning off my modem like everyone suggested, and 2) Holding Command + S (Single User Mode) when booting up.

I had been stuck on the screen with Remote Management requiring me to log in. It was remembering my old wifi just like OP mentioned, and even after I turned off the modem, it was still opening a log-in page (which would freeze, since no internet connection.)

If anyone else is having this problem, try rebooting your computer and hold Command+S while it boots. I have even restarted my computer since and it works great.

  ---
  **sieffy** | Score: 3 | 2022-10-06 16:12 UTC

  What version of Mac OS I’m on Big Sur and people are saying this method won’t work for anything that’s newer than catalina

    ---
    **Interesting-Egg306** | Score: 3 | 2022-10-07 04:05 UTC

    I'm trying to figure this out too on a client's MacBook Pro running Monterey. Haven't found a solution yet.

      ---
      **Kakatua2012** | Score: 7 | 2022-10-09 00:55 UTC

      Hi,
      
      I found this in another blog, i tried it with Big Sur, upgraded to Monterey and no issues.
      
      It worked perfectly
      
      	1	Boot to Recovery Mode by holding Command-R during restart  
      	2	Open Tools → Terminal and type  
      $ csrutil disable  
      	3	Restart computer and hold Command-R to enter Recovery Mode again  
      	4	Enter Disk Utility, and mount the Macintosh HD volume (or whatever your main volume is named)  
      	5	Exit Disk Utility, open the Terminal, and type  
      $ mount -uw "/Volumes/Macintosh HD/System/Library"  
      $ cd "/Volumes/Macintosh HD/System/Library"  
      $ mkdir LaunchDaemons.disabled LaunchAgents.disabled  
      $ mv LaunchDaemons/com.apple.ManagedClient\* LaunchDaemons.disabled/  
      $ mv LaunchAgents/com.apple.ManagedClient\* LaunchAgents.disabled/  
      $ cd ../../etc  
      $ echo "0.0.0.0 albert.apple.com" >> hosts  
      $ echo "0.0.0.0 iprofiles.apple.com" >> hosts  
      $ echo "0.0.0.0 mdmenrollment.apple.com" >> hosts  
      $ echo "0.0.0.0 deviceenrollment.apple.com" >> hosts  
      $ echo "0.0.0.0 gdmf.apple.com" >> hosts  
      $ csrutil enable

        ---
        **JumpySundae3670** | Score: 2 | 2022-12-12 22:43 UTC

        Thanks for this, I will give this a go! 😊

          ---
          **Ahmoody12** | Score: 2 | 2022-12-17 20:41 UTC

          did it work?

            ---
            **Fancy_Enthusiasm3810** | Score: 3 | 2023-03-25 23:53 UTC

            For me, it did not work on Bigsur, but it worked on Mojave. 
            
            I am upgrading from Mojave to Bigsur now.  See how it goes

              ---
              **h_b11** | Score: 3 | 2023-09-18 19:28 UTC

              how did you upgraded? I am on Ventura 13.0.1 and when checking for the update I get the info that my system is up to date.
              
              EDIT: it's possible to find it in an appstore and install from there

        ---
        **pausesir** | Score: 1 | 2024-12-09 23:09 UTC

        This works! But are we not able to do software updates through the apple menu even if we didn’t block the update server?

        ---
        **[deleted]** | Score: 1 | 2025-01-15 16:26 UTC

        Doing this will I be able to use iCloud and other apple services?

          ---
          **Popswavey** | Score: 1 | 2025-02-08 02:10 UTC

          Do you have any idea hot to do same on new iOS software

        ---
        **jack_attack96** | Score: 1 | 2024-02-13 04:17 UTC

        For me it says "hosts: Read-only file system"

  ---
  **Excellent_Hold_117** | Score: 2 | 2024-02-24 17:29 UTC

  This worked. Keep getting the RDM pop up though...Is there a way to make those stop?

  ---
  **Chicken-Dior** | Score: 1 | 2023-10-15 03:46 UTC

  This worked fuck yeah! 2019 MBP Remote MGM with Amazon. Picked it up from my local thrift store, guess someone forgot to send it back.

---
**kickintheeye1** | Score: 2 | 2021-12-15 19:10 UTC

If you replace the hard drive will it get rid of RM?

  ---
  **Scutched** | Score: 5 | 2021-12-15 19:16 UTC

  It will not. It is linked to the motherboard.

    ---
    **GSXMafia** | Score: 3 | 2022-01-15 22:22 UTC

    Did you get this solved? 
    
    Mdm is paired to the nand and serial.

    ---
    **alphabeats23** | Score: 3 | 2022-04-29 02:06 UTC

    so if i replace the motherboard will i get rid of RM and all of these stuff? and if replace motherboard should i replace ssd too ?

      ---
      **Scutched** | Score: 6 | 2022-04-29 03:25 UTC

      No the SSD does not need replacement. I can't confirm replacing the motherboard will fix the problem. My guess is yes it will.

        ---
        **alphabeats23** | Score: 2 | 2022-04-30 00:09 UTC

        thx bro.

          ---
          **Spr3122** | Score: 2 | 2022-06-02 15:29 UTC

          Did it worked? When you changed motherboard?

            ---
            **alphabeats23** | Score: 2 | 2022-06-02 15:33 UTC

            i did not changed it. i will but idk when

              ---
              **ImpressiveStudy1833** | Score: 2 | 2022-06-21 09:01 UTC

              Have you replaced the motherboard yet??

---
**[deleted]** | Score: 2 | 2022-03-10 11:33 UTC

[removed]

  ---
  **meepz** | Score: 2 | 2022-04-06 09:22 UTC

  I've seeen this tool before but there isn't any information as to what the tool is actually doing? Do you know what the tool specifically does to remove the MDM?

  ---
  **firsmode** | Score: 1 | 2022-09-09 02:35 UTC

  Is this legit?

---
**tonyle3k** | Score: 2 | 2022-03-17 00:14 UTC

anyone got this working for Monterey?

  ---
  **ABGinTech** | Score: 4 | 2022-06-20 05:14 UTC

  Have you found a working solution for Monterey?

    ---
    **Kalinucs** | Score: 1 | 2023-09-02 09:45 UTC

    any wins with Monterey?

      ---
      **ABGinTech** | Score: 2 | 2023-09-04 08:18 UTC

      Nope. Apple got that shit locked down. It’s still sitting in my room bricked

        ---
        **Kalinucs** | Score: 1 | 2023-09-04 08:23 UTC

        yeah... i managed to "unlock" it but I still get those notifications daily for that remote management

          ---
          **ABGinTech** | Score: 1 | 2023-09-04 08:25 UTC

          oh just notifications? How did you get past the initial login wall?

            ---
            **Kalinucs** | Score: 2 | 2023-09-04 08:34 UTC

            I have M1 pro MacBook and when I reinstalled Ventura from the recovery boot i waited for it to install and all (connected to my wifi router) and when the installation of Ventura is done and the Apple logo appears I unplugged the router so I do not have access to the internet when it boots. After that i just follow the setup process and ehem prompted to connect to a wifi I choose other and check "I don't have internet acces" pe smth like that. And it just bypasses and only after I get to the desktop screen and all setup is done I turn the wifi on.

              ---
              **ABGinTech** | Score: 1 | 2023-09-04 09:44 UTC

              How annoying is the daily notification? Is it just one click disappear?

                ---
                **Kalinucs** | Score: 2 | 2023-09-04 10:04 UTC

                yeah it's just a normal notification appearing in the top right corner, you can simply close it

                  ---
                  **ABGinTech** | Score: 1 | 2023-09-04 20:20 UTC

                  That doesn’t seem that bad. I will try your walkthrough again to see if I can bypass it

        ---
        **Repulsive-Ad-3890** | Score: 1 | 2023-11-07 08:03 UTC

        Hey 👋 did you get this issue resolved?

          ---
          **AStrangeGoose** | Score: 2 | 2024-04-10 02:51 UTC

          [https://williamhartz.medium.com/how-to-remove-remote-management-screen-from-macbook-without-password-2023-486ac1476acc](https://williamhartz.medium.com/how-to-remove-remote-management-screen-from-macbook-without-password-2023-486ac1476acc)
          
          I tried this on a used MacBook Air that I bought, and it seems to work well. No notifications or anything. If you haven't already found a different solution, it might work for you.

            ---
            **Repulsive-Ad-3890** | Score: 1 | 2024-04-10 07:55 UTC

            Thank you for replying.

            ---
            **Individual_Theme_527** | Score: 1 | 2025-08-13 10:16 UTC

            It worked perfectly but you have to follow all the steps, the most essential one is blocking the MDM Server

          ---
          **ABGinTech** | Score: 1 | 2023-11-07 09:28 UTC

          No. It’s still in the corner of my room bricked. Did you figure out how to bypass?

            ---
            **Repulsive-Ad-3890** | Score: 1 | 2023-11-07 09:33 UTC

            No, I bought it as a sealed new computer and it’s not what I expected. I have contacted the company and I hope they can help me resolve this.

---
**Realistic-Frame-4162** | Score: 2 | 2022-04-26 07:53 UTC

I got high sierra and literally turned modem off while on last loading screen when logo comes on and it worked. Only been cpl hours but haven’t got any notifications either

  ---
  **wanyewayne** | Score: 5 | 2022-04-26 14:29 UTC

  FYI - I just found a way that doesn't require turning off the modem. When the   
  internet options coup there's an 'other   
  k settings' button. When I clicked it there were three options and  
   I chose the option "My computer does not connect to the internet". This  
   bypassed the managed settings and I'm up and running after a reinstall.  
   After restarting, no managed setting message came up. Macbook pro 2017   
  running High Sierra 10.13.6

    ---
    **markbennett90** | Score: 2 | 2022-04-28 07:17 UTC

    have you tried for monterey? or only high sierra?

    ---
    **quwerty77** | Score: 1 | 2022-10-23 23:29 UTC

    Did this work long term? Are you able to upgrade?

  ---
  **quwerty77** | Score: 1 | 2022-10-23 23:29 UTC

  Did this work long term?

    ---
    **Realistic-Frame-4162** | Score: 1 | 2023-02-23 07:25 UTC

    Yes. Lol sorry for late reply. I didn’t even kno I made this post. But yes it worked. Used as a business comp n sold cpl years later. No problems

---
**No_Celery931** | Score: 2 | 2022-10-15 16:00 UTC

The fix is: you have to turn off your wifi from your modem so there is no way the laptop can connect to the old network, or any previously saved network. Turn off the modem if you have to. That works like a charm. Then don't connect to any wifi during the setup and you are fine.  
This was on a 2012 Macbook pro after I did a clean install of Catalina.

&#x200B;

This solution works with my Macbook pro 16 2019 with macOS Monterey

  ---
  **AgreeableAd5043** | Score: 2 | 2023-03-06 00:55 UTC

  Thanks this works for me

  ---
  **Far-Lab5085** | Score: 1 | 2023-02-10 23:39 UTC

  So when exactly do you turn off the modem ? Since I’m using an internet recovery ?

    ---
    **Eggsactly123** | Score: 1 | 2023-07-16 13:57 UTC

    After the os downloads, the Mac will restart. Turn off modem as soon as it does, and follow above directions about connecting without Internet

---
**just1ed** | Score: 2 | 2022-12-03 11:19 UTC

I am unable to bypass Remote Management by turning off the wifi, the modem, or by selecting no internet option during setup.   


What worked for me was to turn off the internet immediately after the Mac restarts during installation.

It works for Big Sur. I am at least able to install and use MacOS. I am not sure if the Device Enrollment prompt would appear or not.

  ---
  **Scutched** | Score: 1 | 2022-12-03 19:44 UTC

  Let us know if you are getting upper right hand popups daily in Big Sur after you use it for a few days.
  
  Yes, turning off the computer, then turning off your router is the most sure way of blocking internet. Then turn the computer back on with internet router off.

    ---
    **alex311es** | Score: 1 | 2023-02-18 10:05 UTC

    It worked for on big sure, 18/02/2023

      ---
      **Haunting_Page4609** | Score: 1 | 2024-03-28 15:33 UTC

      Hi! is still okay? or worked out?

        ---
        **Haunting_Page4609** | Score: 1 | 2024-03-28 15:35 UTC

        u/alex311es Does the Device Enrollment prompt still appear?

          ---
          **alex311es** | Score: 1 | 2024-06-04 11:28 UTC

          Nope

  ---
  **JuanS237** | Score: 1 | 2023-03-04 22:18 UTC

  Hi! I’m trying to bypass the remote management with a fresh install of Big Sur. How you did it to solve the problem?

    ---
    **Fancy_Enthusiasm3810** | Score: 1 | 2023-03-25 08:06 UTC

    I tried on Bigsur a number times and all failed.
    
    However I downgraded it to Mojave (Apple did - dunno why and how - I may damage the startup disk too many times, Apple suddently started installing Mojave) . and then the methond above worked.

---
**Necessary_Age4828** | Score: 2 | 2023-04-15 14:52 UTC

Thank you so much for writing this! Saved my ass today!

I was afraid it was actually "Game over" for me and the laptop. Apprently it was bought for one company registered in Apple, and later passed over to another company and it demanded for me to configure Remote Management with no other option, even thought he server wasnt reachable and probably will never be, since we dont have access to internal network of the past company. Dont ask me why their mdm was configured only for internal network.

---
**thenewquestions** | Score: 2 | 2023-12-26 03:05 UTC

Posting because this was the top hit in google search. I had a Macbook air early 2020 model with the intel i3 chip and Ventura Os that I purchased second hand on FB marketplace. Upon getting home, I went through the setup without paying much attention to it assuming it would all work fine.  


I loaded my wifi info, and then clicked "ok" when it notified me that the laptop was owned by "such and such school district" not really knowing what It meant. It then installed a bunch of remote management stuff and finally ended up at a login screen, waiting for a username and password that I didnt have.  


I went on a google-thon trying to fix the issue. There is so much useless info on this topic its unbelievable. What finally ended up working for me was CONTACTING the person I bought the macbook from. They worked at the school district that "owned" the mac. They missed disabling this one before reselling. 

&#x200B;

After I confirmed that they removed the device from their system, I used the recovery assistant (boot mac, hold command + R key), opened Disk Utility and erased the Macintosh HD (not base os data). After erasing it, I was able to reinstall Ventura from the option within the recovery assistant. Once the setup was complete, I re-entered my WIFI info, and the mac recognized that the mac was "released" from ownership and I was able to load my apple ID in as one would expect. No issues from that point.  


If I wasnt so lucky in being able to contact the owner, my next step would be to install Monteray Os from a bootable drive, and do the installation with WIFI modem OFF. Select "this computer does not use the internet" under "other network options" when it asks for your wifi info during initial setup. This should bypass the ownership deal. Its not possible to do this "turn off the wifi" trick with Ventura. It needs a network connection.   


Good luck!

---
**bimodaltuna** | Score: 2 | 2024-02-23 09:31 UTC

For everyone who came far and got the access to the MB but cannot make the notifications stop: 

Found this on a thread online, worked like a charm for me(MBP 2019)

"Editing the hosts file appears to have worked all by itself. There's no need to reboot into Recovery Mode, disable SIP or FileVault, or move/disable the plists controlling the daemons related to device enrollment and management. You can edit the hosts file in Terminal while logged in normally, although not using those "echo" commands (even typing 'sudo echo "0.0.0.0 albert.apple.com" >> hosts' gave the error 'permission denied: hosts'). I googled editing the hosts file, and the trick appears to be to use the nano editor:

Type in terminal: sudo nano /private/etc/hosts. Enter admin password when prompted.

Use Arrow key on your keyboard to move the cursor to the last line and type the following lines:

0.0.0.0 iprofiles.apple.com
0.0.0.0 mdmenrollment.apple.com
0.0.0.0 deviceenrollment.apple.com

Press Control + X from keyboard to Exit.

Now you will be asked to asked whether you want to save and to enter Y for yes and N for No. Type Y [be sure to do this!]

Check to see whether the enrollment calls are being blocked by typing 'sudo profiles show -type enrollment'

You should see an error like this:

(34000) Error Domain=MCCloudConfigurationErrorDomain Code=34000 "The device failed to request configuration from the cloud." UserInfo={NSLocalizedDescription=The device failed to request configuration from the cloud., CloudConfigurationErrorType=CloudConfigurationFatalError}

That should be all there is to it! Many thanks to all those on gist.github.com who proposed various solutions."

-Odysseus the goat(found the goat's comment on apple.stackexchange)

  ---
  **wallyj2k** | Score: 1 | 2024-03-10 21:41 UTC

  In my case, I was already at the Remote Management screen that will not let me do anything on my Macbook except click "Enroll", so I booted into Recovery Mode to get to a terminal, made the additions to the hosts file that you listed and thought it would work. When I rebooted, it popped up the Remote Management screen again with 15 seconds of me typing in my password. Again, I thought this would work, but it doesn't seem to in my case.

  ---
  **Necessary-Listen8433** | Score: 1 | 2024-07-30 15:59 UTC

  I just wanted to thank you for this post.  It helped along with many of the others in this thread.  I'll share my story.
  
    
  Mac Air 2018 Retina that I received new from my company.  I have been using it for six years.  Early 2020 my Touch ID stopped working so I took it to an Apple Store for repair.  They replaced the motherboard.  All was good.  
  
    
  I used it for another four years without issue.   Recently I received an updated M3 Mac Air.   I decided to do a clean install of Sonoma on the 2018 model.   I was presented at boot up with the Remote Management login advising the Laptop was owned by Amazon.  I was stuck.   I chatted to Amazon Support vial the link presented but she could not assist and said the unit was too old so they had no details.   
  
  I then researched the issue and found this thread and another that helped. 
  
    
  Step 1.  Delete the Volume and install the original Operating system.   Mojave. 
  
  Step 2.  After downloading and at first boot up I turned off my router and select the option that this PC is not used on the internet.   That worked and the install completed. 
  
  Step 3.  I updated to Ventura, then to Sonoma.
  
  So far so good. 
  
  Yesterday I received the pop up notification for Remote Management.   I used the advise suggested here (and I will paste below for reference. 
  
    
  Voila - Laptop has a clean install and no more Remote Management Pop Ups. 
  
  I did the below to remove the pop ups. 
  
  "Editing the hosts file appears to have worked all by itself. There's no need to reboot into Recovery Mode, disable SIP or FileVault, or move/disable the plists controlling the daemons related to device enrollment and management. You can edit the hosts file in Terminal while logged in normally, although not using those "echo" commands (even typing 'sudo echo "0.0.0.0 albert.apple.com" >> hosts' gave the error 'permission denied: hosts'). I googled editing the hosts file, and the trick appears to be to use the nano editor:
  
  
  
  Type in terminal: sudo nano /private/etc/hosts. Enter admin password when prompted.
  
  
  
  Use Arrow key on your keyboard to move the cursor to the last line and type the following lines:
  
  
  
  0.0.0.0 iprofiles.apple.com 0.0.0.0 mdmenrollment.apple.com 0.0.0.0 deviceenrollment.apple.com
  
  
  
  Press Control + X from keyboard to Exit.
  
  
  
  Now you will be asked to asked whether you want to save and to enter Y for yes and N for No. Type Y \[be sure to do this!\]
  
  
  
  Check to see whether the enrollment calls are being blocked by typing 'sudo profiles show -type enrollment'
  
  
  
  You should see an error like this:
  
  
  
  (34000) Error Domain=MCCloudConfigurationErrorDomain Code=34000 "The device failed to request configuration from the cloud." UserInfo={NSLocalizedDescription=The device failed to request configuration from the cloud., CloudConfigurationErrorType=CloudConfigurationFatalError}

    ---
    **Jackpott100** | Score: 1 | 2024-11-23 03:15 UTC

    I know it's been a few months since you posted this. Currently, I have a 2019 on Monterey that works without issue with this host file edit. I was wondering if it still holds true with Ventura? Or had you not tried this and just went straight to Sonoma? It seems as though it works on Sonoma, from what you've posted, but not Sequoia, the newest OS, of course. I honestly would be fine keeping it at Monterey, but there is some software that is bugging me to upgrade to Ventura. I just didn't want to run into the remote management again. Thank you!

    ---
    **robert0192** | Score: 1 | 2025-02-24 09:40 UTC

    Sequoia OS here. This is the solution <3, thank you so much. After doing the file changes, go to Settings -> Profiles and remove any remote management profiles that you have there.

  ---
  **Necessary-Listen8433** | Score: 1 | 2024-07-30 16:05 UTC

  To load a fresh copy of the original operating system boot with holding Shift + Option + Command + R
  
  He covers it in the second half of this video. 
  
  [https://www.youtube.com/watch?v=n7V\_op5sUZw](https://www.youtube.com/watch?v=n7V_op5sUZw)

  ---
  **biwuchen** | Score: 1 | 2024-12-05 19:47 UTC

  This is the simplest working solution all over Internet! Works on Sequoia! Award sent.

    ---
    **bimodaltuna** | Score: 1 | 2024-12-05 19:48 UTC

    Glad to help :)

      ---
      **biwuchen** | Score: 1 | 2024-12-05 19:54 UTC

      🙏

  ---
  **Chentemu5** | Score: 1 | 2025-04-03 17:56 UTC

  Best and easiest solution. Works on the newest OS Sequoia. Much appreciated for sharing this!

---
**[deleted]** | Score: 2 | 2024-03-12 06:40 UTC

Any way to make this work on Sonoma? 14.3.1? The very first screen is "Activate Mac" which requires internet.

---
**Lorinloewe4444** | Score: 1 | 2024-04-08 14:49 UTC

Worked like a charm thanks

---
**Objective-Pea-4569** | Score: 1 | 2024-04-24 17:17 UTC

The MDM finally took over my device. I can’t get past it. I can’t click on anything. I can’t even shut my device down. It is totally frustrating.

---
**Remote-Link-6424** | Score: 1 | 2024-05-23 11:06 UTC

Companies should remove the Remote Management from their machines after they discard them. It's honestly annoying how many companies just sell laptops and Macs with the remote management enabled.

---
**No_Accountant8396** | Score: 1 | 2024-07-10 09:35 UTC

macbook pro keyboard weird symbols

---
**ManufacturerOk926** | Score: 1 | 2024-09-29 01:14 UTC

How do u do this from startup. My old laptop has the corporate managed login come up where u need to sign in. Im a former employee so obviously the username is no longer valid

  ---
  **Scutched** | Score: 1 | 2024-10-27 20:23 UTC

  You have to erase and format the hard drive and reinstall the operating system to get past that. On your first startup after the reinstall the directions on this post will become relevant.

---
**jeramyfromthefuture** | Score: 1 | 2024-11-09 23:10 UTC

https://apple.stackexchange.com/questions/297293/turning-off-device-enrollment-notifications-on-macbook-pro

---
**[deleted]** | Score: 1 | 2024-11-16 20:30 UTC

I am not able to go to boot mode using Cmd+R. 
Also first screen I am getting select your country or Region. 
What can be done in this case

---
**[deleted]** | Score: 1 | 2024-11-24 07:11 UTC

I’ll pay someone $100 Venmo per hour if they jump on a video call and walk me through this shit. This is as far as I’ve made it but I don’t want to mess anything up so I’m going hope someone here can help and get paid !

https://preview.redd.it/a4sws8dgus2e1.jpeg?width=4032&format=pjpg&auto=webp&s=aa2ba75499eeb1f1e897d4956e0869b9b41ac3f3

---
**ConsiderationMost817** | Score: 1 | 2024-12-04 21:36 UTC

Hey i just bought a MacBook off ebay with remote control and ive tried all of the network things but nothing has changed. Is their anything else i can do?

---
**[deleted]** | Score: 1 | 2024-12-28 15:15 UTC

I just erased to clear all content on my laptop and I keep running into the remote management part. I see y’all saying to disconnect the motem when it’s rebooting. I’m not really tech savvy . When is the rebooting part? When I’m on the rebooting screen and after erasing all content on my drive and I’m installing macOS, or when I’m restarting the laptop in general? When I do try to disconnect the internet it keeps saying I have to have an internet connection to move forward. My laptop is a MacBook 2017. Please, if any advice

  ---
  **Scutched** | Score: 1 | 2024-12-28 15:33 UTC

  I don't know whether you've done a proper reinstall of the operating system. If you think you have and it looks like you are starting a new Mac laptop for the first time, hold the start button down for 10 seconds so that you force the computer off. After it is off walk to your modem or modems, you may have two and unplug the power to them so the lights on the modems are black. Then turn your laptop back on and continue the setup where it asks what language you want and whether you want to install an extra keyboard etc, whether you want to use Siri, etc., it'll ask you to set up your username as well and password. Once you do all that and get to the desktop where there's a pretty picture of something, then you can plug your modems back in. 
  I can't guarantee that will work on a 2017, because this thread was only about my 2012 MacBook pro installing Catalina, but that is the procedure.
  
  If you haven't fully erased the laptop and downloaded a new operating system yet then you must keep the modem on to do that part. 
  
  Hope that helps.

---
**Bright-Addendum-1823** | Score: 1 | 2025-01-29 07:28 UTC

Yeah, Macs love holding onto old WiFi settings even after a wipe—cutting off WiFi at the source is definitely the move. For the 'Device Enrollment' nag, you can check **System Settings > Privacy & Security > Profiles** and see if there’s an MDM profile to remove. If it keeps coming back, it's likely tied to Apple's DEP, and you'd need the original admin to fully remove it.

---
**BGinger91** | Score: 1 | 2025-03-04 15:52 UTC

Can I do anything like this with the Monterey OS? Trying to get in but getting the login screen for the company. I have erased my disc But when I try to do anything it won’t let me proceed without Wi-Fi

  ---
  **Scutched** | Score: 1 | 2025-03-06 03:29 UTC

  I only did it on Catalina and then later emailed the school district and they removed the management nags.

---
**Ornery_Quail_9283** | Score: 1 | 2025-05-02 16:03 UTC

For those who are still wondering in 2025, this is how you can do it: (This is an alternative solution for some MacBooks with security settings not allowing Terminal to be used in recovery mode)

Step 1: Skip connecting to Wifi and complete the Setup by moving far away from your wifi setup.

Step 2: In Terminal, type in the following commands:   
echo "0.0.0.0 deviceenrollment.apple.com" >>/Volumes/Macintosh\\ HD/etc/hosts  
echo "0.0.0.0 mdmenrollment.apple.com" >>/Volumes/Macintosh\\ HD/etc/hosts  
echo "0.0.0.0 iprofiles.apple.com" >>/Volumes/Macintosh\\ HD/etc/hosts  
touch /Volumes/Data/private/var/db/.AppleSetupDone  
rm -rf /Volumes/Macintosh\\ HD/var/db/ConfigurationProfiles/Settings/.cloudConfigHasActivationRecord  
rm -rf /Volumes/Macintosh\\ HD/var/db/ConfigurationProfiles/Settings/.cloudConfigRecordFound  
touch /Volumes/Macintosh\\ HD/var/db/ConfigurationProfiles/Settings/.cloudConfigProfileInstalled  
touch /Volumes/Macintosh\\ HD/var/db/ConfigurationProfiles/Settings/.cloudConfigRecordNotFound  
sudo launchctl disable system/com.apple.ManagedClient.enroll

Step 3: Reboot the computer and run the following in Terminal to check if MDM:  
sudo profiles show -type enrollment

If the above command gives an error or says something like "Error fetching Device Enrollment configuration: We can't determine if this machine is DEP enabled.Tye again later." then you are good! I have tried updating macos, and MDM lock will not come back unless you reinstall macos.

  ---
  **Historical_Crazy_750** | Score: 1 | 2025-06-01 02:22 UTC

  Does this work on Monterey

    ---
    **Ornery_Quail_9283** | Score: 1 | 2025-06-01 03:17 UTC

    It should work

      ---
      **Ornery_Quail_9283** | Score: 1 | 2025-06-01 03:18 UTC

      Btw you would need to turn off SIP

      ---
      **Historical_Crazy_750** | Score: 1 | 2025-06-01 03:20 UTC

      I tried a different method but it worked! I’m now updating the OS to Sequoia, hopefully that goes smoothly without any issues, pls let me know if you have any suggestions for that! 
      
      Also before updating, I tried adding in my Apple ID, but once I submitted the multi authentication point, I got a “keychain not found” msg. Do you know how to bypass that? Thank you

        ---
        **Ornery_Quail_9283** | Score: 1 | 2025-06-01 11:03 UTC

        Not sure. That didn’t happen to me. Should update fine.

---
**SnooChickens4855** | Score: 1 | 2025-05-18 23:16 UTC

M

---
**Effective_Context339** | Score: 1 | 2025-06-20 17:28 UTC

Wow

---
**Cultural_Ad3963** | Score: 1 | 2025-07-16 15:34 UTC

hi all so i have a mdm locked macbook i was somehow able to install big sur onto it without an internet connection but now i dont know how to complete the process and skip mdm or even see if it is still locked??? cirrently i can log on the the desktop but i have not connected to wifi yet... any help?

---
**Kombat1978** | Score: 1 | 2025-08-20 09:13 UTC

So I had the same problem. However even when I went to another location with a different WiFi that was never used on MBP it still came up. My fix was technical, i opened the cover and plugged out the WiFi adapter. Logged in with new user and then shutdown and put the adapter back. 

All sunshine and roses.

---
**Nice_Ad_6721** | Score: 1 | 2025-08-22 19:44 UTC

hey guys quick question.

can I upgrade my MacBook MDM bypassed to newer macOS through OTA Software Update?

MacBook Pro 2021 M1 Pro 14 inch running macOS Sequoia 15.5 (24F74)

---
**yofroyolo** | Score: 1 | 2025-12-06 22:38 UTC

Can someone link a resource or explain simply how to use the terminal with all the coding? I don’t want to mess it up and it’d help to see a visual so I know how it’s supposed to be input.

Clearly not tech savvy and desperately trying to get into an inherited MacBook that has MDM from a now non-existent org.

---
**Potato_Kill3r** | Score: 1 | 2022-01-22 18:57 UTC

Hi bro, just want to ask u regarding this. I turned off my modem as well as did not connect to any wifi but still can’t continue the set up due to remote management thing. Can you kindly please help me?

  ---
  **Scutched** | Score: 2 | 2022-01-31 06:13 UTC

  This is only for Catalina. Beyond that OS, I have no advice. I can just tell you what worked for me. Make sure there are no other possible wifi networks that you might automatically be connecting to, like the free xfinitywifi that is everywhere.

  ---
  **wanyewayne** | Score: 1 | 2022-04-26 14:28 UTC

  I just found a way that doesn't require turning off the modem. When the   
  internet options come (don't choose a network) up there's an 'other   
  network settings' button. When I clicked it there were three options and  
   I chose the option "My computer does not connect to the internet". This  
   bypassed the managed settings and I'm up and running after a reinstall.  
   After restarting, no managed setting message came up. Macbook pro 2017   
  running High Sierra 10.13.6

    ---
    **ABGinTech** | Score: 1 | 2022-06-20 05:14 UTC

    Nope. This doesn’t work.

    ---
    **Comprehensive-Egg344** | Score: 1 | 2022-07-29 04:24 UTC

    Did as u said and it allowed me to log in with apple id.  Then it booted up
    
    Thanks

---
**Pa7adox** | Score: 1 | 2022-10-17 13:33 UTC

Hello, I did this and it worked, but can you then use an apple id to log in into the Mac? Also, can you restart the Mac without getting this remote management message? I havent had the guts to do it..

  ---
  **Scutched** | Score: 1 | 2022-10-26 02:41 UTC

  How you log into the Macbook is irrelevant Apple ID or not. So the answer is yes, you can. But it won't bypass the issue. Eventhough, I was able use the above directions to complete the setup and bypass the remote management message, I have been living with another remote management message that pops up in the upper right hand corner where notifications are. I get at least one similar remote management nag a day related to the one during setup. I just click it to close it, but I have not found a way to remove those. I am just living with it. I just don't wanna spend the 5 hours looking for a solution. There are ones out there, but they didn't work for me.

    ---
    **Pa7adox** | Score: 1 | 2022-10-26 05:38 UTC

    Hello, thanks, I have added my id and now is fine. I also think i have an answer for this issue with the pop-up. I never get it because I blocked a bunch of apple sites into checking my laptop. If you need help with this DM me.

      ---
      **starstar2023** | Score: 1 | 2026-02-05 22:21 UTC

      Did you remove your device from your  apple Id account before deleting and reinstall stalling os again?

        ---
        **Pa7adox** | Score: 1 | 2026-02-05 23:22 UTC

        I honestly don’t remember it was a while back

          ---
          **starstar2023** | Score: 1 | 2026-02-05 23:25 UTC

          Have you updated your computer since and had issues?

            ---
            **Pa7adox** | Score: 1 | 2026-02-05 23:42 UTC

            Updated it to latest os, no issues

---
**Nervous-Marsupial730** | Score: 1 | 2022-10-20 22:01 UTC

This tip worked a treat.

---
**Vegetable-View-2058** | Score: 1 | 2022-11-20 00:07 UTC

Still works like a charm as of nov2022

---
**deletedbyredditadmin** | Score: 1 | 2023-05-31 02:09 UTC

bless —you. 

This worked on my Ventura!

  ---
  **Exotic-Light-5332** | Score: 1 | 2023-07-01 11:33 UTC

  Would you mind telling me which method worked for Ventura? I have been trying to figure it out for days and I have Ventura. Thank you in advance!

    ---
    **deletedbyredditadmin** | Score: 1 | 2023-07-01 22:01 UTC

    It was this one upthread: https://www.reddit.com/r/mac/comments/pi9beh/bypass_remote_management_on_macbook_pro_after/henw31i/

---
**InUrEndTho** | Score: 1 | 2023-07-08 17:25 UTC

Just came here to say this dude is doing gods work! Been looking for this solution for months now, and this actually worked! Thank you my guy!! ♥️♥️♥️

---
**mediapoison** | Score: 1 | 2023-07-17 13:15 UTC

I just used this tip, Thanks for posting!

---
**snakeater9980** | Score: 1 | 2023-07-27 13:24 UTC

Does this work even if the previous company used a screen lock on it? I can't even get it past the lock screen anymore..

---
**Nokklen** | Score: 1 | 2023-09-05 22:16 UTC

Question, is it just a popup? Or do they actually have access to the device?

---
**TheMon420** | Score: 1 | 2023-10-12 14:15 UTC

I have a 2014 Mac mini, bought reputably, and would love to turn off remote management. 

LSS: computer store bought a bunch of Mac minis from a school, I bought 2, one was removed successfully the other wasn't. The store said I can return it but didn't have any more. It's currently on Monterey, can I remove it or should I just return it?

  ---
  **Lucas198019801980** | Score: 1 | 2024-07-22 18:51 UTC

  did you got to remove the mdm?

    ---
    **TheMon420** | Score: 1 | 2024-07-22 18:56 UTC

    Nah never able to.

---
**Pink-Elder-Berry** | Score: 1 | 2023-10-21 00:22 UTC

THANK YOU ! You saved my a** !! 😍

---
**Clear-Discussion8628** | Score: 1 | 2023-11-08 15:30 UTC

Hello, let me share mine solved. I bought a new refurbished Mac which had High Sierra OS. I wanted to install monterey. I made a bootable USB to install the os,  while installing I got "THE REMOTE MANAGEMENT.." on screen which I could not proceed further, I was shocked. 

I made a flash bootable with macos Catalina, it installed well ( I did not put my wifi this time) till I got to my Mac desktop screen, I was glad.

I connected to wifi then updated my Mac on software update. I then got another  update  for monterey 12gb (Wow!). I  updated now I am using macos monterey well. 

I hope may be this could save someone some time

---
**[deleted]** | Score: 1 | 2023-11-15 14:34 UTC

if I did   
sudo echo "0.0.0.0 iprofiles.apple.com" /etc/hosts  
& sudo profiles remove -all     


Is there a way I can get my mac to update from 14.1 to 14.1.1 now?   
It got ride of the MDM message but I don't see the SW update anymore.

  ---
  **Camp_1993** | Score: 1 | 2023-12-13 20:09 UTC

  hello, can you explain the command like I'm 5 years old lol  
  do I need the quotations around [0.0.0.0](https://0.0.0.0) iprofiles ? and do I type /etc/hosts before pressing enter? or are they two separate commands? Thank you in advance!

    ---
    **Morpheus_303** | Score: 1 | 2024-01-31 00:34 UTC

    did it worked for you by seperating them?

  ---
  **Morpheus_303** | Score: 1 | 2024-01-31 00:38 UTC

  yes you can download from appstore
