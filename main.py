from pprint import pprint

def foo(name, age):
	greet = "Hi everyone, my name is {0}, and I am {1} years old."
	return greet

pprint(foo("Chris", 30))