#!/bin/python3.12

import lib.funcs
import lib.messages

import sys
import time
import time
import webbrowser

lib.funcs.message(lib.messages.welcome_message, 0.01)
time.sleep(.6)
lib.funcs.message(lib.messages.welcome_message_2, 0.02)
time.sleep(.6)
lib.funcs.message(lib.messages.check_man_message, 0.02)
check_man_page = str(input())
if check_man_page == "yes" or check_man_page == "YES" or check_man_page == "Yes" or check_man_page == "y" or check_man_page == "Y" :
    webbrowser.open('https://github.com/S0d4D3v/mastermind')
    time.sleep(.2)
    lib.funcs.message(lib.messages.check_browser_message, 0.02)
    time.sleep(1.2)
time.sleep(.2)

while True :
    while True :
        try :
            lib.funcs.message(lib.messages.choose_level_message, 0.02)
            level = int(input())
        except :
            continue
        else :
            break
    lib.funcs.message(lib.messages.waiting_prompt, 0.2)
    if level == 1 :
        trials = 15
        lib.funcs.message(lib.messages.easy_level_selected, 0.02)
        time.sleep(.8)
        break
    elif level == 2 :
        trials = 15
        lib.funcs.message(lib.messages.normal_level_selected, 0.02)
        time.sleep(.8)
        break
    elif level == 3 :
        trials = 12
        lib.funcs.message(lib.messages.hard_level_selected, 0.02)
        break
    elif level == 4 :
        trials = 10
        lib.funcs.message(lib.messages.extreme_level_selected, 0.02)
        time.sleep(.8)
        break
    elif level == 5 :
        trials = 5
        lib.funcs.message(lib.messages.ultimate_level_selected, 0.02)
        time.sleep(.8)
        break
    else :
        lib.funcs.message(lib.messages.not_a_level, 0.02)
        continue
answer = lib.funcs.randomize_answer(level)
current_trial = 0

while current_trial <= trials :     
    while True :
        if trials - current_trial <= 1 :
            lib.funcs.message(lib.messages.red_take_guess, 0.02)
        elif trials - current_trial <= 3 :
            lib.funcs.message(lib.messages.yellow_take_guess, 0.02)
        else :
            lib.funcs.message(lib.messages.take_guess, 0.02)
        guess = str(input())
        if len(guess) == len(answer) :
            break
        else :
            continue
    sys.stdout.write(" |\n 0-  \033[0m")
    ans = lib.funcs.check_guess(level, guess, answer)
    lib.funcs.message(ans, 0.02)
    if level == 1 :
        lib.funcs.message(lib.messages.possible_colors_easy, 0.01)
    elif level == 2 or level == 3 or level == 4 :
        lib.funcs.message(lib.messages.possible_colors_normal, 0.01)
    elif level == 5 :
        lib.funcs.message(lib.messages.possible_colors_ultimate, 0.01)
    sys.stdout.write("\n")
    if guess[0] == answer[0] and guess[1] == answer[1] and guess[2] == answer[2] and guess[3] == answer[3] :
        time.sleep(.8)
        lib.funcs.message(lib.messages.win_message, 0.02)
        time.sleep(2)
        exit()
    else :
        current_trial += 1
        index = 0
time.sleep(.5)
lib.funcs.message(lib.messages.loose_message, 0.02)