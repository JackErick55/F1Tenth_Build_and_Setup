# Building F1tenth

**Note:** Before starting the process of disassembling the Traxxas you may want to take this time to drive the car to see it full capability as it is very remarkable. This will aslo give you a baseline understanding of full capabilities of this car.

## 1. Lower Level Chassis

We begin with setting up the Lower Level Chassis. We will be removing some of the internal parts of the Traxxas and repopulating them with our own. Below is a video of this process being done to an older model. It is still helpful to watch as there is a large amount of over lap.

[Lower Level Chassis](https://youtu.be/IoWHUGFfrRE)

## 1.1 Removing Traxxas Stock Components

Take the Traxxas from its box. Remove the four body clips to remove the body so you are left with this:

![Traxxas chassis with body shell removed](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 13-45-52.png>)

We are going to remove several electrical componets including the speed controller and reciver. The only component which we will not be removing is the servo and the drive otor, which is the little black box in the right corner and the large blue motor. There are three hex keys that come with the Traxxas. You will use these to remove and/or install almost all of the screws on the chassis. You may want to have a bowl or container of sorts nearby to hold all the screws that you’ll be removing as these screws will be needed later.

Start by unscrewing the top of the black receiver box.

![alt text](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 13-46-04.png>)

Once the top is open, you will see the receiver labelled “TQi”. **Disconnect** all of the wires going to the receiver. Move the wires out of the way.

![Remove these wires](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 13-55-50.png>)

The receiver is attached to bottom of the receiver box with double sided tape. Carefully, but firmly, pry the receiver from the receiver box and remove it.This will expose the two screws which mount the receiver box to the chassis. Unscrew the screws to remove the receiver box.

![Screws that hold the reciever box in place](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 13-46-33.png>)

After this you can remove the antenna as it will no long be used. There is a set screw that holds the antenna in place. Once the set screw is removed the antenna tube will easily slide out.

![Location of antenna set screw](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 13-46-42.png>)

Then, remove the Traxxas ESC, the blue box labelled “VXL-3s”, by unscrewing the two screws that attach the ESC to the chassis. Disconnect the wires (white, yellow, and blue) that go from the ESC to the Brushless Motor. The wires are connected by what are called bullet connectors. You can safely pull the wires apart by grabbing each side of the connector and pulling.

![Location of ESC screws](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 13-46-50.png>)

Lastly, remove the 2 plastic side bars on each side of the car. THese side bars are held on by 4 screws apiece. These holes will be used as mounting points later.

![Location of side bar screws](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 14-02-09.png>)

Your final result should look as follows.

![Final result](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-12-23.png>)

## 1.2 Attaching the Standoffs

Once the sidebars are removed, located on either side of the chassis. Attach three 45mm M3 standoffs onto the chassis using M3 X 10 screws as shown.

Use M3 screws from underneath the chassis to secure the standoffs. Arrange the standoffs so that two standoffs go on the Motor side and 1 go on the battery side. This arrangement allows for better access to the battery. You may want to use thread-locking fluid to secure these standoffs as the vibrations of the car during movement may loosen them over time.

![Location of 45mm M3 Standoffs](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-20-18.png>)

The standoffs in the picture will be explained in more depth in the next section.

## 1.3 Setting Up the Battery

### Danger

``` text
LIPO (LITHIUM POLYMER) BATTERY SAFETY WARNING

LiPO batteries allow your car to run for a long time, but they are not something to play with or joke about. They store a large amount of energy in a small space and can damage your car and cause a fire if used improperly. With this in mind, here are some safety tips for using them with the car.

When charging batteries, always monitor them and place them in a fireproof bag on a non-flammable surface clear of any other objects.

Do not leave a LIPO battery connected to the car when you’re not using it. The battery will discharge and its voltage will drop to a level too low to charge it safely again.

Unplug the battery from the car immediately if you notice any popping sounds, bloating of the battery, burning smell, or smoke.

Never short the battery leads.

Do not plug the battery in backwards. This will damage the VESC and power board (and likely the Jetson as well) and could cause a short circuit.

See this video for an example of what might happen if you don’t take care of your batteries. Be safe and don’t let these happen to you!
```

Place the battery into the compartment opposite of the motor.

![Battery location on Lower Level Chassis](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-22-49.png>)

## 2. Autonomy Elements

In the second part of the hardware setup we start preparing the autonomy elements for our F1TENTH car. Below is a video of this process being done to an older model. It is still helpful to watch as there is a large amount of over lap.

[F1tenth Autonomy Elements](https://youtu.be/L-V-0zzkl10)

## 2.1 Preparing the NVIDIA Jetson Orin Nano

When you purchase a NVIDIA Jetson Orin Nano, it is attached to small plastic development board. In order to use it on the car, you will need to unscrew the Jetson Orin Nano and disconnect the Wi-Fi antenna wires from the development board. First of all unbox your NVIDIA Jetson Orin Nano.

### 2.1.1 Unpackage the NVIDIA Jetson Orin Nano From this Box

![Jetson Orin Nano Box](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-43-32.png>)

### 2.1.2 Remove the screws that attach the plastic frame to the NVIDIA Orin Nano

![Remove screws from the Jetson Orion Nano frame](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-43-43.png>)

### 2.1.3 Remove Antenna Wires

Afterwards you can turn the Jetson Orin Nano on the back side. You will see the plastic development board is still attached because of the two antenna cables. The two antenna cables are clipped to the Jetson Orin Nano. You have to unclip both of them. You can either use your fingers are lift them with a flat screwdriver.

![Remove antenna wires](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-52-11.png>)

### 2.1.3 Install SSD card

Next remove the screw and insert SSD card then put back in the screw to secure SSD card in place.

![Install SSD card](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-44-18.png>)

Finally your NVIDA Jetson Orin Nano is seperated from the developer board and the SSD card is installed. This is the version you can now screw to the platform deck.

![Nvidia Jetson Orin Nano demounted from the developer board](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 15-58-57.png>)

## 2.2 Preparing the WiFi Antenna

In this step we will prepare the WiFi antennas to be mounted on the platform deck. In the step you will need both the antennas, the 3D printed antenna mount, 2 - 45mm M3 Standoffs, and 2 - M3 X 10 screws.

![Parts overview](<Building_F1Tenth_Pics/IMG_4648.jpg>)

First put the M3 X 10 screw into 3D printed antenna mount as shown below (Image on the left). Next attach the 45mm M3 standoff (Image in the center). Then use a hex head screwdrive and plyers to firmly tighten in place (Image on the right).

![Step by step bracket and standoff assebly](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 15-51-00.png>)

Once you’ve done these steps, take the washers and nut off of each the threaded end of the antenna cables and place the brass thread end on the cable so the threads a poking out on the back side of the L - bracket. After the threads are throught the bracket place the washers back on. Then thread the nut in place using plyers to make sure the nut is secure. Repeat this process for both the left and right side. The image below shows the result of the steps above.

![Result of threading the antenna cables in place](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 16-32-53.png>)

We can now move on to mounting all of the autonomy elements onto the Upper Level Chassis in the next section. Second accomplishment completed.

## 3. Upper Level Chassis

In the third part we’re going to assemble the upper level chassis and mount the important components. Below is a video of this process being done to an older model. It is still helpful to watch as there is a large amount of over lap.

[F1Tenth Upper Level Chassis](https://youtu.be/L-V-0zzkl10)

Place the **Platform Deck** so it’s facing you like this. The **Platform Deck** is the laser cut piece out of 1/4" plexglass.

![Platform Deck](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 14-46-53.png>)

To make things easier to follow, we define **Front, Rear, Away,** and **Towards** like above.

### Important

``` text
This piece is not symmetric. It can be noted that the outline of the base plate is not the same and neither are several of the holes. PAY ATTENTION TO THE LAYTOUT
```

The following image shows the five components that we will be mounting on the Platform Deck.

![Platform Deck Overview](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 14-44-43.png>)

## 3.1 Mounting the VESC

Place the VESC on the Platform Deck so that the power wires are facing AWAY from you and the three cables labelled A, B, and C are facing TOWARDS you.

![VESC placed in correct position on Platform Deck.](<Building_F1Tenth_Pics/IMG_4642.jpg>)

Flip the Platform Deck and the VESC over and use two M5 X 10 screws, mount diagonal from each other to attach the VESC to the Platform Deck, like shown below. Mounting holes for Powerboard and VESC.

**Note:** that this is view of the bottom of the Platform Deck.

![Bottom view of how to mount the VESC](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 15-00-35.png>)

## 3.2 Mounting the Antenna

After the VESC is mounted. We mount the antenna standoffs and cables to the rear of the platform deck. The reason for that is that we want to lay the antenna cables beneath the powerboard and connect it directly to the NVIDIA Jetson Orin Nano before mounting it.

Use the M3 X 10 screw to mount the antenna standoffs+cable onto the platform deck.

![Attach antenna mount to platform deck](<Building_F1Tenth_Pics/New_F1Tenth_Pics_4_2025/Screenshot from 2025-04-18 16-55-49.png>)

Afterwards you can directly attach the black antennas to the antenna mount.

![Attach the antennas to the antenna mount.](<Building_F1Tenth_Pics/New_F1Tenth_Pics_4_2025/Screenshot from 2025-04-18 17-00-11.png>)

## 3.3 Mounting the NVIDIA Jetson Orin Nano

Now its time to mount the NVIDIA Jetson Orin Nano. Before we mount the Jetson on the platform deck please connect the antenna cables to the back of the Jetson. Flip the Jetson around and clip both antenna cables to the antenna connectors on the Jetson.

![Connect antenna wires](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 17-14-27.png>)

Then we need to install the 15mm M2.5 standoffs for the Jetson on the Platform deck. Screw the standoffs to the top of the platform deck to the specific NVIDA Jetson Orin Nano mount holes. Thread the M2.5 X 8 screw from underneath the Platform Deck up and secure 15mm standoff in place.

![Jetson OrinNano Standoff locations](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 17-24-35.png>)

Now you can place the Jetson Orin Nano on the mounted standoffs. Use the 4 main holes on top of the Jetson to mount the Jetson to the platform deck with M2.5 X 8 screws.

![Jetson Orin Nano screw locations](<Building_F1Tenth_Pics/Screenshot from 2025-04-18 17-25-08.png>)

## 3.4 Mounting the Powerboard

Before attaching the Powerboard you will first need to solder all of the components onto the Powerboard. Below is a table with the name of the component, quanity, position on the Powerboard, and an image of the component.

**Note:** There are 3 capacitors that are polarized meaning the direction of the capacitor matters. Please reference the second image as it informs you of the proper direction. **The lines on the top on the power board are positive**

![Powerboard component table](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 18-44-02.png>)

![Powerboard before and after](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 18-59-37.png>)

The image below shows the three holes used to mount the Powerboard. Only three of the Powerboard mounting holes are used. Thread the M3 X 10 screw from underneath the Platform Deck up and secure 3 M3 25mm standoff. Then, secure the Powerboard to the 25mm standoff with a M3 x 8mm screw.

![Platform Deck Overview](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 14-44-43.png>)

Side view of Powerboard mounted on Platform Deck. There should be a gap between the Powerboard and the VESC.

![Side view of Powerboard](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 18-55-13.png>)

![Overview of Powerboard](<Building_F1Tenth_Pics/IMG_4736.jpg>)

After installing the Powerboard here is a top view of Powerboard mounted on Platform Deck. The **green terminal blocks** are facing the **FRONT** of the car.

## 3.5 Mounting the Lidar

The last component to mount is the lidar. Here, we use the Hokuyo UTM-10LX. The mounting holes for the Hokuyo UST-10LX are slightly different than the Hokuyo UTM-30LX.

![Lidar mounting holes](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-31-47.png>)

Lidar mounting holes.

Use the appropriate mounting holes for your lidar.

Use 2 M3 X 8 screws to mount from underneath.

![Lidar mounted on Platform Deck](<Building_F1Tenth_Pics/IMG_4739.jpg>)
Lidar mounted on Platform Deck.

**The upper level chassis is complete and we’re ready to assemble everything!**

## 4. Putting it all together

Now that we have the autonomy elements attached to the upper level chassis, we are going to attach the upper level chassis to the lower level chassis. This part may be a tad unwieldy due to the amount of wires and cables that have to be contained. Below is a video of this process being done to an older model. It is still helpful to watch as there is a some over lap.

[F1Tenth full assembly](https://youtu.be/vNVFCq688ck)

## 4.1 Mounting the Upper Level Chassis to the Lower Level Chassis

Gently place the upper level chassis on top of the 45mm M3 standoffs of the lower level chassis. The VESC should be towards the back of the car. Thread the steering servo cable from the lower level chassis, through one of the Platform Deck slot on the far side. Then use three M3 x 10mm screws to attach the Platform Deck to the standoffs on the lower level chassis.

![Upper Level Chassis gently placed on top of Lower Level Chassis](<Building_F1Tenth_Pics/IMG_4743.jpg>)

**Note:** It may be useful to use a zip tie to secure the USB cable from the lidar to the platform.

### Danger

``` text
The driveshaft that runs along the length of the chassis rotates when the car moves. You can manage the cables and wires in whatever manner you like but make sure that you keep them away from any rotating assemblies, including the driveshaft. If you don’t, then the rotating assemblies will pull on all the cables and the last 1-2 hours of your life will have been in vain.
```

## 4.2 Connecting the Brushless Motor to the VESC

Take three 4mm to 3.5mm bullet adapters.

![4mm to 3.5mm bullet adapters](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-36-02.png>)

Attach the adapters to the blue, yellow, and white wires of the Brushless Motor.

![Blue, yellow, white wires from Brushless Motor](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-36-12.png>)

The VESC also has three wires labelled `A`, `B`, and `C`.

### A -> WHITE

### B -> YELLOW

### C -> BLUE

![VESC MK III](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-36-28.png>)

Brushless Motor wires connected to the Bullet Adapters then connceted to the VESC wires. Then tuck the wires underneather the platform deck.

![alt text](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-36-39.png>)

### Important

``` text
After you flash the firmware on the VESC, if the vehicle runs backwards to the expected motion, simply swap the WHITE wire to “C” and BLUE wire to “A”.
```

## 4.3 Connecting the Battery with the VESC

Plug the charge adapter into the battery plug,

### Danger

``` text
MAKE SURE THAT RED/POWER AND BLACK/GROUND ARE CONNECTED CORRECTLY TO THE RED/POWER AND BLACK/GROUND OF THE CHARGE ADAPTER Fire will happen if this is plugged backwards.
```

![Charge adapter cable plugged into the Lipo battery](<Building_F1Tenth_Pics/IMG_4745.jpg>)

*Charge adapter cable plugged into the Lipo battery.*

Then, connect the other side of the charge adapter to a TRX to XT90 adapter. Reference image below.

![Plugging in the TRX to XT90 adapter](<PBuilding_F1Tenth_Pics/Screenshot from 2025-04-20 19-56-15.png>)

*Plugging in the TRX to XT90 adapter.*

After connecting the XT90 connections between the battery and the VESC (the yellow connectors) This will connect the battery and the VESC. Please reference the image below.

![Battery connected to the VESC](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 20-08-39.png>)

*Battery connected to the VESC.*

Finally, connect the battery and the Powerboard. This is done by connecting the 4-pin connector to the Powerboard. Reference the image below.

![Battery and Powerboard connection](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 20-01-45.png>)

## 4.4 Connecting the NVIDIA Jetson Orin Nano with the Powerboard

The NVIDIA Jetson Orin needs to be connected to the powerboard. Use the barrel jack to pig tail connector. The board uses a 2.5x5.5mm power jack (MFN: PJ-036BH-SMT-TR). It is an unfortunate fact of life that the connections for barrel jacks are not standarized. For the specific barrel jack on this board, the center pin is POWER. Do not plug in a power supply whose center pin is ground. Connect one of the ends of the cable with GND on the powerboard, the other one with the 12V connector. Afterwards you can plug in the barrel jack in the NVIDIA Jetson Orin. (Reference the red box in the image below)

![NVIDIA Jetson power supply connected with the powerboard](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 20-17-18.png>)

*NVIDIA Jetson power supply connected with the powerboard.*

## 4.5 Lidar Connection

The lidar comes with two very long cables. We are going to try out best to manage them. By tucking them under the Platform Deck.

![Storing the Lidar Cable under the Platform Deck](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 20-28-35.png>)

*Storing the USB Lidar Cable in front of the Lidar*

Using a twist tie, rubber band, or zip tie, gather the majority of the cables on each side. Then connect the Lidar to the NVIDIA Jetson. If using the UTM-30LX, plug the USB into one of the ports of the NVIDIA Jetson USB hub. If you are using a 10LX, plug it into the ethernet port of the Jetson Orin Nano.

Then its time to provide the energy connection for the Lidar. The other Lidar cable has a white connection, disconnet the **BROWN** (**POWER**) and **BLUE** (**GROUND**) wires from the white connector and connect to one of the 12V terminal blocks on the Powerboard. (Reference image below)

**Danger**

``` text
BROWN is POWER and BLUE is GROUND.* DO NOT MIX THESE UP OTHERWISE YOU WILL FRY YOUR VERY EXPENSIVE LIDAR. And then life will be very very sad. When in doubt, check the side of the Hokuyo. It will list out the correspondence of each wire.
```

Lidar power is plugged into the terminal block with Brown to Power and Blue to Ground.

![Lidar powered by Powerboard](<Building_F1Tenth_Pics/Screenshot from 2025-04-20 20-30-09.png>)

## 4.6 Attaching the PPM Cable

Now we are going to connect the PPM (Pulse-Position Modulation) cable to the Servo. The PPM cable connects the Servo to the VESC, which we installed on the Upper Level Chassis later.

## 4.6.1 Using PPM cable with servo connector

**Note:** that PPM has a white end and a black end.

![PPM cable](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-38-29.png>)

Take 3 header pins

![Header pins](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-38-38.png>)

Connect the 3 header pins to the **servo cable** on the Traxxas chassis.

![Header pin connected to Servo cable](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-54-23.png>)

Connect the PPM cable with the servo wire.

### Danger

```text
BROWN is GROUND. It should be connected to the BLACK wire of the Servo Cable. Make sure the polarity of the PPM cable to servo is correct.
```

![PPM cable connected to Servo cable](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-38-56.png>)

Now you can put everything together and plug it into the PPM slot on the VESC.

![PPM cable plugged into VESC](<Building_F1Tenth_Pics/Screenshot from 2025-03-13 16-39-04.png>)

## 4.6.2 Using PPM cable WITHOUT servo connector (NOT OPTIMAL)

If you are unable to find the PPM to servo cable you can buy a JST PH 2.0mm 3 Pin Male connectors and splice the JST PH connector wires with the servo wires from the Traxxas chassis. This can be done by cutting and stripping the servo wires. Then use th digram below to twist the wires to gether and heat shrink each individual wire to prevent short circuiting.

The color of these connectors can depend on the PPM connector that is purchased. On the VESC each pin for the PPM is labelled and the PPM connector has a specific direction that it has to be plugged into the VESC. Since each pin is labelled you can trace the coresponding pin to the color of wire on the PPM connector and then attach that to the correct servo wire.

**Note:** The servo wire is **Black** for **ground**, **red** for **positive**, and **white** for **signal**.

To connect these wires you strip 2 cm of coding off over each wire you are splicing and then slide a 3 cm piece of heat shrink over the PPM wire and push it down the wire so you are able to twist the 2 pieces of wire together. Then use a heat gun to shrink the heat shrink around the twisted wires securing them in place. Repeat this process for all 3 wires.

![Heat shrinking the PPM and Sservo wires together](<Building_F1Tenth_Pics/Screenshot from 2025-04-21 09-33-21.png>)

Finally, connect the PPM connector to the VESC. Please reference image below.

![Connect the PPM connector to the VESC](<Building_F1Tenth_Pics/Screenshot from 2025-04-21 09-45-05.png>)

## 7. Final Touches

Almost there!

Connect a micro USB from the the USB port on Jetson Orin Nano to the micro USB port on the VESC (Close to the PPM port).

![Micro USB plugged into Jetson and VESC](<Building_F1Tenth_Pics/Screenshot from 2025-04-21 09-47-55.png>)

## 8. Voila

Your final vehicle should look like the following:

### NEED TO ADD AN OVERALL PICTURE

Now we’re ready to start driving!
