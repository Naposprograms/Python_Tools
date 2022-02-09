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

Known issues, not solved yet:

getSupportedMethods() # That is, with variable=None
Will return in levelExpert the methods for random module, and not the ones for math module.
This is due to the __init__ building the dict and finding the type <class 'module'> twice.
Be aware of this if you would like to access math module's methods.
I chose to place random last, which will replace math, because I find more useful the random module's methods.

Calling getMethodHelp(module) where the object is a module is going to return the help of the class int.