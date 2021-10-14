# MayorSecBackdoor
# Gatekeeper
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)
### Fully functioning, password protected, bind-type backdoor
![Gatekeeper](/images/backdoorlite.png)

This backdoor is a fully functioning bind shell and lite version of my full functioning Gatekeeper tool. It can be ran with Python or compiled to an exe and has full functioning command line access with Windows and Linux.

## Usage
Connect using Netcat after changing the port value to whatever you wish (default is 8180)

```nc ipaddr port```

Once connected you can utilize commands as normal.  If you wish to use Powershell commands, make sure to lead with 

```powershell <command here>```

This will execute the command.  Note that some Powershell functionality may crash the Netcat session requiring a reconnect.  

## Compilation
This tool can be ran on systems that have Python3 installed, or can be compiled to exe using Pyinstaller.  I recommend using the GUI version of Pyinstaller called "Auto Py to EXE" which allows for the easy addition of an exe icon for the application.  The included .exe is set to utilize port 8180.

