
def inputSelection(prompt:str, options:list, amount:int=1, repeat:int=1) -> list:
    '''
    Prompts the user to select a specified number of options from a given list.
    
    Parameters:
        options (list): The list of options to choose from.
        amount (int, optional): The number of options to select. Default is 1.
     repeat (int, optional): The maximum number of times an option can be selected. Default is 1.
    
    Returns:
        list: A list of selected options.
    '''
    if len(options) == 0:
        print('lista vazia...')
        return None
    chosen:list = []
    print(prompt)
    while amount > 0:
        print(f'Choose {amount}:')
        
        for i in range(0,len(options)):
            print(f'{i}: {options[i]}')
        userChoice:str = input('>>')

        try:
            choice = int(userChoice)
            if choice < 0 or choice >= len(options):
                raise IndexError
        except ValueError:
            print(f"ValueError: '{userChoice}' is Not a Number.")
            continue
        except IndexError:
            print(f"IndexError: '{choice}' is not an option.")   
            continue
        if chosen.count(options[choice])+1 >= repeat and repeat != -1:
            chosen.append(options.pop(choice))
        else:
            chosen.append(options[choice])
        amount -= 1
    return chosen

def inputInt(prompt:str, min:int, max:int) -> int:
    '''
    Asks for and returns an user integer input between a min and a max value.
    '''
    print(prompt)
    while True:
        print(f"Choose a number >= '{min}' and <= '{max}'.")
        try:
            userInput:str = input('>>')
            userInt:int = int(userInput)
            if min > userInt or userInt > max: raise IndexError
            return userInt
        except ValueError:
            print(f"ValueError: '{userInput}' is Not a Number.")
            continue
        except IndexError:
            print(f"IndexError: '{userInt}' is not in the range of options.")
            continue

