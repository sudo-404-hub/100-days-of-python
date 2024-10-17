# 8. Tic Tac Toe blocker
# In this Python challenge, write a function that’ll accept two numbers. These numbers will represent a position on a tic-tac-toe board. They can be 0 through 8, where 0 is the top-left spot, and 8 is the bottom-right spot.

# These parameters are two marks on the tic-tac-toe board. The function should return the number of the spot that can block these two spots from winning the game.



winning_combinations = [
    {0, 1, 2},  # Top row
    {3, 4, 5},  # Middle row
    {6, 7, 8},  # Bottom row
    {0, 3, 6},  # Left column
    {1, 4, 7},  # Middle column
    {2, 5, 8},  # Right column
    {0, 4, 8},  # Diagonal
    {2, 4, 6}   # Other diagonal
]

# Tic Tac Toe board
print("This is the numerotation of the spots on the Tic Tac Toe board : ")
print("┌───┬───┬───┐")
print("│ 0 │ 1 │ 2 │")
print("├───┼───┼───┤")
print("│ 3 │ 4 │ 5 │")
print("├───┼───┼───┤")
print("│ 6 │ 7 │ 8 │")
print("└───┴───┴───┘")

print("You have 2 move to win then i try to bloack u , Lets try your intelligence :-)")

def my_function(first_num, second_num):
    for combo in winning_combinations:
        if first_num in combo and second_num in combo:
            print("I will move to ", (combo - {first_num , second_num}).pop() ,"to block u.") # {0, 1, 2} - {0, 1}  # results in {2}
            break
        else:
            print("You can't win with these move")
            break
            
            
while True:
    input1 = int(input("Enter the First move: "))
    input2 = int(input("Enter the Second move: "))
    my_function(input1, input2)


# .pop(): This method removes and returns an arbitrary element from the set. In this case, it will return the only remaining element (the blocking position).

