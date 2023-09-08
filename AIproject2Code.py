""" the code is about a memory matching game where a player plays against a bot. The player has
to input two positions on the board and the program checks if the selected 
positions match. If there is a match, the player scores one point, and if 
there is no match, the positions are cleared. The bot selects two positions ,
and if there is a match, the bot scores one point. The game ends when all positions
on the board are taken, and the winner will be the most one that has points.
The bot uses a minimax algorithm to select the best move.
prepared for for I.Amatulrahman Alsubhi  
prepared by :
- layan alsaud
- joud albaiti
- fai almeganni
- shahad alzahrani
Course Name: Fundamentals of AI  
Course Code: CCAI-221  Section : A2L   Date: 13/2/2023
"""

# Initialize the board and real_board dictionaries.
board={1:' ' , 2:' ',3:' ',
      4:' ',5:' ',6:' ',
      7:' ',8:' ',9:' ',10:' '}
      
real_board={1:2 ,2:5, 3:5,
      4:3, 5:1, 6: 2,
      7:4 , 8:3, 9:1, 10:4}
    
# Define a function to print the current state of the board. 
def printBoard(board):
    print('\n')
    print(board[1]+' | '+board[2]+' | '+board[3]+' | '+board[4]+' | '+board[5])
    print('-----------------')
    print(board[6]+' | '+board[7]+' | '+board[8]+' | '+board[9]+' | '+board[10])
    print('-----------------')
    print('\n')
# Define a function for the start to tell the user what is the position that he/her can enter in the board to select a square .    
def numbersPosition(board):
    print('\n')
    print('1'+' | '+'2'+' | '+'3'+' | '+'4'+' | '+'5')
    print('-----------------')
    print('6'+' | '+'7'+' | '+'8'+' | '+'9'+' | '+'10')
    print('-----------------')
    print('\n')
  
# Define a function to check whether a position on the board is empty or not.    
def spaceIsFree(position):
    if (board[position] == ' '):
        return True
    else:
        return False
        

# Define a list to keep track of the user's score
user_score_list=[]
# Define a function to calculate the user's final score.
def calcUserFinalScore():
  total = 0  #Initialize total =0 
  for i in range(0, len(user_score_list)): # for loop begins with zero to length of the list (from 0 to list (length-1))
    total = total + user_score_list[i] # sum the total scores
  return total #return total csores
  
# Define a list to keep track of the bot's score.   
bot_score_list=[]
# Define a function to calculate the bot's final score
def calcBotFinalScore():
  total = 0 #Initialize total =0 
  for i in range(0, len(bot_score_list)):  # for loop begins with zero to length of the list (from 0 to list (length-1))
    total = total + bot_score_list[i]  # sum the total scores
  return total #return total csores

'''Define a function to insert the user's moves into the board.Checks if the 
 position free or not.Checks if the position1 not equal to position2 or not 
 so in case that user inter a taken position or double same position it will ask him to do it again and choose an apprppriate position , if the user enter right positions it will exposed the hidden positions that he/she enter .
 Now if user match identical numbers , he/she will got a score else it will return the position in board empty.
 Finally when all positions exposed it will check how is the winner or is it a draw'''

def insertInBoardForUser(position1, position2):
  #in this if statment it will check if the position1 and position2 are empty(free) by using spaceIsFree function that we explain above
  # also if statment check for position1 not equal to position2 , now if all 3 is true it will enter if and print real values of the choosen positions
    if (spaceIsFree(position1) & spaceIsFree(position2) & position1 != position2):
        board[position1] = str(real_board[position1]) #real value for first position
        board[position2] = str(real_board[position2]) #real value for second position
        printBoard(board) #print current board and it is value
        # Check whether the user made a match or not.
        # the program will enter if statment if user match , gives user one score for each match
        if (matching(position1, position2)):
            user_score_list.append(1) # add 1 to user_score_list every time user enter right position
            print('you got a score') # print for user that he/she got a score
        # the program will enter else if there is no matching between the values in each move that are exposed currentlly, so the board will return to it is previous state according to current board
        else:
            board[position1] = ' '
            board[position2] = ' '
        #in this if statment it will call chkDraw() function that we will explain below , now when all position is open this will retun true and enter if statment 
        if (chkDraw()):
          #in this if statment it will call calcUserFinalScore() and calcBotFinalScore() functionc to caclulate final score for each one (player, bot) if bot more than player which indicate that bot wins it will enter first if , if bot less than player it will enter second else if which indicate that playe wins, if bot and they are eqaul indicate that it is draw so it will enter third else if
          if(calcUserFinalScore() < calcBotFinalScore()):
            print('bot wins !')
          elif(calcUserFinalScore() > calcBotFinalScore()):
            print('you wins !')
          elif(calcUserFinalScore() == calcBotFinalScore()):
            print('Draw !')
        return
    #here this else if follow the first if statment in the function , in this if statment it check if user enter identical position together , and it will ask him to enter again
    elif(position1 ==position2):
        print('You can not take the same position , please pick a different position.')
        position1 = int(input('Enter new position 1: '))
        position2 = int(input('Enter new position 2: '))
        insertInBoardForUser(position1, position2)
        return
    # this else follow the first if statment in the function , which will execute if user enter taken position
    else:
      print('Position taken, please pick a different position.')
      position1 = int(input('Enter new position 1: '))
      position2 = int(input('Enter new position 2: '))
      insertInBoardForUser(position1, position2)
      return

    
"""This function inserts two values into the board dictionary, 
and if the inserted values match, it adds 1 to the bot_score_list.
It also prints the board state and checks for a draw, then prints the game's result
 """      
