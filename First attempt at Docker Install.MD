# How to Install Docker

## Start by Setting up the Repositories
In a terminal start by ubdating the system `sudo apt update`.

Next Docker requires a few dependencies
```
sudo apt install apt-transport-https ca-certificates curl gnupg lsb-release
```
Next we need to add Docker's gpg ket to ensure the integrity of the packages you are about to download 
```
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

```
Now let's set up the Docker stable repository by running
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
Next refresh the package list by running `sudo apt update` again. With the repository set up we can now install the Docker engine.

## Install Docker Engine
Start by running
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
This concludes the installation process of Docker is now installed the service has been started and is set to automatically initiate on boot. 

Furthermore, you can verify that the status of the Docker service by using the following command `sudo systemctl is-active docker`to ensure that Docker is installed and running correctly `active`

Also run `sudo docker hello-world`