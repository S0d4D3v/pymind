import time
import random

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PINK = '\033[35m'

def randomize_answer(level) :
    if level == 1 :
        answer = [ str(random.randint(1, 4)),  str(random.randint(1, 4)), str(random.randint(1, 4)), str(random.randint(1, 4))]
    elif level == 2 :
        answer = [ str(random.randint(1, 6)),  str(random.randint(1, 6)), str(random.randint(1, 6)), str(random.randint(1, 6))]
    elif level == 3 or level == 4 :
        answer = [ str(random.randint(1, 6)),  str(random.randint(1, 6)), str(random.randint(1, 6)), str(random.randint(1, 6)), str(random.randint(1, 6))]
    elif level == 5 :
        answer = [ str(random.randint(1, 8)),  str(random.randint(1, 8)), str(random.randint(1, 8)), str(random.randint(1, 8)), str(random.randint(1, 8)), str(random.randint(1, 8))]
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
            answer[index] = 'Y'
        elif answer[index] == '6' :
            answer[index] == 'W'
        elif answer[index] == '7' :
            answer[index] == 'C'
        elif answer[index] == '8' :
            answer[index] == 'S'
        index += 1
    return answer

def check_guess(guess, answer) :
    index = 0
    ans = []
    while index < len(answer) :
        time.sleep(.7)
        if guess[index] == answer[index] :
            ans += [colors.OKGREEN, str(guess[index])]
        elif guess[index] == answer[0] :
            ans += [colors.WARNING, str(guess[index])]
        elif guess[index] == answer[1] :
            ans += [colors.WARNING, str(guess[index])]
        elif guess[index] == answer[2] :
            ans += [colors.WARNING, str(guess[index])]
        elif guess[index] == answer[3] :
            ans += [colors.WARNING, str(guess[index])]
        else :
            ans += [colors.FAIL, str(guess[index])]
        index += 1
    return ans