def insertInBoardForBot(position1,position2):
  board[position1] = str(real_board[position1]) #real value for first position
  board[position2] = str(real_board[position2]) #real value for second position
  printBoard(board)  #print current board and it is value
  bot_score_list.append(1) # add 1 to bot_score_list every time user enter right position
  print('bot got a score') # print for user that bit got a score
   #in this if statment it will call chkDraw() function that we will explain below , now when all position is open this will retun true and enter if statment
  if (chkDraw()):
     #in this if statment it will call calcUserFinalScore() and calcBotFinalScore() functionc to caclulate final score for each one (player, bot) if bot more than player which indicate that bot wins it will enter first if , if bot less than player it will enter second else if which indicate that playe wins, if bot and they are eqaul indicate that it is draw so it will enter third else if
    if(calcUserFinalScore() < calcBotFinalScore()):
      print('bot wins !')
    elif(calcUserFinalScore() > calcBotFinalScore()):
      print('you wins !')
    elif(calcUserFinalScore() == calcBotFinalScore()):
      print('Draw !')
  return

   
 #This function checks whether two positions on the board match or not and returns True or False    
def matching(position1,position2):
  if (real_board[position1]==real_board[position2]): # if positions have same values return true
    return True
  else: #other values
    return False


#This function checks if the game has ended, which happens when all positions on the board are filled, and returns True or False     
def chkDraw():
    for key in board.keys():
        if (board[key]==' '):
            return False
    return True
  
 #This function prompts the player to input two positions ,inserts them into the board using insertInBoardForUser function.
def playerMove():
    position1 = int(input('Enter new Position for number 1: ')) #read first position from user take position as int
    position2 = int(input('Enter new Position for number 2: ')) #read second position from user take position as int
    insertInBoardForUser(position1, position2) #call insertInBoardForUser function that we explained above
    return 

# This function calculates the best move for the bot using the minimax algorithm.
# It loops through all the empty positions on the board, and for each position it places
# both key1 and key2 and calculates the score using minimax. If the score is higher than the current
# best score, it updates the best score and stores the position.
def compMove():
  bestScore=-1000
  bestMove=0
  bestMove2=0
  #here we use nested for loops to check for best 2 moves position
  for key in board.keys():
      for key2 in board.keys():
        #this if statment check for empty spaces for two position and both position must be diffrent(not equal to ecah other so we can obtain diffrent places )
        #now when it is enter the if statment it will choose two position , calculate the score foe them and return them to natural status 
        # after that the internal if statment will check if score more than bestScore and if there are matching
        if(board[key]==' ' and board[key2]==' ' and key!=key2 ): 
          board[key]=real_board[key]  #real values
          board[key2]=real_board[key2] #real values
          score=minimax(board,0,False) #call minmax function that we will explain below and return score
          board[key]=' ' #retun the values to there normal status
          board[key2]=' '  #retun the values to there normal status
          if (score>bestScore and matching(key,key2)): #check if score is more than bestScore and if there are matching using matching function that we explain above
            bestScore=score 
            bestMove=key
            bestMove2=key2
            
  # After finding the best move, it calls insertInBoardForBot to make the move          
  insertInBoardForBot(bestMove,bestMove2)
  return
  
# This function is the minimax algorithm, which is used to evaluate the score of a position
# by recursively exploring all possible future moves. It takes in the current state of the board,
# whether it is maximizing or minimizing player's turn. It returns the best score that can be achieved for the current player.
def minimax(board, depth, isMaximizing):
    player_score=0
    bot_score=0
  # Checks for the base cases of the recursion, where there is a winner or the board is full.
  # It returns a value representing the outcome of the game.
    if (player_score<bot_score):
        return 1
    elif (player_score>bot_score):
        return -1
    elif(player_score==bot_score and bot_score!=0):
        return 0
    # If it is the maximizing player's turn, it loops through all empty board and
    # calls the minimax function recursively to evaluate the score of the current position.
    # It returns the best score that can be achieved for the maximizing player.
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            for key2 in board.keys():
                if board[key] == ' ' and board[key2] == ' ' and key!=key2:
                    board[key] = real_board[key]
                    board[key2] = real_board[key2]
                    score = minimax(board, 0, False)
                    board[key] = ' '
                    board[key2] = ' '
                    if score > bestScore:
                        bot_score=+1
                        bestScore = score
                          
        return bestScore
    # If it is the minimizing player's turn, it loops through all empty board and
    # calls the minimax function recursively to evaluate the score of the current position.
    # It returns the best score that can be achieved for the minimizing player.   
    else:
        bestScore = 1000
        for key in board.keys():
            for key2 in board.keys():
                if board[key] == ' 'and board[key2] == ' ' and key!=key2 :
                    board[key] = real_board[key]
                    board[key2] = real_board[key2]
                    score = minimax(board, 0, True)
                    board[key] = ' '
                    board[key2] = ' '
                    if score < bestScore:
                        player_score=+1
                        bestScore = score
                        
        return bestScore
#this are used for testing purposes. The game continues until a draw occurs.
if __name__=="__main__":
  # print welcome message to user and simple explaination for the program
  print('Hello dear user , Welocome to our simple game which is identical numbers')
  # tells the user numbers of playes which is 2 , the user and bot
  print('In this game there will be two player you and bot')
  #simple explain for the game
  print('You will try to remember exposed numbers and match them')
  #tell the user that we will print the numbers format 
  print('You will see the first board that contain allowable position for you to enter')
  #print numbers format using numbersPosition function explained above
  numbersPosition(board)
  #print board that the game will be on
  printBoard(board)   
  # run the whole game until opening all position
  #while will run until there is no empty position
  while not chkDraw() :
    compMove() #computer move
    if(not chkDraw() ): #check again there is no empty position 
      playerMove() #player move
        