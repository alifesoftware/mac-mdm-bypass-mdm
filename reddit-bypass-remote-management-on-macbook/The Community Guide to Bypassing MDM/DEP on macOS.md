# The Community Guide to Bypassing MDM/DEP on macOS

**Author:** Manus AI  
**Based on:** Community contributions from r/mac  
**Source Thread:** [Bypass remote management on Macbook pro after clean install Catalina — solved](https://www.reddit.com/r/mac/comments/pi9beh/bypass_remote_management_on_macbook_pro_after/) (r/mac)

Device Enrollment Program (DEP) and Mobile Device Management (MDM) locks can render a second-hand MacBook virtually unusable by forcing it to enroll in a former organization's management system. Based on extensive community testing and troubleshooting, this guide compiles the most successful methods to bypass MDM on various versions of macOS.

---

## 1. The Classic Setup Bypass (For macOS Catalina & Older)

On older versions of macOS, the setup assistant allows you to skip connecting to the internet. However, the Mac may still remember previously saved Wi-Fi networks and auto-connect in the background, triggering the MDM lock.

**Instructions:**
1. Completely power off your home modem/router. This ensures the Mac has absolutely no way to connect to any previously saved network [1].
2. Boot the Mac and proceed through the initial macOS setup.
3. When prompted to connect to Wi-Fi, select the option indicating you do not have an internet connection.
4. Complete the setup and create your local administrator account.
5. Once you are at the desktop, you can turn your modem/router back on.

*Note: While this bypasses the initial lock, you may still receive a daily "Device Enrollment" notification. See Section 3 to disable this.*

---

## 2. The Hotspot "Bait-and-Switch" (For macOS Monterey, Ventura, Sonoma, & Sequoia)

Newer macOS versions mandate an internet connection to activate the Mac during setup. The classic bypass will not work because there is no option to skip the network step.

**Instructions:**
1. Create a macOS bootable USB drive using another computer.
2. Boot your Mac into **Recovery Mode** (Command + R) or via the bootable USB.
3. Open **Disk Utility** and completely erase the Mac's internal drive.
4. Begin the macOS installation process.
5. When the system requires an internet connection to activate the Mac, **connect to a mobile hotspot from your smartphone** [1]. This is crucial because it gives you on-demand control over the network.
6. The installation will proceed, and a progress bar will appear.
7. **The Critical Step:** The moment the progress bar reaches 100% and the Apple logo appears (or the computer begins to reboot), **immediately turn off the mobile hotspot on your phone** [1].
8. When the Mac boots up to the "Choose a Network" window, you will now have the option to choose "Continue without network" (or similar).
9. Proceed to finish the setup process and create your user account.

---

## 3. Blocking MDM Servers via Hosts File (Preventing Re-enrollment & Nags)

Even after bypassing the setup screen, macOS may persistently prompt you to enroll the device. The most universally successful and least invasive way to stop this is by blocking the Mac from communicating with Apple's MDM servers [2].

**Instructions:**
1. Boot into your Mac normally and log in to your administrator account.
2. Open the **Terminal** application (Applications > Utilities > Terminal).
3. Type the following command to open the hosts file in a text editor:
   ```bash
   sudo nano /private/etc/hosts
   ```
4. Enter your administrator password when prompted.
5. Use the arrow keys to navigate to the bottom of the file and add the following lines [2]:
   ```text
   0.0.0.0 iprofiles.apple.com
   0.0.0.0 mdmenrollment.apple.com
   0.0.0.0 deviceenrollment.apple.com
   0.0.0.0 albert.apple.com
   ```
   *(Optional: Adding `0.0.0.0 gdmf.apple.com` will also block updates, which some users prefer to ensure the MDM profile doesn't return, but it breaks native macOS software updates [1].)*
6. Press `Control + X` to exit, then press `Y` to save, and hit `Enter` to confirm the file name.
7. To verify the block is working, run:
   ```bash
   sudo profiles show -type enrollment
   ```
   You should receive a `(34000) Error Domain=MCCloudConfigurationErrorDomain` error, indicating the Mac can no longer reach the enrollment server [1].

---

## 4. Advanced: Removing Existing Profiles

If an MDM profile has already been installed on the system, you can attempt to force-remove it via Terminal before applying the hosts file block.

**Instructions:**
1. Open **Terminal**.
2. Run the following command to delete all configuration profiles:
   ```bash
   sudo profiles remove -all
   ```
3. *Warning:* This will delete all profiles on the Mac, not just the MDM one.

---

## Tips, Tricks, and Gotchas

| Gotcha / Tip | Explanation & Workaround |
| :--- | :--- |
| **"Hosts: Read-only file system" Error** | If you try to edit the hosts file in Recovery Mode without properly mounting the drive, it will fail. It is highly recommended to edit the hosts file during a **normal boot session** using `sudo nano /private/etc/hosts` [1]. |
| **NVRAM Reset** | Before attempting a clean install, perform an NVRAM reset (`Option + Command + P + R` during boot) to wipe any lingering memory of old Wi-Fi networks [1]. |
| **Contacting the Seller** | The absolute best "fix" is contacting the previous owner (e.g., the school district or company). If they legitimately sold it, they simply forgot to release the serial number from Apple Business Manager. Once they release it on their end, a simple wipe and reinstall fixes everything permanently [1]. |
| **System Integrity Protection (SIP)** | Some older methods require booting into Recovery Mode and running `csrutil disable` to turn off SIP before moving `.plist` files. However, community consensus suggests that simply editing the hosts file (Method 3) is sufficient and doesn't require compromising system security [2]. |
| **Single User Mode** | If you are stuck on a frozen Remote Management login screen and turning off the router doesn't work, try booting into Single User Mode (`Command + S`) while the modem is off to bypass the freeze [1]. |

---

### References
[1] r/mac Community. "Bypass remote management on Macbook pro after clean install Catalina - solved." Reddit. https://www.reddit.com/r/mac/comments/pi9beh/bypass_remote_management_on_macbook_pro_after/
[2] Kakatua2012. Reddit Comment on Hosts File Modification. https://www.reddit.com/r/mac/comments/pi9beh/comment/irku82d/
