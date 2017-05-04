from django.shortcuts import render , redirect
from django.http import HttpResponse

# Create your views here.

def editor(request, *args):
	if request.method == 'POST':
		lines = request.POST['text'].splitlines()
		return compiling(request, lines)
	return render(request,'editor.html')
def compiling(request,lines):
	ax = 0 #0
	bx = 0 #1
	cx = 0 #2
	dx = 0 #3

	dict ={'ax':0 , 'bx':0, 'cx':0 , 'dx':0 }
	regs = ('ax','bx','cx','dx')
	operations = ('mov','add' ,'sub','shl','shr')
	for line in lines : 
		line = line.split()
		cmd = line[0]
		op1 = line[1]
		op2 = line[3]
		
		if cmd =='mov':											# first arg is reg16
			try : 
				dict[op1] = int(op2)						#wil get exception if its a reg literal
			except ValueError: 
				dict[op1] = int(dict[op2])
		elif cmd =='add':
			try :
				dict[op1] += int(op2)
			except: 
				dict[op1] += int(dict[op2])
		elif cmd =='sub':
			try :
				dict[op1] -= int(op2)
			except: 
				dict[op1] -= int(dict[op2])
		elif cmd =='shr':
			try:
				dict[op1] /= (int(op2)*2)
			except: 
				dict[op1] /= int(dict[op2])*2
		elif cmd =='shl':
			try:
				dict[op1] *= int(op2)*2
			except: 
				dict[op1] *= int(dict[op2])*2
		elif cmd =='mul':
			try:
				dict['ax'] *= int(op1)
			except:
				dict['ax'] *= int(dict[op1])
			bin_ax = bin(dict['ax'])
			bin_ax = int(bin_ax[2:])
			dict['dx'] = int(str(bin_ax / 10000000000000000),2) #16bit
			dict['ax'] = int(str(bin_ax % 10000000000000000),2)
		
		if dict[op1] > 65535 or dict[op1] < 0 :
			dict['carry_flag'] = 1 
		else :
			dict['carry_flag'] = 0 
		if dict[op1] > 53248 or dict[op1] < 0 : 
			dict['sign_flag'] = 1
		else :
			dict['sign_flag'] = 0 
		ax = dict['ax']	
		bx = dict['bx']
		cx = dict['cx']
		dx = dict['dx']
		print ax ,bx,cx,dx
		print "{0:#b},{1:#b} ,{2:#b}, {3:#b} ".format(ax,bx,cx,dx)
		
	dict['lines']=lines	
	return  render(request,'editor.html',dict)