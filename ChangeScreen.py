# Write your code here :-)
from guizero import App, Text, PushButton
import subprocess as sub
import os

os.chdir("/home/pi/MZDPI/vga") # change directory
sub.call("ls", shell=True) # ls

app = App("ScreenModeChange",200,200)
app.bg = (251, 251, 208)

title_text = Text(app, "ScreenMode", 16, "black")

def changeToHdmi():
    sub.call('sudo ./mzdpi-vga-uninstall-rpi4', shell=True)
    print("hdmi")

def changeToTft():
    sub.call('sudo ./mzdpi-vga-autoinstall-rpi4-offline', shell=True)
    print("tft")

def reboot():
    sub.call('sudo reboot', shell=True)
    print("reboot")

hdmi_button = PushButton(app, changeToHdmi, text="Select Hdmi")
tft_button = PushButton(app, changeToTft, text="Select 2.8 screen")
reboot_button = PushButton(app, reboot, text="reboot")

app.display()