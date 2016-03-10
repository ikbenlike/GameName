add your login data in the quotes after "email =" and "password =" to let the script
login on your Discord account


installation:
-----------------------------------------------------------------------------------------------

then simply run the script with python 3, after installing the following modules:
on Unix-like systems:
pip3 install discord.py
pip3 install requests

(if not running as root, use put "sudo" in front of your commands)

on Windows systems:
navigate to the directory pip.exe is located (if it's not in your $PATH)
pip.exe install discord.py
pip.exe install requests

-----------------------------------------------------------------------------------------------

this script uses v0.9.2 of the Python module discord.py
tested with Python version 3.4


-----------------------------------------------------------------------------------------------

the folder py35 contains a version of the script compatible with api  v0.10.0
and withe python version 3.5.x

install v0.10.0 of the api with the following pip command:
pip install git+https://github.com/Rapptz/discord.py@async
(this requires git to be installed on your system)
