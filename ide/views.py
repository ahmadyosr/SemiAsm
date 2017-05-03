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
		if line[0]=='mov':											# first arg is reg16
			try : 
				dict[line[1]] = int(line[3])						#wil get exception if its a reg literal
			except ValueError: 
				dict[line[1]] = int(dict[line[3]])

		elif line[0]=='add':
			try :
				dict[line[1]] += int(line[3])
			except: 
				dict[line[1]] += int(dict[line[3]])
		elif line[0]=='sub':
			try :
				dict[line[1]] -= int(line[3])
			except: 
				dict[line[1]] -= int(dict[line[3]])
		elif line[0]=='shr':
			try:
				dict[line[1]] /= int(line[3])*2
			except: 
				dict[line[1]] /= int(dict[line[3]])*2
		elif line[0]=='shl':
			try:
				dict[line[1]] *= int(line[3])*2
			except: 
				dict[line[1]] *= int(dict[line[3]])*2
		elif line[0]=='mul':
			try:
				dict['ax'] *= int(line[1])
			except:
				dict['ax'] *= int(dict[line[1]])
			#comment here 
			bin_ax = bin(dict['ax'])
			bin_ax = int(bin_ax[2:])
			dict['dx'] = int(str(bin_ax / 10000000000000000),2) #16bit
			dict['ax'] = int(str(bin_ax % 10000000000000000),2)
			
		ax = dict['ax']												
		bx = dict['bx']
		cx = dict['cx']
		dx = dict['dx']	
		print "{0:#b},{1:#b} ,{2:#b}, {3:#b} ".format(ax,bx,cx,dx)
	dict['lines']=lines	
	return  render(request,'editor.html',dict)