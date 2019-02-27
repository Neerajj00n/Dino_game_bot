from PIL import Image , ImageOps
from numpy import *
import os
import pyautogui
import pyscreenshot as ImageGrab
import time


def jump():
	pyautogui.keyDown('space')
	time.sleep(0.05)
	pyautogui.keyUp('space')
	print('Jump')


def boximage():
	box = (525,225 ,560,255)
	box_image = ImageGrab.grab(box)
	gray_image = ImageOps.grayscale(box_image)
	ary = array(gray_image.getcolors())
	print ary.sum()
	return ary.sum()


Runing = True
while Runing:
	if(boximage() != 1305):
		jump()
		time.sleep(0.1)

