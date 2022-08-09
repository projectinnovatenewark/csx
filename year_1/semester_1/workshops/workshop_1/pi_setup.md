<div align=center><h1>Setting up your Raspberry Pi</h1></div>

In this workshop, the student will assemble the Raspberry Pi single-board computer and install the necessary software for the rest of the semester.

<div><h3>Note: </h3></div>
<div><ins>Please be careful when unboxing. These boxes will be needed to pack up the Raspberry Pi and its components at the end of the year.</ins></div>
<br>

In your package, you will find:

- Raspberry Pi Desktop Kit containing:
    - A 8GB Raspberry Pi 4 Model B
    - 16 GB MicroSD Card w/ NOOBS
    - Raspberry Pi Keyboard
    - Raspberry Pi Mouse
    - USB-C Power Supply
    - Official Beginner's Guide
    - Micro HDMI to HDMI Cable

- 10.1 inch LCD Monitor containing
    - LCD Monitor
    - Mounting Guards
    - USB-C Output Power Cable
    - Micro HDMI to HDMI
    - Power Supply Chord
    - Three (3) Heat Sinks

- Envelope containing:
    - One (1) Breadboard
    - Fifteen (15) Male-Male Jumper Wires
    - Fifteen (15) Female-Male Jumper Wires
    - Fifteen (15) Female-Female Jumper Wires
    - One (1) Motion Sensor
    - A Second Envelope Containing:
        - Five (5) LED Lights (Assorted colors)
        - Three (3) Tactile Buttons
        - One (1) Buzzer
        - Three (3) Ohm Resistors

<div align=center><h2>Setting up your Raspberry Pi</h2></div>

After unboxing, use the following step-by-step guide to build your Raspberry Pi

1. First we are going to add the heat sinks to the Raspberry Pi (going forward it will be referred to as the Pi).
    - <b><ins>CAUTION:</ins></b> Make sure you are positive when placing the heat sinks because the adhesive is very strong. Give a double check before dropping them in  place.

    a. As you can see, your Pi comes with 3 heat sinks designed to keep the CPU, RAM, and the USB Controller from overheating. The picture below labels where each heat sink belongs on the Pi.
    > The USB Controller splits the USB ports to share the same bandwidth and power
        
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/2_pi_with_sinks.jpg" width="400" height="auto" />
    </div>

    b. Place Pi guard #3 as pictured below on the pi to help place the heat sinks on the Pi. <b><ins>Careful handling the guards as they are very fragile!</ins></b>

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/7_pi_guards.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/3_use_guard_for_sinks.jpg" width="400" height="auto" />
    </div>

    c. After placing the heat sinks on the Pi, you should see the following:
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/5_pi_with_sinks.jpg" width="400" height="auto" />
    </div>

2. Insert the microSD card into the port on the bottom of the Pi.
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/22_micro_sd.jpeg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/21_insert_sd.jpeg" width="400" height="auto" />
    </div>

3. Remove the bolts off from the back of the display monitor. Make sure to keep these in a safe spot as they will be needed later.
    
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/6_remove_washers.jpg" width="400" height="auto" />
    </div>

4. Place Pi guard #1 on the back of the display as shown below:

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/7_pi_guards.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/8_place_first_guard.jpg" width="400" height="auto" />
    </div>

5. Place the Pi on top of the guard on the back of the display monitor.
    > The ethernet and USB ports should be facing away from the middle of the display.

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/9_place_pi.jpg" width="400" height="auto" />
    </div>

