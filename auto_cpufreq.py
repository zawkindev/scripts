import os

s = os.system

s("git clone https://github.com/AdnanHodzic/auto-cpufreq.git")
s("cd auto-cpufreq && sudo ./auto-cpufreq-installer")
s("sudo auto-cpufreq --install")
s("rm -rf auto-cpufreq")
