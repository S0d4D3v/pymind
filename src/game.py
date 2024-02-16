#!/bin/python3.12

import funcs
import messages
import time
import sys

def play() :
    while True :
        while True :
            try :
                funcs.message(messages.choose_level_message, .02)
                level = int(input())
            except :
                continue
            else :
                break
        funcs.message(messages.waiting_prompt, .2)
        if level == 1 :
            trials = 15
            funcs.message(messages.easy_level_selected, .02)
            time.sleep(.8)
            break
        elif level == 2 :
            trials = 15
            funcs.message(messages.normal_level_selected, .02)
            time.sleep(.8)
            break
        elif level == 3 :
            trials = 15
            funcs.message(messages.hard_level_selected, .02)      
            time.sleep(.8)
            break
        elif level == 4 :
            trials = 12
            funcs.message(messages.extreme_level_selected, .02)
            time.sleep(.8)
            break
        elif level == 5 :
            trials = 10
            funcs.message(messages.ultimate_level_selected, .02)
            time.sleep(.8)
            break
        else :
            funcs.message(messages.not_a_level, .02)
            continue

    answer = funcs.randomize_answer(level)
    current_trial = 0

    while current_trial <= trials :     
        while True :
            funcs.message(messages.take_guess, .02)
            guess = str(input())
            if len(guess) == len(answer) :
                break
            else :
                continue
        sys.stdout.write(" |\n 0-  \033[0m")
        ans = funcs.check_guess(level, guess, answer)
        funcs.message(ans, .02)
        if level == 1 :
            funcs.message(messages.possible_colors_easy, .02)
        elif level == 2 or level == 3 or level == 4 :
            funcs.message(messages.possible_colors_normal_hard_extreme, .02)
        elif level == 5 :
            funcs.message(messages.possible_colors_ultimate, .02)
        sys.stdout.write("\n")
        if guess[0] == answer[0] and guess[1] == answer[1] and guess[2] == answer[2] and guess[3] == answer[3] :
            time.sleep(.8)
            funcs.message(messages.win_message, .02)
            time.sleep(2)
            exit()
        else :
            current_trial += 1
            index = 0
    time.sleep(.5)
    funcs.message(messages.loose_message, .02)