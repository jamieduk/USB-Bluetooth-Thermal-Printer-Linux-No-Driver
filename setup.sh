python3 -m venv venv
source venv/bin/activate

# Install deps (once)
sudo apt update -y
sudo apt install -y python3-pip python3-venv

# For printing...
pip install python-escpos pyusb pillow
