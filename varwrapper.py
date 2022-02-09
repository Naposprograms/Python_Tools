"""
	Known issues, not solved yet:
		
		getSupportedMethods() # That is, with variable=None
		Will return in levelExpert the methods for random module, and not the ones for math module.
		This is due to the __init__ building the dict and finding the type <class 'module'> twice.
		Be aware of this if you would like to access math module's methods.
		I chose to place random last, which will replace math, because I find more useful the random module's methods.

		Calling getMethodHelp(module) where the object is a module is going to return the help of the class int.

"""

import sys
from io import StringIO


# An advanced user may take advantage of this, though I have not tested them that much
levelExpert = True

if levelExpert:
	import numpy as np
	import datetime as dt
	import math
	import random
	# And apparently it might work with some other stuff (which I have not tested yet).
	# Help yourself importing the modules that you want and give it a try.


class VarWrapper:
	"""
	VarWrapper provides an easy way to access the methods of python's standard data structures.
	This module provides a simple way for somebody who does not know much about python to use it's methods to quickly shape their data.
	The user may simply pass a variable to see which are it's available methods and to read information about them.
	Then it can access the method through some API that uses this module and use another application to receive it's data formatted.
	Thanks to python's nature of every data structure being an object, VarWrapper allows to export this methods outside of the python interpreter 
	The idea is to extend python's easy of use to external platforms (like a website or a command line).


	Simple use cases may be: 
	Get the binary representing an integer decimal number.
	Convert a bunch of text to upper case.
	Perform a distinct of a bunch of items by converting them to a set.
	Reverse the order of a list of items.
	
	The possibilites are many, and this module will be able to handle much complex operations as well.
	"""
	def __init__(self):

		# int, float, string, list, tuple, set, dict, bool
		self.__supportedTypesExampleVariables = [0, 1.0, 'string', [0, 1], (0, 1), {0, 1}, {'key':'value'}, True]
		if levelExpert:
			# ndarray, datetime, math module, random module
			expertTypes = [np.ndarray([0, 1]), dt.datetime.now(), math, random]
			self.__supportedTypesExampleVariables += expertTypes
		
		
		# list of type(var) for different types. Used to check input variable's type
		self.__supportedTypesNames = list( map(lambda var: str(type(var)), self.__supportedTypesExampleVariables) )
		#print(__supportedTypesNames)
		self.methodsDict = {}
		for i in range(len(self.__supportedTypesExampleVariables)):
			self.methodsDict[self.__supportedTypesNames[i]] = self.__getTypeMethods__(self.__supportedTypesExampleVariables[i])

	
	def __getTypeMethods__(self, variable):
		"""
		Generates a list of the object type (passed variable) methods.
		"""		
		methodsList = dir(variable)
		for i in range( len(methodsList) - 1, -1, -1 ):
			if ( methodsList[i].startswith("__") ):
				methodsList.pop(i)

		return methodsList
	
	
	def __getMethodFromIndex__(self, variable, index):
		"""
		Used to retrieve the method name by it's index in the list of methods.
		"""
		varType = str(type(variable))
		if varType in self.__supportedTypesNames:
			methodsList = self.__getTypeMethods__(variable)
			methodsListSize = len(methodsList)
			if str(type(index)) == "<class 'int'>":
				if (-1 < index and index < methodsListSize):
					return methodsList[index]
				
				else:
					return 'No method found for provided index. Try getSupportedMethods()'				
	
	
	def getSupportedMethods(self, variable=None):
		"""
		Returns the methods available to be used given a variable type.
		If no variable is provided, then it returns a dictionary containing the variable types as keys, and the methods as values.
		Tip:
		Run the following to see more clearly the dict thanks to the indentation 
		import json
		jsonObject = json.dumps(varwrapper.getSupportedMethods(), indent=4)
		print(jsonObject)
		"""
		if variable != None:
			if str(type(variable)) in self.__supportedTypesNames:
				return self.methodsDict[str(type(variable))]
		
		else:
			return self.methodsDict


	def getMethodHelp(self, variable, methodRequested):
		"""
		Returns the requested method's documentation through help command.
		Although this command typically prints the help to stdout. I managed to redirect it to a string variable.
		This way, if the application using this module has no visibility in the command prompt, you may still be able to access the help command.
		For more information on how to do this, visit: https://iqcode.com/code/python/redirect-stdout-to-variable-python
		"""
		varType = str(type(variable))
		if varType in self.__supportedTypesNames:
			if str(type(methodRequested)) == "<class 'int'>":
				methodRequested = self.__getMethodFromIndex__(variable, methodRequested)
			if (methodRequested in self.methodsDict[varType]):
				old_stdout = sys.stdout
				sys.stdout = mystdout = StringIO()
				help(variable.__getattribute__(methodRequested))
				sys.stdout = old_stdout
				helpText = mystdout.getvalue()[:-2] # Discards the two line feeds at the end.
				replaceText = 'Help on built-in function ' + methodRequested + ':\n\n'
				return helpText.replace(replaceText, '')
		
		else:
			return 'variable should be one of the supported types: {}'.format(str(self.__supportedTypesNames))
		
	
	def executeMethod(self, variable, methodRequested, args=[]):
		"""
		Receives an input variable value and performs the requested method on it (with optional arguments provided).
		Returns the output of the method applied on the input variable.
		Provided arguments should be an iterable (pass them in a list)
		>>> self.executeMethod(self, 8, 0)
		4
		>>> self.executeMethod(self, 'python', 'replace', ['thon', ''])
		py
		>>> self.executeMethod(self, 1.5, 0)
		(3, 2)		
		"""
		varType = str(type(variable))
		if varType in self.__supportedTypesNames:
			methodsList = self.__getTypeMethods__(variable)
			if str(type(methodRequested)) == "<class 'int'>":
				methodRequested = self.__getMethodFromIndex__(variable, methodRequested)
				if methodRequested in methodsList:
					result = variable.__getattribute__( methodsList[methodRequested] ) (*args)
					return result
					
			elif str(type(methodRequested)) == "<class 'str'>":
				if methodRequested in methodsList:
					result = variable.__getattribute__( methodRequested ) (*args)
					return result
				
			else:
				return 'Wrong method name/index'


		else:
			return 'Object type not supported'



