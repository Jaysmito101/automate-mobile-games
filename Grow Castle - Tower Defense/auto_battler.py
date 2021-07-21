import os
import time
import time
from PIL import Image

while True:
	os.system("adb exec-out screencap -p > screen.png")
	im = Image.open("screen.png")
	pix = im.load()
	if(pix[1840, 1120] != (206, 199, 180, 255) ):
		continue
	os.system("adb shell input tap 1840 1120")
	time.sleep(1)
	file_name = "ss_"+time.strftime("%H:%M:%S")+".png"
	file_name = file_name.replace(":", "-")
	print("Tapped")
	os.system("adb exec-out screencap -p > ss\\" + file_name)
	print("Captured Screen to " + file_name)
	print()
