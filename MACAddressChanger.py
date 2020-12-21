import random
import os
import subprocess

def get_rand():
    return random.choice("abcdef0123456789")

def new_mac():
    new = ""
    for i in range(0,5):
        new += get_rand() + get_rand() + ":"

    new = get_rand() + get_rand()
    return new

print(os.system("ifconfig eth0 | grep ether | grep -oE [0-9abcdef:]{17}"))

subprocess.call(["sudo","ifconfig","eth0","down"])

new_m = new_mac()

subprocess.call(["sudo","ifconfig","eth0","hw","ether","%s"%new_m])
subprocess.call(["sudo","ifconfig","eth0","up"])