#!/bin/python3.12

welcome_message = "\033[95m ___________________________________\n | Welcome to the \033[1m Mastermind game\033[0m\033[95m |\n |_________________________________|\033[0m\n"
welcome_message_2 = "\033[34m | Time to break the\033[1m code\033[0m\033[34m !\n"

check_man_message = "\033[33m |\n(?) Do you want to check the game's rules ? (y-N) : \033[0m"
check_browser_message = "\033[93m |\n[!] Check your browser, a tab has opened\033[0m\n"

choose_level_message = "\033[35m |\n(→) Choose your level : \033[0m\033[0m"
waiting_prompt = "\033[33m | \033[1m.....\033[0m"

easy_level_selected = "\n\033[33m O- \033[0m\033[32mEasy \033[0mlevel selected\033[0m\n"
normal_level_selected = "\n\033[33m O- \033[0m\033[34mNormal \033[0mlevel selected\033[0m\n"
hard_level_selected = "\n\033[33m O- \033[0m\033[33m\033[1mHard \033[0mlevel selected\033[0m\n"
extreme_level_selected = "\n\033[33m O- \033[0m\033[31mExtreme \033[0mlevel selected\033[0m\n"
ultimate_level_selected = "\n\033[33m O- \033[0m\033[31m\033[1mUltimate \033[0mlevel selected\033[0m\n"
not_a_level = "\n\033[91m X- This is not a level.\n"

take_guess = "\033[34m |\n(→) Take a guess : "
yellow_take_guess = "\033[33m |\n(→) Take a guess : "
red_take_guess = "\033[31m |\n(→) Last guess : "

possible_colors_easy = "\n\033[35m |\n(!)\033[0m The possible colors are : \033[1mR\033[0m, \033[1mG\033[0m, \033[1mB\033[0m and \033[1mP\033[0m"
possible_colors_normal = "\n\033[35m |\n(!)\033[0m The possible colors are : \033[1mR\033[0m, \033[1mO\033[0m, \033[1mY\033[0m, \033[1mG\033[0m, \033[1mB\033[0m and \033[1mP\033[0m"
possible_colors_hard = "\n\033[35m |\n(!)\033[0m The possible colors are : \033[1mR\033[0m, \033[1mO\033[0m, \033[1mY\033[0m, \033[1mG\033[0m, \033[1mB\033[0m and \033[1mP\033[0m"
possible_colors_extreme = "\n\033[35m |\n(!)\033[0m The possible colors are : \033[1mR\033[0m, \033[1mO\033[0m, \033[1mY\033[0m, \033[1mG\033[0m, \033[1mL\033[0m, \033[1mC\033[0m, \033[1mB\033[0m and \033[1mP\033[0m"
possible_colors_ultimate = "\n\033[35m |\n(!)\033[0m The possible colors are : \033[1mR\033[0m, \033[1mO\033[0m, \033[1mY\033[0m, \033[1mG\033[0m, \033[1mL\033[0m, \033[1mC\033[0m, \033[1mS\033[0m, \033[1mB\033[0m, \033[1mM\033[0m and \033[1mP\033[0m"

win_message = "\033[34m\033[95m | You won !\033[0m\n"
loose_message = "\033[91mGAME OVER\033[0m\n"
