"""
A simple script that converts a single word file to PDF.
Input and output filenames (with complete path and file extension) must be provided as command line arguments.
"""

import sys
import os
import comtypes.client


argsOK = False

try:
	wordFileName = os.path.abspath(sys.argv[1])
	pdfFileName = os.path.abspath(sys.argv[2])
	#print(sys.argv)
	argsOK = True

except IndexError:
	print('You must provide arguments: path/to/word/file path/to/pdf/file')
	quit()


if argsOK:

	try:
		word = comtypes.client.CreateObject('Word.Application')
		doc = word.Documents.Open(wordFileName)

		wdFormatPDF = 17
		doc.SaveAs(pdfFileName, FileFormat=wdFormatPDF)
		doc.Close()
		word.Quit()

		print('Converted Word file: {}'.format(wordFileName))
		print('To PDF file: {}'.format(pdfFileName))
		
	except Exception as theError:
		print(theError)