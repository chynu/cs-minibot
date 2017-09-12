# Setting up a Raspberry Pi with WiFi

## Setting up a console

### Hardcoding a network configuration

1.  Download the latest version of Raspbian Lite from
    https://www.raspberrypi.org/downloads/raspbian/
2.  Extract the zip and follow the instructions at
    https://www.raspberrypi.org/documentation/installation/installing-images/README.md to write the
    image to an SD card using Etcher.
3.  Mount the filesystem partition and modify the following files:
```
# /etc/network/interfaces
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```
```
# /etc/wpa_supplicant/wpa_supplicant.conf
...
network={
    ssid="network ssid"
    psk="network password"
    proto=RSN
    key_mgmt=WPA-PSK
    pairwise=CCMP
    auth_alg=OPEN
}
```

### Using serial IO pins

### Using ethernet

*This method does not work with the Raspberry Pi Zero.*

Create an empty file called `ssh` in the BOOT drive.
Add `ip=169.254.1.1` to the end of `cmdline.txt`.
`ssh pi@169.254.1.1`

Remove `ip=169.254.1.1` to the end of `cmdline.txt`.
