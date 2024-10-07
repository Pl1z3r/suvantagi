from characters import NonPlayableCharacter
from user_input import inputSelection
from sys import exit

class charHandler:
    def __init__(self) -> None:
        self.chars:dict = {}

    def listChar(self) -> None:
        for charName, char in self.chars.items():
            print(f'{charName}: {char.type[0]}, {char.rank} {char.subRank}.')

    def printCharSheet(self) -> None:
        key = inputSelection('Qual deseja imprimir?',[*self.chars.keys()])
        if key:
            print(self.chars[key[0]])    

    def createChar(self) -> None:
        newChar = NonPlayableCharacter().create(inputSelection('Criar um personagem aleatoriamente?', [False, True])[0])
        self.chars[input('Nomeie o personagem: ')] = newChar

    def dumpChar(self) -> None:
        key = inputSelection('Qual deseja deletar?',[*self.chars.keys()])
        if key:
            self.chars.pop(key[0])

    def editChar(self) -> None:
            print('Soon™')

    def menu(self) -> None:
        options:dict[str,callable] = {
            'listar personagens' : self.listChar,
            'print ficha de personagem' : self.printCharSheet,
            'criar personagem' : self.createChar,
            'apagar personagem' : self.dumpChar,
            'sair' : exit
        }
        key = inputSelection('', [*options.keys()])
        print('\n' * 100)
        options[key[0]]()
        

if __name__ == "__main__":
    menu = charHandler()
    while True:
        menu.menu()

        
