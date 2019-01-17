import random

from soupsieve.util import upper

sample= ["EVAPORATE","TECHNICAL","WHATEVER","HANGAMA"]
wordtobeguessed = random.choice(sample)
count =0
x = len(wordtobeguessed)
guessingword = list("_"*x)
mistries = 0
while mistries<6:
    char = upper(input("Enter the Letter"))

    if wordtobeguessed.__contains__(char):
        for i in range(len(wordtobeguessed)):
            if wordtobeguessed[i] == char:
                guessingword[i]= char
                count+=1
        print(guessingword)
    else:
        mistries+=1
        print("Sorry. Try Again")
        print(guessingword)
    if count ==x:
        print("Congratulations.")
        break
