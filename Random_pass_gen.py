import random
import json
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

def password_generation(pcase): ## pcase holds is sort of like an id for each case ex: user says yes to symbols but no to caps and numbers therfoce case list will only include [1(default id), 3,(id for symbols)]

####  get json file keys for data char arrays containing UTF-8 letters and symbols for password generation, numbers will be randomly generated from 0-9 with the random library.
    i = 0 ## out of bounds mesure

    while i < _PW_LENGTH:
        rnd = random.randint(pcase[0],pcase[len(pcase)-1]) ## for randomness between cases
        for num in pcase:
            if num == rnd:
                match rnd:
                    case 1:
                        print('lowercase')
                        i +=1
                        break
                    case 2:
                        print('caps')
                        i +=1
                        break
                    case 3:
                        print('symbol')
                        i +=1
                        break
                    case 4:
                        print('numbers')
                        i +=1
                        break


### START REGION ###

## functions to get the date from the json file

def get_letters(): ## gets the letters form the .json file 
    with open('ressources\data.json', 'r') as file:
        data = file.read()
        letters = json.loads(data)
    return letters['letters']
    

def get_symbols(): ## gets the letters form the .json file
    with open('.\ressources\data.json', 'r') as file:
        data = file.read()
        symbols = json.loads(data)
    return symbols['symbols']

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
        case_list = [1]
        # Param input for symbol use
        _SYMBOL = bool(input("    Would you like to use Symbols y/n\n   :  ")) 
        # Param input for symbol use
        _NUMBER = bool(input("    Would you like to use Numbers y/n\n   :"))
        # Param input for symbol use
        _CAPS = bool(input("    Would you like to use CAPS y/n\n   :"))
        
        if _CAPS:
            case_list.append(2)  ## Second case adds CAPS letters to the _PWORD string 
        elif _SYMBOL:
            case_list.append(3)  ## Third case adds SYMBOLS letters to the _PWORD string
        elif _NUMBER:
            case_list.append(4)  ## Fourth case adds NUMBERS letters to the _PWORD string
            
        password_generation()
    else: break
exit()



