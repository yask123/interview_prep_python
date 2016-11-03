# http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function


def foo():
	foo.counter = 1


foo()
print foo.counter
