from django import template 
register = template.Library()

def hexing(reg):
	print type(reg)
	reg = "{0:#x}".format(int(reg))[2:]	
	for zero in range(0, 4-len(reg)):
		reg = "0" + reg 
	return reg
	
register.filter('hexing',hexing)
