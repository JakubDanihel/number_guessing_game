#number guessing game

import random

#funkcia pre hranie znova
#function for playnig again
def znova(nazor):
    #check for correct symbol
    if((nazor == "Y") or (nazor == "y")):
        number_guess()
    elif((nazor == "N") or (nazor == "n")):
        print("Thanks for playing! See you soon!")
    else:
        print("Wrong symbol! Write Y or y for new game. For quit write N or n")
        i = input("Write [y/n]: ")
        znova(i)

#zisti ci je zadana hodnota spravna
def je_cislo(vstup):

    #flag pre zistenie ci je cislo pri porovnani spravne
    #flag for understanding if it is number
    flag = True

    #try to catch error
    #skusenie najst chyby
    try:
        #je vstup integer?
        #is input integer?
        int(vstup)
    #Ak hodnota nie je error jedna sa o chybu hodnoty
    #if value is error it is error of value so it will throw error
    except ValueError:
        #set flag for error is number to false
        #nastavenie flagu ako false pre chybnu hodnotu
        flag = False
    
    #overenie spravnosti vysledku pre flag
    #checking of correction of solution for flag
    if flag:
        #if true return input as a value of int
        #ak je pravdive vydaj hodnotu ako cislo
        return vstup
    else:
        #ak sa jedna o chybu vypis error a poziadaj o zadanie znova a opakuj funkciu
        #if it is false print error message an ask for input again a try to check it again
        print("Error! Value is not a number!")
        foo = input("Put a number: ")
        return je_cislo(foo)

#telo hlavnej fukcie
#body of main function
def number_guess():
    #zadanie maximalnej hodnoty pre hadanie
    #input for maximum value for search
    a= input("Maximum range for numbers: ")
    #overenie ci je vstup cislo alebo nie
    #check if input is number
    rozsah = int(je_cislo(a))

    #zadanie poctu pokusov
    #input for max amout of trys
    a = input("Max number for try: ")

    #check if vaue is valid
    try_value_max = int(je_cislo(a))

    #check if number of trys is less than maximum number
    if try_value_max > rozsah:
        print("Number of try cannot be bigger than maximum number of range. Please vrite valid value! ")
        a = input("Max number for try: ")
        try_value_max = int(je_cislo(a))
    
    #make random number
    number = random.randint(1, rozsah)

    #setting number of try
    try_value = 0

    #setting end condition
    win_cond = 0

    while (win_cond != 1):
        guess = int(input("Put number witch you think is correct: "))
        try_value += 1
        print()


        print()
        if (guess == number):
            print("Correct! Number is: " + str(number))
            print("You guess number on " + str(try_value) + " try from " + str(try_value_max) + " max ammout of try.")
            
            retry = input("Would you like to play again? [Y/n]")
            znova(retry)
            win_cond = 1
        else:
            if (try_value_max == try_value):
                win_cond = 1
                print("Incorrect! You are out of try")
            else:
                print("Incorrent you can try " + str(try_value_max - try_value) + " times")
                retry = input("Would you like to play again? [Y/n]")
                znova(retry)

                print()
                #try_value += 1

if __name__ == "__main__":
    number_guess()
