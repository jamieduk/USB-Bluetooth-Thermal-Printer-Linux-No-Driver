#!/usr/bin/python3
# (c) J~Net 2026
#
# https://jnet.forumotion.com/t2191-usb-thermal-printer-linux-bash-plus-no-driver-required#3367
#
# ESC/POS QR Adjustable Printer Tool (USB PT210)
# size modes: tiny/medium/big/huge/custom
# alignment: left/center/right

from escpos.printer import File
from datetime import datetime

printer="/dev/usb/lp0" # Change if different!

def get_size():
    print("\nQR SIZE OPTIONS")
    print("1) tiny")
    print("2) medium")
    print("3) big")
    print("4) huge")
    print("5) custom")
    c=input("Select size: ")
    if c=="1":
        return 2
    if c=="2":
        return 4
    if c=="3":
        return 6
    if c=="4":
        return 8
    if c=="5":
        return int(input("Enter custom size (1-10): "))
    return 2

def get_align():
    print("\nALIGNMENT OPTIONS")
    print("1) left")
    print("2) center")
    print("3) right")
    c=input("Select align: ")
    if c=="1":
        return "left"
    if c=="2":
        return "center"
    if c=="3":
        return "right"
    return "center"

size=get_size()
align=get_align()

p=File(printer)

p.text("jnetai.com\n\n")

p.set(
    align=align,
    bold=False,
    width=1,
    height=1
)


p.qr(
    "https://jnetai.com",
    size=size,
    center=True
)

p.text("\n\n")
p.cut()

print("Print Complete!")
