#!/usr/bin/python3
# (c) J~Net 2026
#
# python3 raw-test.py
#

from escpos.printer import File
from datetime import datetime

printer="/dev/usb/lp0"

p=File(printer)

p.set(
    align='center',
    bold=True,
    width=2,
    height=2
)

p.text("PT210 TEST\n")

p.set(
    align='left',
    bold=False,
    width=1,
    height=1
)

p.text(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
p.text("\n")
p.text("Python ESC/POS working\n")
p.text("USB-C thermal printer\n")

p.qr("https://jnetai.com")

p.text("\n\n")
p.cut()

print("Print complete")

