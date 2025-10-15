import random
computer = random.randint(1,100)
i=0
while True:
   mynum = int(input("guess the number (1-100):"))
   i+=1
   if (computer == mynum):
        print("your guess is match")
        print("you win!!")
        break
   elif(mynum==-1):
        print("quit game")
        print("this is your random number ",computer)
        break
   elif(computer<mynum):
        print("too large, guess small number")
   elif(computer>mynum):
        print("too small, guess large number")
print(f"you guess the number total {i} attemps")