varwrapper = VarWrapper()


if __name__ == "__main__":
	#import doctest
	#doctest.testmod()	
	
	# Though most of this works I have not fully tested this module
	# All of this tests below have proved to work fine:

	""""
	
	print(varwrapper.getSupportedMethods())
	print(varwrapper.getSupportedMethods(1.6))
	print(varwrapper.getSupportedMethods('wait'))
	print(varwrapper.getSupportedMethods(0))
	print(varwrapper.getMethodHelp(1, 'to_bytes'))
	print(varwrapper.getMethodHelp('a', 'capitalize'))
	print(varwrapper.__getMethodFromIndex__(1, 1))
	print(varwrapper.__getMethodFromIndex__(1, 20))
	print(varwrapper.getMethodHelp(1, 0))
	print(varwrapper.getMethodHelp('a', 2))
	
	# levelExpert	
	print(varwrapper.executeMethod(dt.datetime(1, 1, 1, 1, 1, 1), 'now'))
	print(varwrapper.executeMethod(math, 'cos', [0]))
	print(varwrapper.executeMethod(random, 'randrange', [-5, -1]))

	"""

	typesList = [0, 1.0, '1', [0, 1], (0, 1), {0, 1}, {0 : 1, }, False]
	if levelExpert:
		expertTypesList = [np.ndarray([0, 1]), dt.datetime.now(), math, random]
		typesList += expertTypesList

	for atype in typesList:
		print(str(type(atype)))	
		print(varwrapper.getSupportedMethods(atype))
		print(varwrapper.getMethodHelp(atype, 0))