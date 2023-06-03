import random

board = [
    """სათამაშო დაფა, სიის სახით"""
    ' ',' ',' ',
    ' ',' ',' ',
    ' ',' ',' ',
    ]
winning_combinations = [
    """მომგები კომბინაციები"""
    #რიგები
    [0,1,2],
    [3,4,5],
    [6,7,8],
    #სვეტები
    [0,3,6],
    [1,4,7],
    [2,5,8],
    #დიაგონალები
    [0,4,8],
    [2,4,6]
]

def check_win(player):
    """ფუნქცია, რომელიც ამოწმებს, მოიგო თუ არა რომელიმე მოთამაშემ თამაში მომგები კომბინაციების 
    გადამოწმებით."""
    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def print_board():
    """ფუნქცია, რომელიც ბეჭდავს დაფას"""
    print(board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("-" * 5)
    print(board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("-" * 5)
    print(board[6] + "|" + board[7] + "|" + board[8] + "|")
    print("-" * 5)

def play_game():
    """ფუნქცია, რომელიც წარმართავს თამაშს (მოთამაშე-მოთამაშე)"""
    current_player = "X"
    game_over = False
    while not game_over:
        print_board()
        move = int(input(f"გააკეთე სვლა(1-9)({current_player})"))
        
        if move not in range(1, 10):
            print("არასწორი სვლაა")
            continue
        index = move - 1
        if board[index] != ' ':
            print("თქვენს მიერ მითითებული უჯრა უკვე დაკავებულია")
            continue
        board[index] = current_player
        
        if check_win(current_player):
          print_board()
          print(f"გამარჯვებულია {current_player}")
          game_over = True
        elif all(cell != " " for cell in board):
            print_board()
            print("ფრე.")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

def play_computer():
    """ფუნქცია, რომელიც წარმართავს თამაშს (მოთამაშე-კომპიუტერი)"""
    current_player = "X"
    game_over = False
    while not game_over:
        print_board()

        if current_player == "X":
            print(f"მოთამაშის({current_player} სვლა)")
            move = int(input(f"გააკეთე სვლა(1-9)({current_player})"))
            index = move - 1
        else:
            print(f"კომპიუტერის({current_player} სვლა)")
            available_moves = [i for i, cell in enumerate(board) if cell == " "]
            if not available_moves:
                print_board()
                print("ფრე.")
                game_over = True
                break
            move = random.choice(available_moves)
            index = move - 1


        if move not in range(1, 10):
            print("არასწორი სვლაა")
            continue
        if board[index] != ' ':
            print("თქვენს მიერ მითითებული უჯრა უკვე დაკავებულია")
            continue
        
        board[index] = current_player
        if check_win(current_player):
          print_board()
          print(f"გამარჯვებულია {current_player}")
          game_over = True
        elif all(cell != " " for cell in board):
            print_board()
            print("ფრე.")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


play_computer()