board = [' ' for i in range(9)]
def disp():
        print(board[0],'|',board[1],'|',board[2])
        print("-"*9)
        print(board[3],'|',board[4],'|',board[5])
        print("-"*9)
        print(board[6],'|',board[7],'|',board[8],'\n')
disp()
def cwin(play):
    if board[0]==board[1]==board[2]==play or\
    board[3]==board[4]==board[5]==play or\
    board[6]==board[7]==board[8]==play or\
    board[0]==board[3]==board[6]==play or\
    board[1]==board[4]==board[7]==play or\
    board[2]==board[5]==board[8]==play or\
    board[0]==board[4]==board[8]==play or\
    board[2]==board[4]==board[6]==play:
        return True
    return False
while True:
    try:
        y = int(input("Enter position (1-9): ")) - 1
    except (IndexError,ValueError):
        print("Invalid input")
        continue
    if board[y] not in ' ':
        print("Position occupied")
        continue
    elif board[y]==' ':
        board[y] = "X"
    if cwin('X'):
        disp()
        print("Winner X")
        break
    if ' ' not in board:
        disp()
        print("draw")
        break
    disp()
    try:
        y = int(input("Enter Position (0-9): ")) -1
    except (IndexError,ValueError):
        print("Invalid input")
        continue
    if board[y] not in ' ':
        print("Position occupied") 
        continue
    elif board[y]==' ':
        board[y] = "O"
    if cwin("O"):
        disp()
        print("winner O")
        break
    if ' ' not in board:
        disp()
        print("draw")
        break
    disp() 
