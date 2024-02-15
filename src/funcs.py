import time

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
