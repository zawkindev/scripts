import os

s = os.system

file_name = "powertop.service"

config = '''
[Unit]
Description=Powertop tunings

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/usr/bin/powertop --auto-tune

[Install]
WantedBy=multi-user.target
'''

s(f"touch {file_name}")

with open(file_name, "w") as f:
    f.write(config)

s("paru -Sy powertop")
s(f"sudo cp {file_name} /etc/systemd/system")
s(f"rm -rf {file_name}")
s(f"sudo systemctl enable {file_name}")
s(f"sudo systemctl start {file_name}")
