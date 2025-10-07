import random
import os
#### TODO LIST ####
# -Capture input from user as parameters for password generation
# -Captured parameters will be global variables (Pwd length, Symbol use, number use, Caps use)
# -Return generated password in the console and ask to copy to clipboard 

_PWMIN = 8
_PWMAX = 28


_PW_LENGTH = 5
_SYMBOL = False
_NUMBER = False
_CAPS = False
_ANSWER = False

_PWORD = ""



### CALL TO GENERATE PASSWORD ###

def password_generation(): ## params to be used are global variables that capture user entries

    params = 1 ## default case is always going to be 1 therfore only lowercase letters will be added to the _PWORD string

    if _CAPS:
        params +=1  ## Second case adds CAPS letters to the _PWORD string 
    elif _SYMBOL:
        params +=1  ## Third case adds SYMBOLS letters to the _PWORD string
    else:
        params +=1  ## Fourth case adds NUMBERS letters to the _PWORD string
####  get json file keys for data char arrays containing UTF-8 letters, symbols and numbers for password generation.
    i = 0 ## index for pw_length
### init for loop pwd length if statements in said for,generate new random number at the start of the loop to get index from data
    while i < _PW_LENGTH:
        rnd = random.randrange(params) ## for randomness between cases

        match _CAPS:
            case True:
                pass
            case False:
                pass
        
        match _SYMBOL:
            case True:
                pass
            case False:
                pass
        
        match _NUMBER:
            case True:
                pass
            case False:
                pass

### START REGION ###

def get_letters():
    
    pass

def get_symbols():
    
    pass

def get_nums():
    
    pass

### END REGION ###



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
        password_generation()
    else: break

exit()



