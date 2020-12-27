#new random matrix
def new_list(mode):
	a=list()
	b=list()
	g=list()
	import random
	i=0
	while i!=16:
		t=int(random.randint(1,16))	
		if not (t in g):
			g.append(t)
			i=i+1
	if mode=='0':
		g.sort()
	c=0
	for i in range(0,4):
		for j in range(0,4):
			b.append(g[c])
			c=c+1
		a.append(b)
		b=[]
	for i in range(0,4):
		for j in range(0,4):
			if (a[i])[j]<10:
				(a[i])[j]=str("0"+str((a[i])[j]))
			else:
				if (a[i])[j]==16:
					(a[i])[j]='  '
				else:
					(a[i])[j]=str((a[i])[j])
	return a

#x position
def pos(a):
	pos=''
	for i in range(0,4):
		for j in range(0,4):
			if (a[i])[j]=='  ':
				pos=str(i)+str(j)
	return pos
	
#done check
def done(a,x,y):
	c=1
	lis=list()	
	for i in range(0,4):
		for j in range(0,4):
			lis.append((a[i])[j])
	if lis[len(lis)-1]=='  ':	
		for i in range(0,len(lis)-2):
			if int(lis[i])+1==int(lis[i+1]):
				c=c+1

	if c==15:
		return False
	else:
		return True



#start chortcut
def cuted():
	print("The game of FIFTEEN.")
	print("Type <How> to read instruction about the game.")
	print("Type <Start> to start the game.")
	print("Type <Quit> to exit from the game.")
	print("\n")


#start
def start():
	mat=new_list('1')
	gpos=pos(mat)
	ypos=int(gpos[0])
	xpos=int(gpos[1])
	while (done(mat,xpos,ypos)):
		print("\n")	
		print(mat[0])
		print(mat[1])
		print(mat[2])
		print(mat[3])
		print("\n")
		move=input("Move to: ")
		move=move.lower()
		try:
			if move[0]=='s':
				temp=(mat[ypos+1])[xpos]
				(mat[ypos+1])[xpos]='  '
				(mat[ypos])[xpos]=temp
				ypos+=1
			elif move[0]=='a':
				temp=(mat[ypos])[xpos-1]
				(mat[ypos])[xpos-1]='  '
				(mat[ypos])[xpos]=temp
				xpos-=1
			elif move[0]=='d':
				temp=(mat[ypos])[xpos+1]
				(mat[ypos])[xpos+1]='  '
				(mat[ypos])[xpos]=temp
				xpos+=1		
			elif move[0]=='w':
				temp=(mat[ypos-1])[xpos]
				(mat[ypos-1])[xpos]='  '
				(mat[ypos])[xpos]=temp
				ypos-=1	
			elif move=='tajadym.buturchu':
				pw=input("Enter password for game: ")
				if pw=='bitir_oyunu':
					mat=new_list('0')
					print("\n")	
					print(mat[0])
					print(mat[1])
					print(mat[2])
					print(mat[3])
					print("\n")
				else:
					print("Incorrect password!")	
			else:
				continue
		except:
			continue
	print("BINGO! YOU WIN!")
	cuted()


#Intro
cuted()

while True:
	mode=input(">")
	mode=mode.lower()
	if mode=='quit':
		break
	elif mode=='how':
		print("Goal: to sort 4x4 matrix in ascending order.")
		print("Use these keys to move <x> from position:")
		print("Left: <a>, Right: <d>, Up: <w>, Down: <s>.")
		print("\n")

	elif mode=='start':
		start()
	else:
		print("An invalid input.")
		print("\n")
