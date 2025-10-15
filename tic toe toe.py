import random

b=[[" "," "," "],[" "," "," "],[" "," "," "]]  # board

def show():
   for r in b:
     print("|".join(r))
print("-----")

def winner():
	for i in range(3):
	  if b[i][0]==b[i][1]==b[i][2]!=" ": return b[i][0]
	if b[0][i]==b[1][i]==b[2][i]!=" ": return b[0][i]
	if b[0][0]==b[1][1]==b[2][2]!=" ": return b[0][0]
	if b[0][2]==b[1][1]==b[2][0]!=" ": return b[0][2]
	if all(c!=" " for r in b for c in r): return "Tie"
	return None

def comp(): 
	empt=[]
	for r in range(3):
	  for c in range(3):
	    if b[r][c]==" ": empt.append((r,c))
	if empt:
	  m=random.choice(empt)
	  b[m[0]][m[1]]="O"
	  print("\ncomputer put O at",m,"\n")

while True:
	b=[[" "," "," "],[" "," "," "],[" "," "," "]] # reset
	while True:
	  show()
	  # player
	  while True:
	    try:
	      p=int(input("enter pos 1-9: "))
	      p-=1
	      r=p//3
	      c=p%3
	      if b[r][c]==" ":
	        b[r][c]="X"
	        break
	      else:
	        print("oops full cell")
	    except:
	      print("wrong input lol")
	  w=winner()
	  if w:
	    show()
	    if w=="X": print("You winn!")  # intentional typo for authentic feel
	    elif w=="O": print("computer winn")
	    else: print("its tie")
	    break
	  comp()
	  w=winner()
	  if w:
	    show()
	    if w=="X": print("You winn!")
	    elif w=="O": print("computer winn")
	    else: print("its tie")
	    break
	play=input("play again? y/n: ")
	if play.lower()!="y":
	  print("bye bye")
	  break
