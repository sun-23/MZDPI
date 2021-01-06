#!/usr/bin/env python3

# Write your code here :-)
from guizero import App, Text, PushButton
import subprocess as sub
import os

os.chdir("/home/pi/MZDPI/vga") # change directory
sub.call("ls", shell=True) # ls

app = App("ScreenModeChange",400,200)
app.bg = (251, 251, 208)

title_text = Text(app, "ScreenMode", 16, "black")

def changeToHdmi():
    sub.call('sudo ./mzdpi-vga-uninstall-rpi4', shell=True)
    print("hdmi")
    sub.call('sudo reboot', shell=True)

def changeToTft():
    sub.call('sudo ./mzdpi-vga-autoinstall-rpi4-offline', shell=True)
    print("tft")
    sub.call('sudo reboot', shell=True)

#def reboot():
#    sub.call('sudo reboot', shell=True)
#    print("reboot")

hdmi_button = PushButton(app, changeToHdmi, text="Select Hdmi")
tft_button = PushButton(app, changeToTft, text="Select 2.8 screen")
#reboot_button = PushButton(app, reboot, text="reboot")

description1_text = Text(app, "Click Select Hdmi Button to change to hdmi output", 12, "black")
description2_text = Text(app, "Click Select 2.8 screen Button to change to 2.8 screen", 12, "black")

app.display()