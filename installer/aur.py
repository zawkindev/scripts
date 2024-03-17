import os

p = os.path
s = os.system

current_dir = os.getcwd()

s("sudo pacman -Sy git wget curl")

# install aur helper
if p.exists(p.expanduser("~/.temp/")):
    s("rm -rf ~/.temp/paru")
else:
    s("mkdir -p ~/.temp")

s("git clone https://aur.archlinux.org/paru ~/.temp/paru")
s(f"cd ~/.temp/paru && makepkg -si && cd {current_dir}")