6. Place the plastic guard (#2) followed by the final guard (#3) on top of the Pi. Then screw each washer back on so that the Pi is secure without too much pressure being on the Pi.
    
    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/10_pi_guard_2.jpg" width="auto" height="300" />
    <img src="./Raspberry_Pi_setup_images/11_pi_guard_3.jpg" width="auto" height="300" />
    </div>

7. Below are the USB-C cable and the micro-HDMI cables as well as their corresponding Pi ports.
    a. The USB-C provides power to the Pi.
    b. The micro-HDMI cable is used to display the GUI of the Pi.

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/12_usbC_and_hdmi.jpg" width="auto" height="250" />
    <img src="./Raspberry_Pi_setup_images/13_port_view_of_pi.jpg" width="auto" height="250" />
    </div>

8. Plug in the USB-C into the display and then into the Pi as shown below:

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/14_plug_in_usbC_in_disp.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/15_plug_in_usbC_in_pi.jpg" width="400" height="auto" />
    </div>

9. Repeat step 9 for the micro-HDMI cable as shown below:

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/16_plug_hdmi_display.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/17_plug_hdmi_pi.jpg" width="400" height="auto" />
    </div>

10. Now we are going to connect the keyboard to the Pi. We want to utilize the USB 3.0 port as shown below:

    <div class=mdImage align=center>    
    <img src="./Raspberry_Pi_setup_images/31_keyboard_usb.jpg" width="400" height="auto" />
    </div>

11. Now that our keyboard is connected, we can connect our mouse. The desktop kit is convenient in that we can connect our mouse directly to the keyboard. This way we don't have to worry about the wire being too short. Go ahead and connect the mouse to the USB port closest to the edge of the keyboard as shown below:

    <div class=mdImage align=center>    
    <img src="./Raspberry_Pi_setup_images/34_mouse_&_keyboard.jpg" width="400" height="auto" />
    </div>


12. Below is the power supply chord for the display which in turn also provides power for the Pi. Plug in to the display and a wall outlet to get started for the next section.

    <div class=mdImage align=center>
    <img src="./Raspberry_Pi_setup_images/18_power.jpg" width="400" height="auto" />
    <img src="./Raspberry_Pi_setup_images/20_plug_in_power.jpg" width="400" height="auto" />
    </div>

<div align=center><h2>Installing Raspbian/Rasperry Pi OS & VS Code</h2></div>

Power on your Raspberry Pi by holding the power button on the back of your monitor for about 5 seconds. 

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/26_power_on.jpg" width="400" height="auto" />
</div>

<div align=center><h3>Installing Debian/Raspberry Pi OS</h3></div>

Now that everything is connected and the Pi is powered on, you should see something similar to the following screen:

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/23_installing_rasp_os.jpg" width="400" height="auto" />
</div>

11. Setup up your wifi network by selecting the “Wifi networks (w)” button circled in the picture below and follow the steps to connect to your local network.

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/24_wifi_setup.jpeg" width="400" height="auto" />
</div>

12. Select the language at the bottom of the screen to be “English (US)”. Then click on the install button in the top left corner and check the box next to “Raspberry Pi OS Full (32-bit) (RECOMMENDED)”. Then click the install button in the top left corner again. Now the OS should be installing onto your Raspberry Pi. This should take a few minutes until a popup appears to let you know that the OS has installed successfully.

13. There should be a prompt to update and restart the Raspberry Pi. It is recommended to do so.

<div align=center><h3>Installing VS Code and Git</h3></div>

14. Before doing the step below, we want to check if we can access the internet. Click on the web icon at the top left of your screen and type "google.com" in the browser.

**If you're unable to connect to the internet**, it's likely due to your computer's clock being out of sync. If this is the case, you will have to run a sequence of commands in your terminal. To make this process smoother, right click your mouse on the desktop. Click the option that reads "New File...", and name that file "start.txt". Now type/add the following command sequence into your text box `sudo systemctl stop systemd-timesyncd`, `sudo systemctl disable systemd-timesyncd`, then add this last command but fill in the date details (i.e. `2021-01-01 23:11` where "23:11" would represent 11:11 PM) based on your current time `sudo timedatectl set-time 'YEAR-MONTH-DATE TIME'`. Once you've added these commands in your text file, you will now copy and paste each command into your computer's terminal one by one. For future use, make sure to edit the time to reflect the current time when you are using the Pi.

We will be using an open-source version of VS Code that is compatible with the Pi. Click the terminal icon in the to left portion of your screen as circled below.

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/27_rasp_term_icon.png" width="400" height="auto" />
</div>

You will see the Raspberry Pi's terminal open. This should look similar to the emulator used in class.

15. The following commands will install VS Code using apt, which is a tool for installing programs on your computer via the command line.

16. `sudo apt update` followed by `sudo apt install code`.

17. Now let’s install Git in the VS Code window. Open VS Code using the Raspberry Pi icon in the top left corner -> Programming -> Visual Studio Code.

18. The VS Code window should pop up. To open a terminal in your VS Code window, press “ Ctrl + shift + ~”. This will look like the following:

<div class=mdImage align=center>
<img src="./Raspberry_Pi_setup_images/30_installing_git.png" width="500" height="auto" />
</div>

This step requires a Github account. If you have not created one yet, do so <a href="https://github.com/">here</a>. If you already have a Github account feel free to continue.

<!-- 19. In your terminal, use the following commands to enter your github credentials:
`git config --global user.name "[YOUR GITHUB USERNAME]"`
> Whenever you see words in all caps inside brackets like the above, it means to replace it with what the command is asking for. That also means that the brackets should be removed.

then:
`git config --global user.email “[YOUR GITHUB ASSOCIATED EMAIL]”`

Now you're all set to utilize VS Code, Git, and Github for the rest of the semester. Happy Coding! -->
