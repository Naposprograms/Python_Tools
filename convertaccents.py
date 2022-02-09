def convertAccents(inputString):
	"""
	Takes an input string and converts the non-ASCII typically used characters in Spanish to ASCII.
	It replaces the accents and opening question and exclamation marks.
	Returns a string suitable for UTF-8.
	"""
	replaceDict = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', '¿':'', '¡':''}
	for key in replaceDict:
		inputString = inputString.replace(key, replaceDict[key])
	
	return inputString