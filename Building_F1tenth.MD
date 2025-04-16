# Building F1tenth

# 1. Lower Level Chassis

We begin with setting up the Lower Level chassis. We will be removing the internal parts of the Traxxas and repopulate it with our own parts. The complete process for the first hardware part can be watched in this video tutorial too.

[Lower Level Chassis](https://youtu.be/IoWHUGFfrRE)

## 1. Removing Traxxas Stock Components
Take the Traxxas from its box. Remove the four Body Clips to remove the Body so you are left with this:

![alt text](<../Pictures/F1Tenth Build/IMG_4620.jpg>)

Traxxas chassis with body shell removed.¶

We are going to remove several electrical assemblies including the speed controller and reciver. The only component which we will not be removing is the Servo and the Drive Motor, which is the little black box in the right corner and the large blue motor. There are three hex keys that come with the Traxxas. You will use this to remove and/or install almost all of the screws on the chassis. You may want to have a bowl or container of sorts nearby to hold all the screws that you’ll be removing as these screws will be needed later.

Start by removing the plastic side bars. THese holes will be used as mounting points later.

![alt text](<../Pictures/F1Tenth Build/IMG_3285.jpg>)

Next, unscrewing the top of the black Receiver Box.

![alt text](<../Pictures/F1Tenth Build/IMG_3286.jpg>)

Once the top is open, you will see the Receiver labelled “TQi”. Disconnect all of the wires going to the receiver. Move the wires out of the way. The Receiver is attached to bottom of the Receiver Box with double sided tape. Carefully, but firmly, pry the Receiver from the Receiver Box and remove.

![alt text](<../Pictures/F1Tenth Build/IMG_3288.jpg>)
Inside of Receiver Box.¶

This will expose the two screws which mount the Receiver box to the chassis. Unscrew the screws to remove the Receiver Box.

![alt text](<../Pictures/F1Tenth Build/IMG_3287.jpg>)

Screws are visible once the Receiver Box has been removed.¶

You may find a screw driver and pair of pliers useful in removing the Antenna Tube.

Then, remove the Traxxas ESC, the blue box labelled “VXL-3s”, by unscrewing the two screws that attach the ESC to the chassis. Disconnect the wires (white, yellow, and blue) that go from the ESC to the Brushless Motor. The wires are connected by what are called bullet connectors. You can safely pull the wires apart by grabbing each side of the connector and pulling.

Your final result should look as follows.

![alt text](<../Pictures/F1Tenth Build/IMG_3295.jpg>)

## 2. Attaching the Standoffs
First, remove the two Nerf Bars (black handles) located on either side of the chassis. There are 4 screws that hold each Nerf Bar in place. The screws are accessible from underneath the chassis.

Attach three M3 screws and three 45mm M3 FF standoffs into the chassis as shown.

![alt text](<../Pictures/F1Tenth Build/IMG_3295.jpg>)
Location of Standoffs.¶

Use M3 screws from underneath the chassis to secure the standoffs. Arrange the standoffs so that two standoffs go on the Motor side and 1 go on the battery side. This arrangement allows for better access to the battery. You may want to use thread-locking fluid to secure these standoffs as the vibrations of the car during movement may loosen them over time.

## 3. Setting Up the Battery
**Danger**
```
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

![alt text](<../Pictures/F1Tenth Build/IMG_3295.jpg>)


**Lipo battery on Lower Level Chassis.**


![alt text](<../Pictures/F1Tenth Build/IMG_3295.jpg>)
Lower Level Chassis with installed Brushless Motor. The Standoffs in the picture will be explained in the next section.

# 2. Autonomy Elements
In the second part of the hardware setup we start preparing the autonomy elements for our F1TENTH car. The complete process for the second hardware part can be watched in this video tutorial too.

[F1tenth Autonomy Elements](https://youtu.be/L-V-0zzkl10)

## 1. Preparing the NVIDIA Jetson Orin Nano
When you purchase a NVIDIA Jetson Orin Nano, it is attached to small plastic development board. In order to use it on the car, you will need to unscrew the Jetson Orin Nano and its Wi-Fi antenna from the development board. First of all unbox your NVIDIA Jetson Orin Nano.

![alt text](<../Pictures/F1Tenth Build/IMG_4639.jpg>)
Unpackage the NVIDIA Jetson Orin Nano

When you look on the Jetson Orin Nano from above you will see four screws (see red circles in the image). Please unscrew all of these 4 screws.

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 15-45-31.png>)
Remove the screws that attach the plastic board to the NVIDIA Orin Nano

Afterwards you can turn the Jetson Orin Nano on the other side. You will see the plastic development board is still attached because of the two antenna cables.

![alt text](<../Pictures/F1Tenth Build/IMG_4645.jpg>)
Plastic development board attached to the NVIDIA Orin Nano

Also remove the srew and inserct SSD card then put back in the screw to secure it.

The two antenna cables are clipped to the Jetson NX. You have to unclip both of them. You can either use your fingers are lift them with a flat screwdriver.

![alt text](<../Pictures/F1Tenth Build/IMG_4646.jpg>)
Unclip the two antennas from the NVIDA Jetson Orin Nano

Afterwards your NVIDA Jetson Orin Nano is seperated from the developer board. This is the version you can now screw to the platform deck.

![alt text](<../Pictures/F1Tenth Build/IMG_4647.jpg>)
Nvidia Jetson Orin Nano demounted from the developer board

## 2. Preparing the WiFi Antenna
In the next step we are providing both Wifi Antennas so we can mount them in the later steps quick and easy. First of all unpackage your antennas and demount the cables from the antennas. Remove the two brass-colored nuts holding the antennas to the L-shaped bracket, and then remove the two antennas from the bracket. (M3X10mm)

![alt text](<../Pictures/F1Tenth Build/IMG_4648.jpg>)
Demounted Wifi antennas

Afterwards we need to Screw the Standoffs onto the antenna bracket. Using a Phillips screwdriver, thread the two screws you saved earlier completely into the bracket as pictured below. Attach two M3 FF 45mm standoffs to the opposite ends of the screws and hand-tighten them until they won’t turn anymore. Use the pliers to tighten the standoffs more while you hold the head of the screw in place using the screwdriver.

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 15-51-00.png>)
Screwing standoffs onto the bracket.

Once you’ve done these steps, place the antennas and washers back into the bracket, and tighten the brass nuts onto the threaded connectors again. It helps to use two pairs of pliers: one to hold the rear nuts in place and another to unscrew the nuts on the end with the antenna connectors.

![alt text](<../Pictures/F1Tenth Build/IMG_4652.jpg>)

Thighten the nuts from the L-shaped bracked.¶

We can now move on to mounting all of the autonomy elements onto the Upper Level Chassis in the next section. Second accomplishment completed.

# 3. Upper Level Chassis
In the third part we’re going to assemble the upper level chassis and mount the important components. The complete process for the third hardware part can be watched in this video tutorial too.
[F1tenth Upper Level Chassis](https://youtu.be/L-V-0zzkl10)

Place the **Platform Deck** so it’s facing you like this. The **Platform Deck** is the laser cut piece.

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 14-46-53.png>)

To make things easier to follow, we define **Front, Rear, Away,** and **Towards** like above.

**Important**
```
This piece is not symmetric. Notice in the figure above that the big M5 VESC mounting holes marked in yellow are not centered. The holes need to be skewed TOWARDS to you.
```

The following image shows the five components that we will be mounting on the Platform Deck.

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 14-44-43.png>)
Locations of parts to be mounted.

## 1. Mounting the VESC
Place the VESC on the Platform Deck so that the power wires are facing AWAY from you and the three cables labelled A, B, and C are facing TOWARDS you.

![alt text](<../Pictures/F1Tenth Build/IMG_4642.jpg>)
VESC placed in correct position on Platform Deck.

Flip the Platform Deck and the VESC over and use two M5 screws mounted diagonal from each other to attach the VESC to the Platform Deck, like shown below.

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 15-00-35.png>)
Mounting holes for Powerboard and VESC. Note that this is view of the bottom of the Platform Deck.

## 2. Mounting the Antenna
After the VESC we mount the antenna standoffs+cables to the rear of the VESC. The reason for that is that we want to lay the antenna cables beneath the powerboard and connect it afterwards directly to the NVIDIA Jetson NX before mounting it. Use the M3 screw to mount the antenna standoffs+cable.

![alt text](<../Pictures/F1Tenth Build/IMG_4653.jpg>)
Mounted Antenna on the platform deck.

Afterwards you can directly attach the black antennas to the antenna mount. Just as you demounted the antenna rotate them back to the antenna mount.

![alt text](<../Pictures/F1Tenth Build/IMG_4654.jpg>)
Attach the antenna mount to the Antenna.

## 3. Mounting the NVIDIA Jetson NX
Now its time to mount the NVIDIA Jetson NX. Before we mount the Jetson please connect the antenna cables first. Flip the Jetson around and clip both antenna cables to the antenna connectors on the Jetson.

![alt text](<Pictures/F1tenth Build/ulchassisNX_04.jpeg>)
Connect the antenna cables to the Jetson NX.

Afterwards we need to install the M3 standoffs for the Jetson on the Platform deck. Screw the standoffs to the platform deck to the specific NVIDA Jetson NX mount holes. Thread the M3 screw from underneath the Platform Deck up and secure with a 25mm standoff.

![alt text](<Pictures/F1tenth Build/ulchassisNX_05.jpeg>)
Install the standoffs for the Nvidia Jetson.

Now you can place the Jetson NX on the mounted standoffs. Use the 4 main holes on top of the Jetson to mount the Jetson to the platform deck with M3 screws. Then, Secure the Powerboard to the 25mm standoff with a M3 x 8mm screw.

![alt text](<Pictures/F1tenth Build/ulchassisNX_06.jpeg>)
Mount the Nvidia Jetson NX to the platform deck.

## 4. Mounting the Powerboard
The image above shows the three holes used to mount the Powerboard. Only three of the Powerboard mounting holes are used. Flip the Platform Deck with the VESC attached to it back over so the VESC is facing up. Attach the Powerboard to the Platform deck by using the M3 screws that were removed from the chassis in the Lower Level Chassis section. Thread the M3 screw from underneath the Platform Deck up and secure with a 25mm standoff. Then, Secure the Powerboard to the 25mm standoff with a M3 x 8mm screw.

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 16-19-13.png>)
Side view of Powerboard mounted on Platform Deck.

![alt text](<../Pictures/F1Tenth Build/IMG_4655.jpg>)

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 17-20-13.png>)

### The lines on the top on the power board are positive
Top view of Powerboard mounted on Platform Deck. The green terminal blocks are facing the FRONT of the car.

There should be a gap between the Powerboard and the VESC.

![alt text](<../Pictures/F1Tenth Build/IMG_4658.jpg>)
Notice there is space between the VESC and the Powerboard.

After installing the powerboard your upper level should look like this.

![alt text](<Pictures/F1tenth Build/ulchassisNX_07.jpeg>)
Platform deck with Jetson NX, VESC, Powerboard and antenna.

## 5. Mounting the Lidar
The last component to mount is the lidar. Here, we use the Hokuyo UTM-30LX. The mounting holes for the Hokuyo UST-10LX are slightly different.

![alt text](<../Pictures/F1Tenth Build/Screenshot from 2025-03-13 16-31-47.png>)
Lidar mounting holes.

Use the appropriate mounting holes for your lidar.

Use four M3 screws to mount from underneath.

![alt text](<Pictures/F1tenth Build/ulchassis10.jpeg>)
Lidar mounted on Platform Deck.

The upper level chassis is complete and we’re ready to assemble everything!

![alt text](image.png)

# 4. Putting it all together
Now that we have the autonomy elements attached to the upper level chassis, we are going to attach the upper level chassis to the lower level chassis. This part may be a tad unwieldy due to the amount of wires and cables that have to be contained. The complete process for the last hardware part can be watched in this [video tutorial](https://youtu.be/vNVFCq688ck) too.


## 1. Mounting the Upper Level Chassis to the Lower Level Chassis¶
Gently place the upper level chassis on top of the standoffs of the lower level chassis. The VESC should be towards the back of the car. Thread the PPM cable from the lower level chassis, through one of the Platform Deck slot.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-35-24.png>)
Upper Level Chassis gently placed on top of Lower Level Chassis.¶

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-35-50.png>)
Lidar cables carefully arranged on top of battery.¶

Use three M3 x 10mm (these are the ones that were removed from the chassis during the Lower Level Chassis build section) screws to attach the Platform Deck to the standoffs on the lower level chassis.

It may be useful to use a zip tie to secure the USB cable from the lidar to the platform.

Danger

The driveshaft that runs along the length of the chassis rotates when the car moves. You can manage the cables and wires in whatever manner you like but make sure that you keep them away from any rotating assemblies, including the driveshaft. If you don’t, then the rotating assemblies will pull on all the cables and the last 1-2 hours of your life will have been in vain.

## 2. Connecting the Brushless Motor to the VESC¶
Take three 4mm to 3.5mm bullet adapters.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-36-02.png>)

4mm to 3.5mm bullet adapters.¶

Attach the adapters to the blue, yellow, and white wires of the Brushless Motor.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-36-12.png>)

*Blue, yellow, white wires from Brushless Motor.*

The VESC also has three wires labelled `A`, `B`, and `C`.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-36-28.png>)

*VESCMKIII.*

Now, we are going to connect these to the VESC. This part is a tad tricky.

**A -> WHITE**

**B -> YELLOW**

**C -> BLUE**

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-36-39.png>)

Brushless Motor wires connected to the Bullet Adapters then connceted to the VESC wires.¶

**Important**

```
After you flash the firmware on the VESC, if the vehicle runs backwards to the expected motion, simply swap the WHITE wire to “C” and BLUE wire to “A”.
```

## 3. Connecting the Battery with the VESC¶
Plug the charge adapter into the battery plug,

**Danger**

```
MAKE SURE THAT RED/POWER AND BLACK/GROUND ARE CONNECTED CORRECTLY TO THE RED/POWER AND BLACK/GROUND OF THE CHARGE ADAPTER Fire will happen if this is plugged backwards.
```

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-36-50.png>)

*Charge adapter cable plugged into the Lipo battery.*

Then, connect the other side of the charge adapter to a TRX to XT90 adapter.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-37-01.png>)

*Plugging in the TRX to XT90 adapter.*

It should look like this:

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-37-10.png>)

*TRX to XT90 adapter installed.*

After connecting the batter the car should look like this.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-37-21.png>)

*Battery connected to the VESC.*

## 4. Connecting the NVIDIA Jetson NX with the VESC¶
The NVIDIA Jetson NX needs to be connected to the powerboard. Use the barrel jack to pig tail connector. The board uses a 2.5x5.5mm power jack (MFN: PJ-036BH-SMT-TR). It is an unfortunate fact of life that the connections for barrel jacks are not standarized. For the specific barrel jack on this board, the center pin is POWER. Do not plug in a power supply whose center pin is ground. Connect one of the ends of the cable with GND on the powerboard, the other one with the 12V connector. Afterwards you can plug in the barrel jack in the NVIDIA Jetson NX.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-37-38.png>)

*NVIDIA Jetson power supply connected with the powerboard.*

## 5. Lidar Connection
The lidar comes with two very long cables. We are going to try out best to manage them. Split the two cables of the lidar and loop them under the slots on the Platform Deck.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-37-45.png>)

*Storing the USB Lidar Cable in front of the Lidar*

Using a twist tie, rubber band, or zip tie, gather the majority of the cables on each side. Then connect the Lidar to the NVIDIA Jetson. If using the UTM-30LX, plug the USB into one of the ports of the NVIDIA Jetson USB hub. If you are using a 10LX, plug it into the ethernet port of the Jetson NX.

Then its time to provide the energy connection for the Lidar. For the stripped cable side, insert the BROWN (POWER) and BLUE (GROUND) wires into one of the 12V terminal blocks on the Powerboard.

**Danger**

```
*BROWN is POWER and BLUE is GROUND.* DO NOT MIX THESE UP OTHERWISE YOU WILL FRY YOUR VERY EXPENSIVE LIDAR. And then life will be very very sad. When in doubt, check the side of the Hokuyo. It will list out the correspondence of each wire.
```

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-38-16.png>)

Lidar power is plugged into the terminal block with Brown to Power and Blue to Ground.

## 6. Attaching the PPM Cable¶
Now we are going to connect the PPM (Pulse-Position Modulation) cable to the Servo. The PPM cable connects the Servo to the VESC, which we will install on the Upper Level Chassis later.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-38-29.png>)

*PPM cable. Note that it has a white end and a black end.*

Take 3 header pins,

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-38-38.png>)

Header pins.¶

Plug it into the servo wires.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-54-23.png>)

Header pin connected to Servo cable of the Servo on the Traxxas chassis.¶

Connect the ppm cable with the servo wire.

Danger

BROWN is GROUND. It should be connected to the BLACK wire of the Servo Cable. Make sure the polarity of the PPM cable to servo is correct.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-38-56.png>)

*PPM cable connected to Servo cable.*

Now you can put everything together and plug it into the ppm slot on the VESC.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-39-04.png>)

*PPM cable plugged into VESC.*

The Lower Level chassis is now set up and we can move on to the autonomy elements. First accomplishment completed!

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-39-38.png>)

## 7. Final Touches
Almost there!

Connect a micro USB (here: the white cable) from the VESC to the USB hub.

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-39-53.png>)

*Micro USB plugged into the VESC. Plug the USB side into the USB hub.*

Finally, screw on the antennas included with the Jetson TX2 Kit to the Antenna Terminals.

## 8. Voila!
Your final vehicle should look like the following:

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-40-06.png>)

Now we’re ready to start driving!

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-40-18.png>)

**DEPRECATED: NVIDIA TX2 Setup**
Attach the two wires for the Jetson Wi-Fi antenna to the two gold-colored connectors near the fan connector on the heat sink (the order of the wires doesn’t matter). This can be a little tricky, so you might want to use a flathead screwdriver to ensure the connections are tight.  Don’t press too hard , however as you can easily damage the connectors if you use excessive force!

![alt text](<../Pictures/F1Tenth Build/RoboRacer_Pics/Screenshot from 2025-03-13 16-40-26.png>)