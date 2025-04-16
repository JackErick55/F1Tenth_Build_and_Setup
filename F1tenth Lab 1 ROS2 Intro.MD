# F1tenth Lab 1 ROS2 Intro

## Lab 1: Intro to ROS 2

## Learning Goals
- Getting familiar with ROS 2 workflow
- Understanding how to create nodes with publishers, subscribers
- Understanding ROS 2 package structure, files, dependenciees
- Creating launch files

## Before you start
It's highly recommended to install Ubuntu natively on your machine for developement in simulation. However, if it's impossible for you to do so, you can still use the simulation inside Docker containers. In the following instructions, if you have Ubuntu installed natively, ignore directions for using Docker.

## 1. Overview

The goal of this lab is to get you familiar with the ROS 2 workflow. You'll have the option to complete the coding segment of this assignment in either Python or C++. However, we highly recommend trying out both since this will be the easiest assignment to get started on a new language, and the workflow in these two languages are slightly different in ROS2 and it's beneficial to understand both.

In this lab, it'll be helpful to read these tutorials if you're stuck:

https://docs.ros.org/en/foxy/Tutorials.html

https://roboticsbackend.com/category/ros2/

## 2.1 Getting ready (Native Ubuntu)
Install ROS 2 following the instructions here: https://docs.ros.org/en/foxy/Installation.html.

Next, create a workspace:

```
mkdir -p ~/F1tenth/lab1_ws/src
cd lab1_ws
colcon build
```

Move on to *Section 3* once you're done.

## 2.2 Getting ready (Docker)
If you can't have Ubuntu installed natively, install Docker on your system following the instructions here: https://docs.docker.com/get-docker/. The documentation of Docker can be found [here](https://docs.docker.com/reference/).

Next, start a container with a bind mount to your workspace directory on your host system inside this repo by:
```
docker run -it -v <absolute_path_to_this_repo>/F1tenth/lab1_ws/src/:/F1tenth/lab1_ws/src/ --name f1tenth_lab1 ros:humble
```

<span style="color:red;">
Next, start a container with a bind mount to your workspace directory on your host system inside this repo by:

```
erickj1@darc-desktop-02:~/lab1_ws$ docker run -it -v /home/erickj1/F1tenth/lab1_ws/src/:/F1tenth/lab1_ws/src/ --name f1tenth_lab1 ros:humble
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.
```
Attempt to fix current error

**1. Docker Socket Permissions**:
- The error message indicates that Docker is unable to connect to the Docker daemon socket at `unix:///var/run/docker.sock`.

- This socket file controls communication between the Docker client and the Docker daemon.

- To resolve this, we need to ensure proper permissions for the socket.

**2. Fixing Docker Socket Permissions**:
- You can try the following solutions: 

**A. Change Group Ownership of Docker Socket**: 

- Run the following command to change the group ownership of the `/var/run/docker.sock`

    file:           
`sudo chown root:docker /var/run/docker.sock `
- This ensures that the Docker client has the necessary permissions to communicate with the Docker daemon. 

**B. Additional Permissions for ~/.docker Directory**: 
- Sometimes, additional permissions are needed if you’ve previously run Docker commands with `sudo`. 
- Execute the following commands to adjust permissions for the `~/.docker` 
directory:           
```
mkdir ~/.docker
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R 
```
 - Now try running Docker without `sudo`.

**3. Retrying the Docker Command**:
After making the above changes, try running your Docker command again:

```
docker run -it -v /home/erickj1/F1tenth/lab1_ws/src/:/F1tenth/lab1_ws/src/ --name f1tenth_lab1 ros:humble
```

Hopefully, this time it should work without permission issues.

<span style="color:white;">
This will create a workspace directory on the host at `<absolute_path_to_this_repo>/F1tenth/lab1_ws/src`. It'll create the container based on the official ROS 2 Foxy image, and give the container a name `f1tenth_lab1`. You'll then have access to a terminal inside the container.

`tmux` is recommended when you're working inside a container. It could be installed in the container via: `apt update && apt install tmux`. `tmux` allows you to have multiple `bash` session in the same terminal window. This will be very convenient working inside containers. A quick reference on how to use tmux can be found here. You can start a session with `tmux`. Then you can call different `tmux` commands by pressing `ctrl+B` first and then the corresponding key. For example, to add a new window, press `ctrl+B` first and release and press `c` to create a new window. You can also move around with `ctrl+B` then `n` or `p`.

A cheatsheet for the original tmux shortcut keys can be found here. To know about how to change the configuration of tmux to make it more useable (for example, if you want to toggle the mouse mode on when you start a tmux bash session or change the shortcut keys), you can find a tutorial here.

## 3: ROS 2 Basics
Now that we have the access to a ROS 2 environment, let's test out the basic ROS 2 commands. In the terminal, run:

```
source /opt/ros/humble/setup.bash
ros2 topic list
```
You should see two topics listed:
```
/parameter_events
/rosout
```
If you need multiple terminals and you're inside a Docker container, use `tmux`.

## 4: Creating a Package
**Deliverable 1**: create a package named `lab1_pkg` in the workspace we created. The package needs to meet these criteria:

- The package supports both `Python` and `C++`.
- The package needs to have the `ackermann_msgs` dependency.
- Both of these can be done by declaring the correct dependencies in `package.xml`.
- If declared properly the depencies could be installed using `rosdep`.
- Your package folder should be neat. You shouldn't have multiple 'src' folders or unnecessary 'install' or 'build' folders.

<span style="color:red;">**My Work**
```
ros2 pkg create --build-type ament_cmake ament_python --license Apache-2.0 <lab1_pkg>
```

## 5: Creating nodes with publishers and subscribers
**Deliverable 2**: create two nodes in the package we just created. You can use either `Python` or `C++` for these nodes.

The first node will be named `talker.cpp` or `talker.py` and needs to meet these criteria:

- `talker` listens to two ROS parameters `v` and `d`.
- `talker` publishes an `AckermannDriveStamped` message with the `speed` field equal to the `v` parameter and `steering_angle` field equal to the `d` parameter, and to a topic named `drive`.
- `talker` publishes as fast as possible.
- To test node, set the two ROS parameters through command line, a launch file, or a yaml file.

 The second node will be named relay.cpp or relay.py and needs to meet these criteria:

- `relay` subscribes to the `drive` topic.
- In the subscriber callback, take the speed and steering angle from the incoming message, multiply both by 3, and publish the new values via another `AckermannDriveStamped` message to a topic named `drive_relay`.

## 6: Creating a launch file and a parameter file
**Deliverable 3**: create a launch file `lab1_launch.py` that launches both of the nodes we've created. If you want, you could also set the parameter for the `talker` node in this launch file.

## 7: ROS 2 commands
After you've finished all the deliverables, launch the two nodes and test out these ROS 2 commands:
```
ros2 topic list
ros2 topic info drive
ros2 topic echo drive
ros2 node list
ros2 node info talker
ros2 node info relay
```

## 8: Deliverables and Submission
In addition to the three deliverables described in this document, fill in the answers to the questions listed in `SUBMISSION.md`.

We'll be using Github classroom throughout the semester to manage submissions for lab assignments. After you're finished, directly commit and push to the repo Github classroom created for you.

## 9: Grading Rubric
Correctly creating the package: 25 Points
Correctly creating the nodes: 25 Points
Correctly creating the launch file: 25 Points
Written questions: 25 Points