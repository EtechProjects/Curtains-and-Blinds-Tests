File Must be placed in 'Home/Pi/' directory for the script to work since it reads and writes a config file. 
Also the AlarmPi script includes the curtians and blinds opening, this is not set up to work staraight from 
download it will take slight tweating so it works for you.

Required-
sudo apt-get install python-feedparser mpg123 festival
sudo mkdir -p /mnt/ram
echo "ramfs       /mnt/ram ramfs   nodev,nosuid,noexec,nodiratime,size=64M   0 0" | sudo tee -a /etc/fstab

credits-
Skiwithpete- creator of AlarmPi

