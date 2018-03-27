How to Download and Install the Twilio Package
These instructions cover installing Twilio on Windows, Macintosh and Linux computers.

Preface
Twilio works in several countries (the United States, Australia, the UK, and others) but, currently, full support outside of North America and Europe is not guaranteed. A list of supported countries is available on Twilio's site. Note that you'll have to scroll down to the "SMS Enabled Phone Numbers" section.

Background
In Python, developers usually use one of the two common utilities to automatically download, and setup the necessary folders and files: easy_install and pip.

easy_install comes with the setuptools Python library which comes standard with Python and pip comes with the pip library. easy_install and pip are executed in the terminal that can be used to install Python packages.

Preparation
Have you installed Python 2.7?
Having this version makes getting Twilio a lot easier. Open IDLE to find out what you have -- you should see something similar to this:

Python 2.7.9 (default, Jan 22 2015, 16:00:57) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.56)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
If you don't have 2.7, there are instructions that will show you how to install it (click the link!). If you already have an older version, the installer will gracefully replace it with this one. Ensure that all installation options, if you see any, are checked during that process.

Furthermore, make sure you are connected to the Internet and your Internet does not block the Python Package Index Server: https://pypi.python.org/pypi that easy_install and pip will connect in order to download Twilio.

Windows Instructions
Make sure your computer's PATH has Python added. This means that in the program Command Prompt you can type the words python and the system knows how to find the python.exe located in your system.

If your system does not have Python added to your PATH, it's suggested you reinstall Python and make sure to click on the option to install python to your system PATH when you customize your Python installation:

Also make sure that your account has Administrative access in order to be able to install programs on your Windows system. If you get permission errors, on Windows, you'll have to close your Command Prompt and open it again as an administrator by right-clicking on it and choosing the appropriate option
You can then either type easy_install twilio or pip install twilio to download and install Twilio
Macintosh and Linux Instructions
Macintosh and Linux systems will already have Python added in their system PATH.
Therefore the only step you need to take is to load up the Terminal application and type in sudo easy_install twilio and enter in your password to give easy_install permissions to write to your system folders.
If you want to install Twilio with pip, you may need to first install pip on your system because newer Macintosh systems and some Linux distributions may not come with pip installed.
Therefore, you should first install pip with sudo easy_install pip
You can then use pip to install Twilio with sudo pip install twilio
Install Verification
To check whether Twilio was properly installed, we enter the python command to enter the Python interpreter in the Command Prompt or Terminal application and type in these two commands:

import twilio
print(twilio.__version__)
If it prints a version number, you're all set!

Troubleshooting
Anaconda
If you have Anaconda installed on your Mac or PC, it comes with its own version of Python that is siloed from the version of Python that is included with IDLE. You may have installed Twilio to Anaconda's Python instead of IDLE's Python -- to find out whether or not you've done that, we suggest opening Spyder, Anaconda's alternative to IDLE, and trying an import twilio there. If that works, then feel free to do your programming for this assignment in Spyder instead of IDLE.
