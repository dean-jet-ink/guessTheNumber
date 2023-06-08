import math
import random


print("Guess The Number Game");
s1 = input("Input min number ");
s2 = input("Input max number ");

min = int(s1);
max = int(s2)

if max > min:
    guess = random.randint(min, max);

    for i in range(math.floor((max - min + 1) / 3), 0, -1):
        print(f"You can answer {i} more times.");
        s = input("Answer is...? ");
        answer = int(s);

        if guess == answer: 
            print("Conguratulations!!");
            break;
        elif guess > answer:
            print("No, more greater");
        else: print("No, more smaller");
        
    else: print("game over.");
    
else:
    print("Please enter a number greater than min for max.");
