import time

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
