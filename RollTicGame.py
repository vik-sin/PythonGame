import random

print("\t\t\t\t Welcome to the Game")

print("Introduction: \n")
print("This is a game of 3 players in which two players- Player-1 and Player-2 will play in Round-1. The winner of this round will play with Player-3 in Round-2.\n")
print("Round-1: \n ")
print("In this round,each player will be given 5 chances to roll a dice and output of that rolling of dice will be shown on screen.The total sum of 5 rollings will be \
calculated and the one with more score will win this round and qualifies for Round-2.In case,if score of the two players come out to be equal,then  the player who scored \
maximum number of sixes will be a winner.\n")
print("Round-2: \n")
print("In this round ,the winner of first round play a 'TIC-TAC-TOE' game with player-3 and the winner of this round will be declared as a winner of the game.\n")

p1 = input(("Player-1,Enter your name. : "))
p2= input(("Enter your name, Player-2. : "))
p3= input(("Player-3,Enter your name. : "))
print("\n")

print("\t\t Welcome to the Round-1 \n")
print("{} ,it's your turn. All the best! \n".format(p1))

sum1= 0
ran =0
sixNum1=0

for i in range(1,6,1):

    j= int(input("Press 1 to roll a dice.\n"))

    if j ==1 :
        print("\t Rolling-{} ".format(i))
        ran= (random.randint(1,6))
        print("Result of rolling is : {}".format(ran))
        sum1=sum1 + ran
        print("Sum : ", sum1)
        print("\n")

        if ran == 6:
            sixNum1 +=1;

    else:
        print(" Character isn't recognised.Please,enter 1 only to roll a dice.")
        

  
print("{} your total score is {}. \n\n".format(p1,sum1))



print("{} ,it's your turn. All the best! \n".format(p2))

sum2 =0
ran=0
sixNum2 =0

for k in range(1,6,1):

    j= int(input("Press 1 to roll a dice.\n"))

    if j ==1 :
        print("\t Rolling-{} ".format(k))
        ran= (random.randint(1,6))
        print("Result of rolling is : {}".format(ran))
        sum2=sum2 + ran
        print("Sum : ", sum2)
        print("\n")

        if ran == 6:
            sixNum1 +=1;

    else:
        print(" Character isn't recognised.Please,enter 1 only to roll a dice.")
        

  
print("{} your total score is {}. \n\n".format(p2,sum1))
print("-----------------------------------------------------------------------------------------------------------------------")


if sum1 > sum2:
    winner=p1
    
elif sum1 == sum2:
    if sixNum1 >= sixNum2:
        winner=p1
    else:
        winner=p2
    
else:
    winner=p2
    
print("\t Winner of Round-1 is {}.".format(winner))


print("----------------------------------------------------------------------------------------------------------------------")



print("\t\t Welcome to the Round-2 \n")
print("\t TIC-TAC-TOE ")

tic = [[0]*3]*3
print(tic)

#===========================================================================================================================
#===========================================================================================================================

#TIC TAC TOE
import sys

print("\t\t Welcome to the Round-2 \n")
print("\t TIC-TAC-TOE ")


tic = [1,2,3,4,5,6,7,8,9]
#----------------------------------------------------------------------------------------------------------------------------------------------

def mark(val,char):
    abc=tic[val-1]
          
    if abc!='A' and abc!='B' :
        tic[val-1]=char
        show()
    
    else:
        val=int(input("Already marked. Please,try some another block to mark."))
        mark(val,char)

#-------------------------------------------------------------------------------------------------------------------------        

def check(name):
          
         
    #checking row-wise

    a = ( (tic[1]==tic[0]) and (tic[2]==tic[1]) ) or ( (tic[4]==tic[3]) and (tic[5]==tic[4]) ) or ( (tic[7]==tic[6]) and (tic[8]==tic[7]) )
        
    #checking column-wise
    
    b = ( (tic[3]==tic[0]) and (tic[6]==tic[3]) ) or ( (tic[4]==tic[1]) and (tic[7]==tic[4]) ) or ( (tic[5]==tic[2]) and (tic[8]==tic[5]) )
        
   #checking diagonal-wise
          
    c = ( (tic[4] == tic[2]) and (tic[6] ==  tic[4]) ) or ( (tic[4] == tic[0]) and (tic[8] ==  tic[4]) )

    if (a==1) or (b==1) or (c==1):
        print("{} has won this round as well as game.".format(name))
        sys.exit()

#----------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
def show():
    print('|',tic[0],'|',tic[1],'|',tic[2],'|')
    print("----------------")
    print('|',tic[3],'|',tic[4],'|',tic[5],'|')
    print("----------------")
    print('|',tic[6],'|',tic[7],'|',tic[8],'|')
    print("----------------")

#-------------------------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------------------------
#1
val = int(input("{}, Enter the block no.".format(winner)))
char='A'
mark(val,char)

#2
val = int(input("{}, Enter the block no.".format(p3)))
mark(val,'B')

#3
val = int(input("{}, Enter the block no.".format(winner)))
mark(val,'A')

#4
val = int(input("{}, Enter the block no.".format(p3)))
mark(val,'B')

#5
val = int(input("{}, Enter the block no.".format(winner)))
mark(val,'A')
check(winner)

#6
val = int(input("{}, Enter the block no.".format(p3)))
mark(val,'B')
check(p3)

#7
val = int(input("{}, Enter the block no.".format(winner)))
mark(val,'A')
check(winner)

#8
val = int(input("{}, Enter the block no.".format(p3)))
mark(val,'B')
check(p3)

#9
val = int(input("{}Enter the block no.".format(winner)))
mark(val,'A')
check(winner)
#------------------------------------------------------------------------------------------------------------------------

