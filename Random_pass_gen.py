import random
import os
#### TODO LIST ####
# -Capture input from user as parameters for password generation
# -Captured parameters will be global variables (Pwd length, Symbol use, number use, Caps use)
# -Return generated password in the console and ask to copy to clipboard 

_PWMIN = 8
_PWMAX = 28


_PW_LENGTH = 0
_SYMBOL = False
_NUMBER = False
_CAPS = False
_ANSWER = False

_PWORD = ""

### CALL TO GENERATE PASSWORD ###

def password_generation(plength:str, psymbol:bool, pnumber:bool, pcaps:bool ):

####  get json file keys for data char arrays containing UTF-8 letters, symbols and numbers for password generation.

### init for loop pwd length if statements in said for,generate new random number at the start of the loop to get index from data
    if _SYMBOL:
        pass
    elif _CAPS:
        pass
    elif _NUMBER:
        pass
        

# Loop while _ANSWER is true to repeat program until user selects the exit option 

while not _ANSWER :
    # Contextual menu for the console
    print("     ###############################")
    print("     ### Welcome to the password ###")
    print("     ###         generator       ###")
    print("     ############################### \n ")
    print("     Please select one of the \n     following options: ")
    print("     (1) - Start the password generator\n     (0) - Exit the password generator")
    #captures answer
    _ANSWER = bool(input("      : "))

    #Checks if _ANSWER is True or False for program continuance
    if _ANSWER:
        
        ### Param violation check
        
        # Param input for pwsd length
        while(_PW_LENGTH < _PWMIN or _PW_LENGTH > _PWMAX):
            print(f"    Minimal password length is {_PWMIN} and Max password lenght is {_PWMAX}")
            _PW_LENGTH = int(input("    Set password length\n   :"))
        ## end
        
        # Param input for symbol use
        _SYMBOL = bool(input("    Would you like to use Symbols y/n\n   :  ")) 
        # Param input for symbol use
        _NUMBER = bool(input("    Would you like to use Numbers y/n\n   :"))
        # Param input for symbol use
        _CAPS = bool(input("    Would you like to use CAPS y/n\n   :"))
        password_generation(_PW_LENGTH, _SYMBOL, _NUMBER, _CAPS)
    else: break

exit()



