from django import template 
register = template.Library()


def hexing(reg):
	#carry flag 

	if int(reg) >= 0:
		reg = "{0:#x}".format(int(reg))[2:]
		for zero in range(0, 4-len(reg)):
			reg = "0" + reg 
		return reg
	else : 
		reg = "{0:#x}".format(int(reg))[3:]
		for zero in range(0, 4-len(reg)):
			reg = "0" + reg 
		return "-"+reg

register.filter('hexing',hexing)
