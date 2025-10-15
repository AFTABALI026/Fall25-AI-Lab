import random
board = [["", "", ""], ["", "", ""], ["", "", ""]]



def show():
  for r in board:
    print("|".join(cell if cell != "" else " " for cell in r))
    print("------")

def victory():
  for i in range(3):
    if board [i][0]==board[i][1 ]==board[i][2]!="": return board[i][0]
    if board [0][i]==board[1][i]==board[2][i]!="": return board[0][i]
    if board[0][0]== board[1][1]==board[2][2]!="":return board[0][0]
    if board[0][2]==board[1][1]==board[2][0]!="":return board[0][2]
    if all(c != "" for r in board for c in r): return "Tie"
  return None


def complete():
  empty=[]
  for r in range (3):
    for c in range (3):
      if board[r][c]=="":empty.append((r, c))
   
  if empty:
    m = random.choice(empty)
    board[m[0]][m[1]] = "0"
    print(f"\ncomputer gives 0 at {m}\n")
    show()   # 👈 show table after computer move


while True:
 board = [["", "", ""], ["", "", ""], ["", "", ""]]
 while True:
    show()   # 👈 show table before player move
    try:
      p = int (input("enter value from (0-9)"))

      r= p//3
      c=p%3
      if board[r][c] == "":
       board[r][c] = "x"
       show()   # 👈 show table after player move
       break
      else:
        print("sorry the cell is full")
    except:
      print("wrong input number lol")
 w = victory()
 if w :
    show()
    if w=="x":print("huraaah you won!")
    elif w == "0": print("computer win")
    else : print("it is a tie sorry")
    break

 complete()

 if w:
  show()
  if w=="x": print("you win!")
 elif w == "0":
    print("computer win lolz!")
 else:
    print("it is a tie ")

 break 
 play = input("play again sorry")

 if play.lower()!="y":
  print("bye bye see yaa")
  break
