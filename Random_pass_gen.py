import secrets
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

### CALL TO GENERATE PASSWORD ###

def password_generation(pcase): ## pcase holds is sort of like an id for each case 
                                ##ex: user says yes to symbols but no to caps and numbers 
                                ## therfore case list will only include [1(default id), 3,(id for symbols)]

        ####  get json file keys for data char arrays containing UTF-8 letters and symbols for password generation, 
        ###   numbers will be randomly generated from 0-9 with the random library.
    i = 0 ## out of bounds mesure

    password = ""

    while i < _PW_LENGTH+1:
        rnd = secrets.choice(pcase) ## for randomness between cases
        for num in pcase:
            if num == rnd:
                match rnd:
                    case 1:
                        x = 0
                        ls:list = [0]
                        letters:list[chr] = get_letters()
                        for c in letters:
                            x+=1
                            ls.append(x)
                        password += letters[secrets.choice(ls)]
                        i += 1
                        break
                    case 2:
                        x = 0
                        ls:list = [0]
                        caps:list[chr] = get_letters()
                        for c in letters:
                            x+=1
                            ls.append(x)
                        password += caps[secrets.choice(ls)].capitalize()
                        i +=1
                        break
                    case 3:
                        x = 0
                        ls:list = [0]
                        symbols:list[chr] = get_symbols()
                        for s in symbols:
                            x+=1
                            ls.append(x)
                        password += symbols[secrets.choice(ls)]
                        i +=1
                        break
                    case 4:
                        x = secrets.choice([0,1,2,3,4,5,6,7,8,9])
                        password += str(x)
                        i +=1
                        break
    return password


### START REGION ###

## functions to get the date from the json file

def get_letters(): ## gets the letters form the .json file 
    with open('ressources\data.json', 'r') as file:
        data = file.read()
        letters = json.loads(data)
    return letters['letters']
    

def get_symbols(): ## gets the letters form the .json file
    with open('ressources\data.json', 'r') as file:
        data = file.read()
        symbols = json.loads(data)
    return symbols['symbols']

### END REGION ###

# Loop while _ANSWER is true to repeat program until user selects the exit option 

while  True:
    # Contextual menu for the console
    print("     ###############################")
    print("     ### Welcome to the password ###")
    print("     ###         generator       ###")
    print("     ############################### \n ")
    print("     Please select one of the \n     following options: ")
    print("     (1) - Start the password generator\n     (0) - Exit the password generator")
    #captures answer
    answer = bool(int(input("      :")))


    #Checks if _ANSWER is True or False for program continuance
    if answer:
        
        ### Param violation check
        
        # Param input for pwsd length
        while(_PW_LENGTH < _PWMIN or _PW_LENGTH > _PWMAX):
            print(f"    Minimal password length is {_PWMIN} and Max password lenght is {_PWMAX}")
            _PW_LENGTH = int(input("    Set password length\n   :"))
        ## end
        
        # Param input for symbol use
        _SYMBOL = bool(input("    Would you like to use Symbols y/n:")) 
        # Param input for symbol use
        _NUMBER = bool(input("    Would you like to use Numbers y/n:"))
        # Param input for symbol use
        _CAPS = bool(input("    Would you like to use CAPS y/n:"))
        
        case_list = [1]         ## default case 1 is random letters 

        if _CAPS:
            case_list.append(2)  ## Second case adds CAPS letters to the _PWORD string 
        if _SYMBOL:
            case_list.append(3)  ## Third case adds SYMBOLS letters to the _PWORD string
        if _NUMBER:
            case_list.append(4)  ## Fourth case adds NUMBERS letters to the _PWORD string
            
        print(f"This is your password:{password_generation(case_list)}")
    else: break
exit()



