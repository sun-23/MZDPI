    for not rpi4
    
    cd ~/

    git clone https://github.com/sun-23/MZDPI.git

    cd MZDPI/vga

    sudo chmod +x mzdpi-vga-autoinstall-online

    sudo ./mzdpi-vga-autoinstall-online

    sudo reboot
    
    for rpi4
    
    cd ~/

    git clone https://github.com/sun-23/MZDPI.git

    cd MZDPI/vga
    sudo chmod +x mzdpi-vga-uninstall-rpi4
    sudo chmod +x mzdpi-vga-uninstall
    
    /---------------------/
    sudo chmod +x mzdpi-vga-autoinstall-rpi4-online

    sudo ./mzdpi-vga-autoinstall-rpi4-online
    /---------------------/
    
    or 
    
    /---------------------/
    sudo chmod +x mzdpi-vga-autoinstall-rpi4-offline

    sudo ./mzdpi-vga-autoinstall-rpi4-offline
    /---------------------/

    sudo reboot
    
    screen 2.8inch geekworm rpi 60fps 640x480 
    see. https://raspberrypiwiki.com/2.8_inch_Touch_Screen_for_Pi_zero
    see. https://th.aliexpress.com/item/32908424504.html?spm=a2g0o.cart.0.0.754e3c004vFC77&mp=1
    
    
    or use python app for rpi4
    open termianl and type following commands
    
    python3 ./path/ChangeScreen.py
