import os

s = os.system

path = "/etc/X11/xorg.conf.d/"
filename = "30-touchpad.conf"

config = """
Section "InputClass"
    Identifier "Elan Touchpad"
    Driver "libinput"
    MatchIsTouchpad "on"
    	Option "Tapping" "on"
	Option "ClickMethod" "clickfinger"
	Option "NaturalScrolling" "true"
EndSection
"""

s(f"touch {filename}")

with open(filename, "w") as f:
    f.write(config)

s(f"sudo cp {filename} {path}")
s(f"rm {filename}")
