## NitroSense™ clone for ```AN515-46-R5WF```
### Controls fan speed, gaming modes and undervolting on Linux. This application is intended for Acer Nitro 5 AN515-46 model.

![Predator Sense](LinuxPredatorSense.png)

## Disclaimer:
* Secure Boot **IS** \* supported if you only use the ```acpi_ec``` package.
* Secure Boot is **NOT** \* supported if you want to control CPU voltage offsets using the ```msr-tools``` and ```undervolt``` packages.
* Using this application with other laptops may potentially damage them. Proceed at your discretion.

## Install:
- From the command line
```
git clone https://github.com/Packss/Linux-NitroSense/
cd Linux-NitroSense/
``` 

## Usage:
### COMMAND LINE  
 - ```sudo``` is required in order to access the Super I/O EC registers and apply undervolt offsets.
  - From the command line run the main script as root:
  ```
  sudo python3 main.py
  ```

_[OPTIONAL]_
- Make sure to set the ```UNDERVOLT_PATH``` in ```main.py``` to the appropriate location of the undervolt package.
  - If you installed without sudo you can find where undervolt is located by doing.
    ```
    which undervolt
    ```
  - Next set ```COREOFFSET``` and ```CACHEOFFSET``` to the mV that you determined to be stable via throttlestop on windows.

### ICON
 - Alternatively you can copy the .desktop file to your applications folder and launch the program via it's icon.
  - Open ```nitro-sense.desktop``` in a text editor.
  - Set ```<path_to_NitroSense>``` to the directory where you downloaded this project.
  ```
  Exec=sh -c "pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY sh -c 'cd <path_to_NitroSense> && python3 main.py'"
  Icon=<path_to_NitroSense>/app_icon.ico
  ```
  - Copy the file to the application directory
  ```
  sudo cp nitro-sense.desktop /usr/share/applications/
  ```
  - Now launch via the application and on initialization it will prompt for the user password.

### NVIDIA-POWERD
- After switching nitro modes \* **YOU MAY NEED TO RESTART NVIDIA-POWERD SERVICE IN ORDER TO DETECT NEW TGP** \*
```
sudo systemctl restart nvidia-powerd
``` 
- You can check the current GPU TGP via
```
nvidia-smi
```

## Dependencies:
* Ubuntu / Linux Mint:
  ```
  sudo apt-get install python3-pyqt5, python3-pyqt5.qtchart
  ```

  ```
  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```

  ```
  [OPTIONAL]
  pip install git+https://github.com/georgewhewell/undervolt.git
  sudo apt-get install msr-tools
  ```
* Fedora:
  ```
  sudo dnf install python3-qt5
  sudo dnf install python3-pyqtchart
  ```
  Make sure SecureBoot is off.

  ```
  sudo dnf install dkms
  
  git clone https://github.com/musikid/acpi_ec/
  cd acpi_ec
  sudo ./install.sh
  modprobe acpi_ec
  sudo cat /dev/ec #confirm access to EC
  ```

  ```
  [OPTIONAL]
  pip install git+https://github.com/georgewhewell/undervolt.git
  sudo dnf install msr-tools
  ```

Packages:
* ```Python Qt5``` -> [PyQt5](https://pypi.org/project/PyQt5/)
* ```acpi_ec``` -> [acpi_ec by musikid](https://github.com/musikid/acpi_ec/)
* ```undervolt``` -> [Undervolt by georgewhewell](https://github.com/georgewhewell/undervolt)
* ```msr-tools``` -> [msr-tools by intel](https://github.com/intel/msr-tools)

## This is a fork of [PredatorSense by snowyoneill](https://github.com/snowyoneill/Linux-PredatorSense), customized for ```AN515-46-R5WF```

## Changelog:

Nothing yet
