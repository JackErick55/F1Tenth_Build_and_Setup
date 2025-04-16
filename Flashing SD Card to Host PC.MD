# Flashing SD Card to Host PC

1. Use SD card to usb adapter.
2. Insert the original SD card and check the name of the device (usually mmcblkX or sdcX):

```
sudo fdisk -l
```

You might see:

```
Disk /dev/loop19: 271.98 MiB, 285192192 bytes, 557016 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/sda: 116.06 GiB, 124621160448 bytes, 243400704 sectors
Disk model: MassStorageClass
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: B3A4E828-DCD1-475A-9379-9458E1448E62

Device       Start       End   Sectors   Size Type
/dev/sda1  3057664 243398655 240340992 114.6G Linux filesystem
/dev/sda2     2048    264191    262144   128M Linux filesystem
/dev/sda3   264192    265727      1536   768K Linux filesystem
/dev/sda4   266240    331007     64768  31.6M Linux filesystem
/dev/sda5   331776    593919    262144   128M Linux filesystem
/dev/sda6   593920    595455      1536   768K Linux filesystem
/dev/sda7   595968    660735     64768  31.6M Linux filesystem
/dev/sda8   661504    825343    163840    80M Linux filesystem
/dev/sda9   825344    826367      1024   512K Linux filesystem
/dev/sda10  827392    958463    131072    64M EFI System
/dev/sda11  958464   1122303    163840    80M Linux filesystem
/dev/sda12 1122304   1123327      1024   512K Linux filesystem
/dev/sda13 1124352   1255423    131072    64M Linux filesystem
/dev/sda14 1255424   2074623    819200   400M Linux filesystem
/dev/sda15 2074624   3056639    982016 479.5M Linux filesystem
```
2. Now you have to unmount the device:

```
sudo umount /dev/sda
```

3. Create a folder to put the image in

Example: 
```
mkdir SDCardBackups
```

4. Now use the dd (Disk Destroyer) command

```
sudo dd if=/dev/sda of=~/SDCardBackups/f1tenth-driver-stack.img bs=1M status=progress
```
5. Eject disk using
```
sudo eject /dev/sda
```
- `if=` is where the sd card image is loacted
- `of=` is where you want to save the image that is on the sd card

## Flashing a SD card from Host PC to SD card

```
sudo dd if=~/SDCardBackups/f1tenth-driver-stack.img of=/dev/sda bs=1M status=progress
```

Then use `sudo eject /dev/sda` to eject the disk.


#### Note

- `if=` is where the image is loacted
- `of=` is where you want to save the image to. (Example: SD card --> /dev/sda)