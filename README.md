# NitroSense™ clone for ```Acer Nitro 16```
## Controls fan speed, gaming modes and undervolting on Linux. This application is intended for Acer Nitro 16 (Nitro AN16-51)

### Disclaimer:
* Secure Boot **IS** \* supported if you only use the ```acpi_ec``` package.
* Secure Boot is **NOT** \* supported if you want to control CPU voltage offsets using the ```msr-tools``` and ```amdctl``` packages.
* Using this application with other laptops may potentially damage them. Proceed at your discretion.

## Install of dependencies
### Nessessary:
- Ubuntu / Linux Mint:
  ```
  sudo apt-get install python3-pyqt5, python3-pyqt5.qtchart
  ```
 
- Fedora:
  ```
  sudo dnf install python3-qt5
  sudo dnf install python3-pyqtchart
  sudo dnf install dkms
  ```
### EC tools (acpi_ec)
```
  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
```

### Undervolt & Voltage control:
- Fedora:
```
sudo dnf install amdctl
```

### NVIDIA-POWERD
- After switching nitro modes \* **YOU MAY NEED TO RESTART NVIDIA-POWERD SERVICE IN ORDER TO DETECT NEW TGP** \*
```
sudo systemctl restart nvidia-powerd
``` 
- You can check the current GPU TGP via
```
nvidia-smi
```


## App install:
- ~~Get the latest [release](https://github.com/Packss/Linux-NitroSense16/releases)~~ no releases yet, try main
- ~~Run ```sudo ./install.sh``` from inside the folder~~

## Usage:
If installed just open it up from the applications menu!
If cloned proceed to the command line instructions.

### COMMAND LINE  
- ```sudo``` is required in order to access the Super I/O EC registers and apply undervolt offsets.
- From the command line run the main script as root:
  ```
  sudo python3 main.py
  ```


## Packages:
* ```Python Qt5``` -> [PyQt5](https://pypi.org/project/PyQt5/)
* ```acpi_ec``` -> [acpi_ec by musikid](https://github.com/musikid/acpi_ec/)
* ```msr-tools``` -> [msr-tools by intel](https://github.com/intel/msr-tools)
* ```acer module for RGB``` -> [acer-predator-module](https://github.com/JafarAkhondali/acer-predator-turbo-and-rgb-keyboard-linux-module)

### This is a fork of [NitroSense](https://github.com/snowyoneill/Linux-NitroSense), customized for ```Acer Nitro 16``` (especcially for Nitro AN16-51)
