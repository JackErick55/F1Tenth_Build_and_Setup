# Setting Up F1Tenth Firmware and Software

## Note

The project is conducted with a Jetson Orin Nano Developer Kit 8GB. Depending on the current firmware version of the Jetson Orin Nano Developer Kit depicts how the Jetson will be set up. If the Jetson has a firmware verison below 5.1.0 extra steps will need to be taking.

Though out this process the "**Host PC**" is your personal machine not the F1Tenth Car.

## 1. First Boot: Flashing Jetpack Jetson Orin Nano Developer Kit Using Ethcher

To prepare your micro SD card, you’ll need a computer with Internet connection and the ability to read and write SD cards, either via a built-in SD card slot or adapter.

### 1.1 Downloading Image

Download the Jetson Orin Nano Developer Kit SD Card image from [JetPack SDK Page](https://developer.nvidia.com/embedded/jetpack), and note where it was saved on the computer. (Reference image and select green box to download Jetpack 6.2 for an SD card image.)

![JetPack 6.2 for an SD card image](<Setting_Up_F1Tenth_Pics/Screenshot from 2025-04-21 15-02-31.png>)

### 1.2 Writing SD Card Image

Write the image to your microSD card by following the instructions [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#write) according to the type of computer you are using: Windows, Mac, or Linux.

### Use the following instructions to download [Ether](https://etcher.balena.io/)

### Instructions for Linux

There are **2 ways** to write the SD card image one is using a graphical program like **Etcher**, and the other is via **command line**.

### **Option 1: Use Etcher**

1. Download, install, and launch Etcher.

    ![Ether window](Setting_Up_F1Tenth_Pics/image-8.png)

2. Click “Select image” and choose the JetPack zipped image file downloaded earlier.

3. Insert your microSD card. If you have no other external drives attached, Etcher will automatically select the micro SD card as target device. Otherwise, click “Change” and choose the correct device.

    ![Select the micro sd card](Setting_Up_F1Tenth_Pics/image-9.png)

4. Click “Flash!” Your OS may prompt for your username and password before it allows Etcher to proceed.

    ![Username and Password Prompt](Setting_Up_F1Tenth_Pics/image-10.png)

    It will take Etcher 10-15 minutes to write and validate the image if your microSD card is connected via USB3.

5. After Etcher finishes, eject (⏏) the SD Card using Files application.

    ![select eject](Setting_Up_F1Tenth_Pics/image-11.png)

6. Physically remove microSD card from the computer.

### **Option 2: Use Command Line**

1. Open the Terminal application by pressing `Ctrl + Alt + t`.

2. Insert your microSD card, then use a command like this to show which disk device was assigned to it:

    `dmesg | tail | awk '$2 == "sd" {print}'`

    ![Show disk device](<Setting_Up_F1Tenth_Pics/Pasted image.png>)

3. Use this command to write the zipped SD card image to the microSD card:

    `/usr/bin/unzip -p ~/Downloads/jp60-orin-nano-sd-card-image.zip | sudo /bin/dd of=/dev/sda bs=1M status=progress
    `

    For example:

    ![Write the zipped SD card image](<Setting_Up_F1Tenth_Pics/Pasted image (2).png>)

    When the dd command finishes, eject the disk device from the command line:

    `sudo eject /dev/sda`

4. Physically remove microSD card from the computer.

    After your microSD card is ready, proceed to [Setup your developer kit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit#setup).

## 2. Setup and First Boot

### 2.1 Setup

1. Insert the microSD card (with system image already written to it) into the slot on the underside of the Jetson Orin Nano module.

2. Power on your computer display and connect it.

3. Connect the USB keyboard and mouse.

4. Connect the provided power supply. The Jetson Orin Nano Developer Kit will power on and boot automatically.

![Insert SD card](<Setting_Up_F1Tenth_Pics/Pasted image (3).png>)

### 2.2 First Boot

A green LED next to the USB-C connector will light as soon as the developer kit powers on. When you boot the first time, the Jetson Orin Nano Developer Kit will take you through some initial setup, including:

- Review and accept NVIDIA Jetson software EULA
- Select system language, keyboard layout, and time zone
- Connect to Wireless network
- Create username, password, and computer name
- Log in

### 2.3 After Logging In

You will see this screen. Congratulations!

![Home Screen](<Setting_Up_F1Tenth_Pics/Pasted image (4).png>)

## If First Boot is Unsuccessful

### NOTE

If this first boot is unsuccessful it could be because an old firmware version. If the firmware is below 5.1.0 it can not make the Just to 6.0 or high unless the JetPack SDK is used on a Ubuntu 20.04 machine. (If you don't use a Ubuntu 20.04 machine than the flash will fall and the Jetson will be bricked until it is properly flashed)

The firmware version can be seen when the GUI first boots up you will see the firmware verion at the top on the screen next to the `Jetson UEFI firmware`.

![alt text](<Setting_Up_F1Tenth_Pics/Pasted image (5).png>)

## Steps to Update and Flash New Firmware (6.0 +)

### Equitment needed

- Jetson Orin Nano Dev Kit
- Host PC running on **Unbuntu 20.04** with **Nvidia SDK Manager 2.2.0**
- 128 gb sc card
- 500 gb NVMe
- Nvidia Jetson Power cable (19.0V, 2.37A)
- Data capable usb to type-c
- Jumper wire
- Display with display port
- Display port cable
- Keyboard
- Mouse

## 1. Download Jetpack SDK on Ubuntu 20.04 Machine

Start by opening your Ubuntu 20.04 machine and using the [link](https://developer.nvidia.com/sdk-manager) to download the Nvidia SDK Manager. Then creating a Nvidia account to log in to the SDK Manager.

## 2. Hareware Setup

### 2.1 Install SD card and NVMe

Install blank SD card and blank NVMe into Jetson Orin Nano

### 2.2 Put Jetson in Force Recovery Mode

Connect juper cable to the `FC REC` and `GND` pin to put the Jetson in Force Recovery mode. (This enbles the board to be detected by the SDK manager)

    ![Jetson in Force Recovery Mode](<Setting_Up_F1Tenth_Pics/Screenshot from 2025-04-21 16-26-21.png>)

### 2.3 Connect Jetson to Host Computer

 Connect the USB to USB type-c cable from the machine with Ubuntu 20.04 with the other end going to the type-c port on the Jetson.

    ![Jetson connected Ubunut machine](Setting_Up_F1Tenth_Pics/image-19.png)

### 2.4 Connect the power source to the Jetson

![Power Jetson](Setting_Up_F1Tenth_Pics/image-20.png)

### 2.5 Open the SDK Manager (2.2.0 version ) on the Host computer (Ubuntu 20.04)

### 2.6 Select The Jetson Orin Nano Developer Kit

After the `Jetson Orin Nano [8GB developer kit version]` is selected click `OK`

![Jetson Orion Nano Developer Kit selected in SDK Manager](Setting_Up_F1Tenth_Pics/image-21.png)

## 3. Update Firmware to JetPack 6.1

### 3.1 `STEP 1` of SDK Manager

Below is an image that shows the inforamtion that should be selected in `STEP 1` of the SDK Manager. After the information is selected click `CONTINUE TO STEP 2` in the bottom right hand corner of the SDK Manager.

![Information in step 1 of the SDK Manager](Setting_Up_F1Tenth_Pics/image-27.png)

### 3.2 `STEP 2` of SDK Manager

Once in `STEP 2` unsure that Jetson Linux and Jetson Runtime Components are selected under TARGET COMPONENTS.

![Jetson Linux and Runtime Components Selected](Setting_Up_F1Tenth_Pics/image-28.png)

> Before proceeding to `STEP 3` **DISCONNECT** the jumper wire taking the Jetson out of Force Recovery Mode.

In the bottom left hand coner check the box `I accept the terms and conditions of the license agreement`. Then click `CONTINE TO STEP 3`.

A window will pop up as show below stating "The specified folder doesn't exist. Do you want to create?" Click: **Create**

![Create folder for documents to be downloaded](Setting_Up_F1Tenth_Pics/image-24.png)

**Next** it will ask for your password.

![Password prompt](Setting_Up_F1Tenth_Pics/image-25.png)

### 3.3 `STEP 3` of SDK Manager

Then all of the host componets will be installed and the Jetson Linux image will be created.

Once the OS image is ready the following screen will appear. Select the following parameters shown in the picture.
(username: darc-f1-<car #>)
(password: lab password)

![Jetson configuration select](Setting_Up_F1Tenth_Pics/image-29.png)

Then all of the host componets will be installed and the Jetson Linux image will be created.

### 3.4 `STEP 4` of SDK Manager

 Once the the flash finishes connect a monitor via display port, mouse and keyboard. The Jeston should be setup. Then login into the system, open a terminal and type `ip addr show` confirm that the IP Address matches the IP address show on the HOst computer. An example is shown below.

![Final installation of SDK components](Setting_Up_F1Tenth_Pics/image-30.png)

When this install is complete the Jetson is ready to proceed to the next step.

## 4. Connect the Jetson Orin Nano to WiFi

To connect the WiFi for the Jetson depends on the type of Network the Jetson is trying to connect to.

### 4.1 Option 1: Non - Static IP Address

If the Jetson is trying to connect to a large network the IP address may constantly change. To solve this the MAC address can be to the network allowing the Jetson to connect.

To obtain the IP Address run `ip link show`. Then under the wireless name (example `wlan0`) there will be a line that starts with `link/ether` followingf this is the MAC address for the wireless network. (example `28:d0:43:84:f5:9f`)

### 4.2 Option 2: Static IP Address

If you are connecting the Jetson to a personal network than a static IP address will need to be set. THis will take several steps.

Start by finding the wifi connection device. This can be down by running `nmcli d` then use the device name for wifi.

![Example of command: nmcli d](Setting_Up_F1Tenth_Pics/image-17.png)

For the example above the device name is wlan0

### 4.2.1 Obtain Current IP Address

 To get the currently-assigned IP address use the command `ip addr show dev wlan0`.

![Currently-connected WiFi IP address](Setting_Up_F1Tenth_Pics/image-12.png)

Currently-connected WiFi IP address.

### 4.2.2 Obtain Name of Connection

 To set a static IP address, you will also need to know the name of the connection. This is usually the same as the SSID of the WiFi network but not always. To see the list of current connections, use the command `nmcli c show`.

![List of connections](Setting_Up_F1Tenth_Pics/image-13.png)

List of connections.

### 4.2.3 Setting Static IP Address:f5

 To set a static IP address use: the command sudo `nmcli c mod [CONNECTION_NAME] ipv4.address [NEW_ADDRESS]/[CIDR]` where `[CONNECTION_NAME]` is replaced with the name of your WiFi connection that you got from step 8, `[NEW_ADDRESS]` is replaced with the static IP address that you want to set, and `[CIDR]` is the [CIDR representation](https://www.ionos.com/digitalguide/server/know-how/cidr-classless-inter-domain-routing/) of the subnet (usually 24).

![Setting static IP address](Setting_Up_F1Tenth_Pics/image-14.png)

Setting static IP address.

### 4.2.4 Setting Default Gateway

 To set the connection’s default gateway, use the command `sudo nmcli c mod [CONNECTION_NAME] ipv4.gateway [GATEWAY_IP]` where `[CONNECTION_NAME]` is replaced with the name of your WiFi connection that you got from step 8 and `[GATEWAY_IP]` is replaced with the IP address of your WiFi network’s gateway/router.

![Setting IP gateway](Setting_Up_F1Tenth_Pics/image-15.png)

Setting IP gateway.

### 4.2.5 Setting Connection DNS Servers

 To set the connection’s DNS servers, use the command sudo `nmcli c mod [CONNECTION_NAME] ipv4.dns "[DNS_SERVER1]"` where `[CONNECTION_NAME]` is replaced with the name of your WiFi connection that you got from step 8 and `[DNS_SERVERS]` is replaced with a comma-separated list of DNS server IP addresses. Google DNS servers at `8.8.8.8` and `8.8.4.4` are recommended.

### 4.2.6 Setting Connection to Always Use Static IP Address

 To disable DHCP and always use the static IP address on this connection, use the command `sudo nmcli c mod [CONNECTION_NAME] ipv4.method manual` where `[CONNECTION_NAME]` is replaced with the name of your WiFi connection that you got from step 8.

![Setting connection to always use static IP](Setting_Up_F1Tenth_Pics/image-16.png)

Setting connection to always use static IP.

### 4.2.7 Save Changes

 To save the changes you’ve made, run the command `sudo nmcli c up [CONNECTION_NAME]` where `[CONNECTION_NAME]` is replaced with the name of your WiFi connection that you got from step 8.

### 4.2.8 Use SSH to Verify Changes Have Been Saved

 To verify that you can SSH into the NVIDIA Jetson Orin Nano Developer Kit, verify that the Pit/Host PC is connected to the same network as the Jetson Orin Nano Developer Kit and use an SSH client on the Host PC to connect to the new IP address of the Developer Kit. On Linux this would be done with the command ssh f1tenth@[IP_ADDRESS] where [IP_ADDRESS] is replaced with the static IP address that you assigned to the Developer Kit. After you have verified that SSH works correctly, you can close the connection to the Developer Kit in your terminal emulator.
**After setup SSH using following command**

`ssh -p 22 User@ip adress`

**example:**
`ssh -p 22 darc-f1@10.152.69.100`

**Note**: If network is having difficulty connecting got to the wi-fi settings under the`IPv4` tab and select `Automatic` unsure the `DNS` is clear.

## 5. Install Chromium Using Command Line

- 5.1 Install Chromium using the following command

    `sudo apt-get install chromium-browser`

- 5.2 Open Chromium using the following command

    `chromium-browser`

- 5.3 Add Chromium to favorites by right clicking on the Chromium icon and click "add to favorites"

## 6. Run Jetson Orin Nano from SSD

In the build instruction we applied an SSD NVMe on to the Jetson Orin Nano. We will now make use of this SSD by switching the rootfs to point to the SSD. In effect, the system will now run from the SSD, the SD card is only there to boot the system. Therefore everything you install on your system will automatically installed on the SSD.

Please follow this tutorial [here](https://www.jetsonhacks.com/2020/05/29/jetson-xavier-nx-run-from-ssd/) that has both video and commands integrated to enable your Jetson NX to run from the SSD

>I highly recommend going to the "here" link above it is very helpful even though it is meant for the Jetson Xavier NX and the same commands work for the Jetson Orin Nano

### Important

>These script changes the rootfs to the SSD after the kernel image is loaded from the eMMC/SD card. For the Xavier NX, you will still need to have the SD card installed for booting. As of this writing, the default configuration of the Jetson NX does not allow direct booting from the NVMe.

The [here](https://www.jetsonhacks.com/2020/05/29/jetson-xavier-nx-run-from-ssd/) link will take you to a cite and execute the following steps

1. Ensure the SSD is correctly installed

2. Watch video on how to format SSD using this [link](https://youtu.be/ZK5FYhoJqIg)
3. Open a terminal window on the Jetson and run the following commands

**Note** :*You should do this process directly after creating a new SD card.*

On the [JetsonHacks account on Github](https://github.com/jetsonhacks/rootOnNVMe), there is a repository rootOnNVMe. Clone the repository:

``` bash
git clone https://github.com/jetsonhacks/rootOnNVMe
```

and switch over to that repository’s directory:

``` bash
cd rootOnNVMe
```

Next, copy the rootfs of the eMMC/SD card to the SSD

``` bash
./copy-rootfs-ssd.sh
```

Finally, we will add a service which will run a script when the system starts up. The script will “pivot the root” to the SSD so that the system will run from the SSD.

``` bash
./setup-service.sh
```

Before moving on run the following command to rest are the Jetson.

``` bash
sudo reboot
```

## 7. Setup Bluetooth and Connect Controller

### Steps to Setup Bluetooth on Jetson Orin Nano

### 7.1 Update System Packages

 Update the system to make sure the system is up to date.

``` bash
sudo apt update
sudo apt upgrade
```

### 7.2 Install Bluetooth Packages: Install the necessary Bluetooth packages if they’re not already installed

```
sudo apt install bluez bluez-tools
sudo apt install pulseaudio pulseaudio-module-bluetooth
```

#### - Enable Bluetooth Service: Start and enable the Bluetooth service

```
sudo systemctl start bluetooth
sudo systemctl enable bluetooth
```

If your adapter is detected, you should see output like hci0: Type: BR/EDR .... If no device is found, it might be due to a missing driver or unsupported hardware.

#### Check if bluez and bluez-tools are installed

Run this command:

```
sudo dpkg -l | grep bluez
```

**If the packages are installed, you should see an output like this:**

```
ii  bluez          <version>     <architecture>   <description>
ii  bluez-tools    <version>     <architecture>   <description>
```

Run this command:

```
dpkg -l | grep pulseaudio
```

This will show all ```pulseaudio``` related packages that are installed. Look for ```pulseaudio``` and ```pulseaudio-module-bluetooth``` in the output. If installed, the output will look similar to:

```
ii  pulseaudio                     <version>     <architecture>   <description>
ii  pulseaudio-module-bluetooth     <version>     <architecture>   <description>
```

If they are not installed, there will be no output or only partial results.

#### Now you should be able to go to settings and connect the controller
