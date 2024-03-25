import os

s = os.system

evremap_toml="""
device_name = "AT Translated Set 2 keyboard"

[[dual_role]]
input = "KEY_CAPSLOCK"
hold = ["KEY_LEFTCTRL"]
tap = ["KEY_CAPSLOCK"]
"""

evremap_service = """
[Service]
WorkingDirectory=/
ExecStart=bash -c "/usr/bin/evremap remap /etc/evremap.toml -d 0"
Restart=always

[Install]
WantedBy=multi-user.target
"""


s("sudo rm -rf /usr/lib/systemd/system/evremap.service")
s("sudo rm -rf /etc/evremap.toml")

s("paru -Sy evremap-git")

s("touch evremap.toml")
s("touch evremap.service")

with open("evremap.toml","w") as f:
    f.write(evremap_toml)

with open("evremap.service","w") as f:
    f.write(evremap_service)


s("sudo cp evremap.service /usr/lib/systemd/system/")
s("sudo cp evremap.toml /etc")
s("sudo systemctl daemon-reload")
s("sudo systemctl enable evremap.service")
s("sudo systemctl start evremap.service")

s("rm -rf evremap.service")
s("rm -rf evremap.toml")
