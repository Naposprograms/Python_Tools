"""
This script is a simple screen recorder (no audio).
It is run from terminal and stores in a .avi file your screen after an initial delay time.
Required arguments are path/to/video/file and delay time to start recording (must be integer).
You should not provide a file name with a extension since the script adds .avi at the end of the provided path.
To stop recording you must return to the terminal window and type KeyboardInterrupt
"""

import sys
import cv2
import numpy as np
import os
import pyautogui
from time import sleep


argsOK = False

try:
	fileName = str(sys.argv[1])
	delayTime = int(sys.argv[2])
	#print(sys.argv)
	argsOK = True

except IndexError:
	print('You must provide arguments: path/to/video/file (no extension) delayTime (integer)')
	quit()


if argsOK:

	print('Recording will initiate in {} seconds from now. To stop recording type KeyboardInterrupt.'.format(delayTime), flush=True)
	
	for i in range(delayTime, 0, -1):
		print(i, flush=True)
		sleep(i)
	
	print('Action!', flush=True)	
	
	img = pyautogui.screenshot()
	img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
	height, width, channels = img.shape
	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	out = cv2.VideoWriter(fileName + '.avi', fourcc, 20.0, (width, height))


	while(True):
		
		try:
			img = pyautogui.screenshot()
			image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
			out.write(image)
			StopIteration(0.5)
			
		except KeyboardInterrupt:
			break


	out.release()
	cv2.destroyAllWindows()