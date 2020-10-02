
bd= ["-","-","-",
        "-","-","-",
        "-","-","-"]

game_still_going = True
winner = None

def display_bd():  
    print("|"+bd[0]+" "+bd[1]+" "+ bd[2]+"|    |1 2 3|" )
    print("|"+bd[3]+" "+bd[4]+" "+ bd[5]+"|    |4 5 6|" )
    print("|"+bd[6]+" "+bd[7]+" "+ bd[8]+"|    |7 8 9|" )

def play_game():
    display_bd()

    while game_still_going():
0
    
turn ="X"


def check_win():
    if result == 1:
        print("Win.")
    elif result == 0:
        print("lose")
    else:
        print("Tie")

def checkk_raw():
    for i in range(3): 
        if bd[i]==bd[i+1]==bd[i+2]:
            result = 1

def check_col():
    for i in range(3): 
        if bd[i]==bd[i+3]==bd[i+6]:
            result = 1

def check_dia():
    if (bd[0]==bd[4]==bd[8]):
        result = 1
    elif(bd[2]==bd[4]==bd[6]):
        result = 1

def get_input():
    if(turn == "X"):
        print("It is X's turn.")
        get = int(input("Please enter the number form 1 to 9 : "))
        if (get > 9) or (get <1):
            print("Please enter the right number.")
            get_input()
        else:
            None
        get = (get-1)
        bd[get] = "X"
        display_bd()

    if(turn == "O"):
        print("It is O's turn.")
        get = int(input("Please enter the number form 1 to 9 : "))
        if (get > 9) or (get <1):
            print("Please enter the right number.")
            get_input()
        get = (get-1)
        bd[get] = "O"
        display_bd()



