"""
This script uses Tesseract-OCR (you must install it in your system first) to read text from image files.
You only need to provide the image path and the path for the output text file.
"""

import sys
import cv2
import pytesseract

# Uncomment if needed to run as root:
#from elevate import elevate
#elevate()

# Mention the installed location of Tesseract-OCR in your system ONLY IF YOU HAVE NOT ADDED THIS PATH TO WINDOWS PATH
#pytesseract.pytesseract.tesseract_cmd = 'System_path_to_tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = 'C:\"Program Files"\Tesseract-OCR\tesseract.exe'

argsOK = False

try:
	imgPath = str(sys.argv[1])
	fileName = str(sys.argv[2])
	#print(sys.argv)
	argsOK = True

except IndexError:
	print('You must provide arguments: path/to/img outfile/name')
	quit()


if argsOK:

	img = cv2.imread(imgPath)
	check_image_type = str(type(img))
	if check_image_type == "<class 'NoneType'>":
		print("No image file found in provided path: {}".format(imgPath))
		quit()

	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	
	file = open(fileName, "w")
	file.close()
	file = open("recognized.txt", "a")


	# Apply OCR on the cropped image
	text = pytesseract.image_to_string(gray)
	  

	file.write(text)
	file.write("\n")
	file.close()