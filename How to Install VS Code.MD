# How to Install Visual Studio Code

## Steps
- Downlaod Visual Studio
- Install Visual Studio
    - Terminal

## Download Visual Studio
Look up "VS code" in Google Chrome and access Visual Studio website

![alt text](<Pictures/VS_Code/Screenshot from 2024-04-05_10-12-26.png>)>)

## Install Visual Studio

**Start with ...**
```
sudo apt update
```
**Next ...**
```
cd Downloads
```
**Then ...**
```
ls
```
**This will list all of the downloads in folder**

*Example*
```
erickj1@darc-desktop-02:~/Downloads$ ls
code_1.87.2-1709912201_amd64.deb  debian-binary
code_1.88.0-1712152114_amd64.deb  sdkmanager_2.1.0-11660_amd64.deb
control.tar.xz                    ubuntu-20.04.6-desktop-amd64.iso
data.tar.xz
```
**Next ...**
```
sudo dpkg -i code_1.88.0-1712152114_amd64.deb
```
*Functions*
1. -i = install software packages
2. dpkg = Debian Package is a fundamental tool in the world of Linux package management. Primaily used to install, build, remove, and manage packages.

**Finally** use `code`  in terminal to open **VS code**