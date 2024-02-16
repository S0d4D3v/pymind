#!/bin/python3.12

import random

def randomize_answer(level) :
    if level == 1 :
        answer = [ str(random.randint(1, 4)),  str(random.randint(1, 4)), str(random.randint(1, 4)), str(random.randint(1, 4))]
    elif level == 2 :
        answer = [ str(random.randint(1, 6)),  str(random.randint(1, 6)), str(random.randint(1, 6)), str(random.randint(1, 6))]
    elif level == 3 or level == 4 :
        answer = [ str(random.randint(1, 6)),  str(random.randint(1, 6)), str(random.randint(1, 6)), str(random.randint(1, 6)), str(random.randint(1, 6))]
    elif level == 5 :
        answer = [ str(random.randint(1, 10)),  str(random.randint(1, 10)), str(random.randint(1, 10)), str(random.randint(1, 10)), str(random.randint(1, 10)), str(random.randint(1, 10))]
    index = 0
    while index < len(answer) :
        if answer[index] == '1' :
            answer[index] = 'R'
        elif answer[index] == '2' :
            answer[index] = 'G'
        elif answer[index] == '3' :
            answer[index] = 'B'
        elif answer[index] == '4' :
            answer[index] = 'P'
        elif answer[index] == '5' :
            answer[index] = 'O'
        elif answer[index] == '6' :
            answer[index] = 'Y'
        elif answer[index] == '7' :
            answer[index] = 'L'
        elif answer[index] == '8' :
            answer[index] = 'C'
        elif answer[index] == '9' :
            answer[index] = 'S'
        elif answer[index] == '10' :
            answer[index] = 'M'
        index += 1
    return answer

def check_guess(level, guess, answer) :
    index = 0
    ans = []
    if level == 1 or level == 2 :
        while index < len(answer) :
            if guess[index] == answer[index] :
                ans += ["\033[92m", str(guess[index])]
            elif guess[index] == answer[0] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[1] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[2] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[3] :
                ans += ["\033[93m", str(guess[index])]
            else :
                ans += ["\033[91m", str(guess[index])]
            index += 1
    elif level == 3 or level == 4 :
        while index < len(answer) :
            if guess[index] == answer[index] :
                ans += ["\033[92m", str(guess[index])]
            elif guess[index] == answer[0] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[1] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[2] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[3] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[4] :
                ans += ["\033[93m", str(guess[index])]
            else :
                ans += ["\033[91m", str(guess[index])]
            index += 1
    elif level == 5 :
        while index < len(answer) :
            if guess[index] == answer[index] :
                ans += ["\033[92m", str(guess[index])]
            elif guess[index] == answer[0] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[1] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[2] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[3] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[4] :
                ans += ["\033[93m", str(guess[index])]
            elif guess[index] == answer[5] :
                ans += ["\033[93m", str(guess[index])]
            else :
                ans += ["\033[91m", str(guess[index])] 
            index += 1
    return ans