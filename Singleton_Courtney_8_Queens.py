# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 14:27:08 2019

@author: Courtney Singleton
"""
from random import randrange


#set up board, initialize with 0s for empty spaces
chess_board = [
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"],
["0", "0", "0", "0", "0", "0", "0", "0"]
]

def initialize():
    
    #set initial state with random locations of 1s in each column (Queens)
    for c in range(8): 
        #make sure there are no queens on board
        if "1" in chess_board[c]:
            chess_board[c][chess_board[c].index("1")] = "0"
        rand_num = randrange(8)
        chess_board[c][rand_num] = "1";
        
        
        
    horizontal = horizontal_check()
    diagonal = diagonal_check()
        
    return horizontal + diagonal
    

def horizontal_check():
    h = 0
    #loop through chessboard based on index
    for i in range(8):
        num_queens = 0
        #increase the number of queens by 1 for every "1" found in the row
        for n in range(8):
            if chess_board[n][i] == "1":
                num_queens+=1;
        #if more than one queen is found in the row, increase heurisitc        
        if num_queens > 1:
            #heuristic increases for every extra queen in the row
            h += num_queens -1
    #print("Horizontal: " + str(h))
    return h
    

def diagonal_check():
  
  h = 0
  num_queens = 0
  start_col = 0
  start_sq = 0
  #1st loop will run twice to get diagonals in both directions
  for j in range(4):
      #second loop will run 7 times to check each diagonal
      for i in range(8):
          #if this is the first time through, start for (0,0)
          if j == 0:
              start_col = 0
              start_sq = i
          elif j == 1:
              #if this is the second time, start from (7,0)
              start_col = 7
              start_sq = i
          #these two get the botom half diagonals    
          elif j == 2:
              #start at (0,7)
              start_col = 0
              start_sq = 7 - i
              
              #don't want to count that long diagonal twice, so skip iteration at (0,0)
              if start_sq == 0:
                  continue
              
          elif j == 3:
              #start at (7,7)
              start_col = 7
              start_sq = 7 - i 
              
              #don't want to count that long diagonal twice, so skip iteration at (7,0)
              if start_sq == 0:
                  continue
             
              
          #reset number of queens found
          num_queens = 0
          #3rd loop will run once for every square in the diagonal
          for n in range(i + 1):
              #print("Round " + str(j + 1) + " Diagonal " + str(i + 1) )
              #print (str(start_col) + ", " + str(start_sq))
              
              #check if there is a queen in current square
              if chess_board[start_col][start_sq] == "1":
                  #print("Queen Found: " + str(start_col) + ", " + str(start_sq))
                  num_queens += 1
                  #print(num_queens)
                  
              
              #move left or right based on which column loop starts in/up and down
              if j == 0:
                  start_col += 1
                  start_sq -= 1
              elif j == 1:
                  start_col -=1
                  start_sq -= 1
              elif j == 2:
                  start_col += 1
                  start_sq += 1
              elif j == 3:
                  start_col -= 1
                  start_sq += 1
          
              
          #print("Queens in diagonal: " + str(num_queens))
          if num_queens > 1:
              h += num_queens - 1
              #print("Heuristic: " + str(h))
  #print("Diagonal: " + str(h))            
  return h       
#initialize variables for the heuristics of current and next states
current_h = initialize()
lowest_h = current_h
#print("Overall: " + str(current_h))

#get column and index positions for the lowest heuristic/next state
lowest_col = 0
lowest_index = 0
queen_pos = 0
replace_pos = 0

#variables to track state changes and restarts
restarts = 0
states = 0



while current_h > 0:
    #initialize the number of lower heuristics at 0 every time the loop runs
    num_lower = 0
    next_h = 0   
    
    #update current heuristic
    current_h = lowest_h
    
    #loop to check each possible future state
    #first loop to go through each column
    for c in range(7):
        
        #c == index of current column
        
        #get current position of the queen
        queen_pos = chess_board[c].index("1")
        
        #remove queen from the board
        chess_board[c][queen_pos] = "0"
        
        
        #second loop to go through each square in the column
        for s in range(7):                      
            
            #s == index of current square
           
            #place queen on current square
            chess_board[c][s] = "1"
            
            #calculate the heuristic if the queen is moved to this position
            this_h = diagonal_check() + horizontal_check()
            #print("Heuristic: " + str(this_h))
                       
            #check if next heuristic value is lower than current
            if this_h < current_h:
                num_lower += 1
                #check if heuristic value is the lowest so far
                if this_h < lowest_h:
                    #set this as the lowest heuristic and save position of this queen
                    lowest_h = this_h
                    lowest_col = c
                    lowest_index = s
                    replace_pos = queen_pos
                    
            #remove queen   
            chess_board[c][s] = "0"
            
        
        #replace queen in original current state's position before moving to next column
        chess_board[c][queen_pos] = "1"
                    
    #END OF FOR LOOPS        
    
    #print current board and heuristic value
    print(" ")
    print("Current Heuristic: " + str(current_h))
    print("Current State")
    position = 0
    while position < 8:
       print(chess_board[0][position] + " " + 
             chess_board[1][position] + " " + 
             chess_board[2][position] + " " + 
             chess_board[3][position] + " " + 
             chess_board[4][position] + " " + 
             chess_board[5][position] + " " + 
             chess_board[6][position] + " " + 
             chess_board[7][position])
       position += 1
       
    #print Solution found if current_h == 0 else, contnue displaying next state
    if current_h == 0:
        print("SOLUTION FOUND :) " )
    else:
        print("Neighbors Found With Lower State: " + str(num_lower))
    
        if num_lower == 0:
            #RESTART - call initial method again
            print("RESTART")
            current_h = initialize()
            lowest_h = current_h
            has_restarted = True
            restarts += 1
        else:
            print("Setting New Current State")
            chess_board[lowest_col][replace_pos] = "0"
            chess_board[lowest_col][lowest_index] = "1"
            states += 1   
#END OF WHILE LOOP    
#print total state changes and restarts, guess I need variable to track those
print("State Changes: " + str(states))
print("Restarts: " + str(restarts))     










