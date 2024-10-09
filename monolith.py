from math import ceil
from sys import exit
import random

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

class Character:
    def __init__(self) -> None:
        self.name = ''
        self.rank:str = 'None'
        self.rankLimits:list = [0,0]

        self.atr:dict[str,int] = {
            'Forca' : 1,
            'Resis' : 1,
            'Veloc' : 1,
            'Intel' : 1,
            'Vntad' : 1,
            'Mente' : 1,
            'Spirt' : 1,
            'Sentd' : 1,
            'Cosmo' : 0
        }
        self.com:dict[str,int] = {
            'Socos' : 0,
            'Chute' : 0,
            'Armso' : 0,
            'Armas' : 0,
            'Psque' : 0
        }


class NonPlayableCharacter(Character):
    def __init__(self) -> None:
        super().__init__()
        self.subRank:str = 'None'
        self.subRankLimit:int = 0

        self.type:list = ['None']

        self.nac:dict = {}
        self.car:dict[str, list] = {'Genericas' : ['Restrição', 'Efeito Contínuo', 'Poder Passivo',
                              'Destruição de Durabilidade', 'Ataque Múltiplo',
                              'Ataque em Área', 'Energizar']}
        self.tec:list[list] = []

        self.art:dict[str, list] = {}
        self.glp:dict[str, list] = {
            'Socos' : ['Jab', 'Strong', 'Fierce'],
            'Chutes' : ['Short', 'Forward', 'Roundhouse'],
            'Arremessos' : [],
            'Bloqueios' : ['Bloqueio', 'Jump']
        }
        self.cmb:list[list] = []

    def __repr__(self) -> str:
        repr:str = f'*[FICHA DE INIMIGO]*\n\n*Classe:*\n- {self.type[0]}\n*Rank:*\n- {self.rank} {self.subRank}\n\n*Atributos:*```\n'
        for atr in self.atr.keys():
            repr += f'-{atr}: {self.atr[atr]}\n'

        repr += '```\n*Competências:*```\n'
        for com in self.com.keys():
            repr += f'-{com}: {self.com[com]}\n'

        repr += '```\n*Naturezas Cósmicas:*\n'
        if self.nac:
            for key in self.nac.keys():
                repr += f'-{key}: {self.nac[key]}\n'
        else:
            repr += '-\n'

        repr += '\n*Técnicas:*'
        if self.tec:
            for tec in self.tec:
                repr += f'\n```-{tec[0]}:```'
                for c in tec[1]:
                    repr += f'\n- {c}'
        else:
            repr += '\n-'
        repr += '\n'
        return repr

    def _selectRank(self, rand:bool) -> None:
        ranks:dict[str,list[int]] = {'Sobrehumano' : [5, 20],
                                     'Superhumano' : [20, 50],
                                     'Milagre' : [50, 70],
                                     'Divino' : [90, 200]}

        subRanks:dict[str, float] = {'Baixo' : 1/5,
                                   'Médio' : 2/5,
                                   'Alto' : 3/5,
                                   'Perfeito' : -1}

        if rand:
            rank = random.choice([*ranks.keys()])
        else:
            rank = inputSelection('Selecione o Rank do personagem.', [*ranks])[0]

        self.rank = rank
        self.rankLimits = ranks[rank]

        if rand:
            subRank = random.choice([*subRanks.keys()])
        else:
            print('\n' * 100)
            subRank = inputSelection('Selecione o SubRank do personagem.', [*subRanks.keys()])[0]
        self.subRank = subRank
        self.subRankLimit = ceil((self.rankLimits[1]-self.rankLimits[0]) * 9 * subRanks[subRank])

    def _selectType(self, rand:bool):
        types = {
            'Brutamontes' : {'atr' : ['Forca', 'Resis', 'Veloc', 'Vntad', 'Sentd', 'Mente', 'Spirt', 'Intel', 'Cosmo'],
                             'cna' : [5,3,2],
                             'com' : [3,3,2,2,1],
                             'car' : [1, 1, 2, 2, 2, 1, 3]},
            'Artista Marcial' : {'atr' : ['Veloc', 'Forca', 'Intel', 'Resis', 'Vntad', 'Sentd', 'Mente', 'Spirt', 'Cosmo'],
                                 'cna' : [3,2,5],
                                 'com' : [2,2,1,2,1],
                                 'car' : [2, 2, 1, 2, 1, 1, 2]},
            'Elemental' : {'atr' : ['Cosmo', 'Vntad', 'Sentd', 'Intel', 'Resis', 'Veloc', 'Mente', 'Spirt', 'Forca'],
                           'cna' : [3,5,2],
                           'com' : [1,1,1,1,2],
                           'car' : [1,2,1,1,2,2,1]},
            'Espiritualista' : {'atr' : ['Cosmo', 'Spirt', 'Vntad', 'Mente', 'Intel', 'Sentd', 'Resis', 'Veloc', 'Forca'],
                                'cna' : [5,3,2],
                                'com' : [1,1,1,1,2],
                                'car' : [2,1,1,1,1,2,2]},
            'Ilusionista' : {'atr' :['Intel', 'Mente', 'Spirt', 'Vntad', 'Sentd', 'Resis', 'Veloc', 'Cosmo', 'Forca'],
                             'cna' : [5,3,2],
                             'com' : [1,1,1,1,2],
                             'car' : [2,1,2,1,1,2,1]}
        }
        if rand:
            type = random.choice([*types.keys()])
        else:
            print('\n' * 100)
            type = inputSelection('Selecione o Tipo de personagem.', [*types.keys()])[0]
        self.type = [type, types[type]]

    def _selectNac(self, rand:bool) -> tuple:
        nac = {'Calor' : ['Dano Contínuo', 'Atravessar Armadura'],
               'Frio' : ['Atravessar Armadura', 'Congelamento'],
               'Relâmpago' : ['Atravessar Armadura', 'Ricochete', 'Paralisia'],
               'Água' : ['Barreira'],
               'Terra' : ['Barreira'],
               'Ar' : ['Barreira'],
               'Luz' : ['Atravessar Armadura', 'Camuflagem'],
               'Trevas' : ['Atravessar Armadura', 'Paralisia', 'Camuflagem']}

        match self.type[0]:
            case 'Ilusionista':
                nac['Ilusão'] = ['Ataque Ilusorio']
                if random.randint(0, 1):
                    return 'Ilusão', nac['Ilusão']
            case 'Espiritualista':
                nac['Sekishiki'] = ['Ataque Espiritual']
                if random.randint(0,1):
                    return 'Sekishiki', nac['Sekishiki']
        if rand:
            choice = random.choice([*nac.keys()])
        else:
            print('\n' * 100)
            choice = inputSelection('Selecione uma Natureza Cosmica para o personagem.', [*nac.keys()])[0]
        return choice, nac[choice]

    def _destributeAttributes(self, rand:bool) -> None:
        left:int = self.subRankLimit

        for key in self.type[1]['atr']:
            if left <= -1:
                self.atr[key] = self.rankLimits[1]
                continue
            if left == 0: break
            self.atr[key] = self.rankLimits[0]
            if rand:
                amount = min(random.randint(0, int(left/2)), self.rankLimits[1] - self.atr[key])
            else:
                print('\n' * 100)
                amount = inputInt(f'Distribuir pontos em {key}, {left} pontos restantes.', 0, min(self.rankLimits[1] - self.atr[key], left))
            self.atr[key] = self.atr[key] + amount
            left -= amount

    def _destributeIntelPoints(self, rand:bool) -> None:
        left:int = ceil(self.atr['Intel']/2)
        options:list[str] = ['Competencias', 'Naturezas Cosmicas', 'Artes Marciais']
        while left > 0:
            if rand:
                upgradeChoice = random.choices(options, self.type[1]['cna'])[0]
            else:
                print('\n' * 100)
                upgradeChoice = inputSelection('Evoluir capacidades.', options, repeat= -1)[0]

            match upgradeChoice:
                case 'Competencias':
                    if rand:
                        com = str(random.choices([*self.com.keys()], self.type[1]['com'])[0])
                        if self.com[com] < 5:
                            self.com[com] += 1
                            left -= 1
                    else:
                        print('\n' * 100)
                        com = str(inputSelection(f'Competência a evoluir, {left} pontos restantes.', [*self.com.keys()], repeat= -1)[0])
                        amount = inputInt('Quantos pontos usar.', 0, min(5 - self.com[com], left))
                        self.com[com] = self.com[com] + amount
                        left -= amount
                case 'Naturezas Cosmicas':
                    if rand:
                        if random.randint(1,3) % 2 == 0 and self.nac.keys():
                            nac = random.choice([*self.nac.keys()])
                            self.nac[nac] = min(self.nac[nac] + 1, 3)
                            left -=1
                        else:
                            nac = self._selectNac(rand)
                            if nac[0] in self.nac.keys():
                                if self.nac[nac[0]] < 3:
                                    self.nac[nac[0]] += 1
                                    left -= 1
                            else:
                                self.nac[nac[0]] = 1
                                self.car[nac[0]] = nac[1]
                                left -= 1

                    else:
                        nac = self._selectNac(rand)
                        if nac[0] in self.nac.keys():
                            if self.nac[nac[0]] < 3:
                                print('\n' * 100)
                                amount = inputInt('Quantos pontos usar.', 0, min(3 - self.nac[nac[0]], left))
                                self.nac[nac[0]] += amount
                                left -= amount
                        else:
                            print('\n' * 100)
                            amount = inputInt('Quantos pontos usar.', 0, min(3, left))
                            self.nac[nac[0]] = amount
                            self.car[nac[0]] = nac[1]
                            left -= amount

                case 'Artes Marciais':
                    pass

    def create(self, rand:bool = False) -> object:
        print('\n' * 100)
        if self.type[0] == 'None': self._selectType(inputSelection('Selecionar classe aleatoriamente?', [False, True])[0])
        print('\n' * 100)
        if self.rank == 'None' or self.subRank == 'None': self._selectRank(False)
        print('\n' * 100)
        self._destributeAttributes(rand)
        print('\n' * 100)
        self._destributeIntelPoints(rand)

        #tec
        if self.nac:
            if rand:
                for _ in range(0, self.atr['Intel']//10):
                    nac = random.choice([*self.nac.keys()])
                    car = self.car['Genericas'] + self.car[nac]
                    tec = [nac, random.choices(car,self.type[1]['car']+[2]*len(self.car[nac]),k=self.nac[nac]+1)]
                    for n in range(0,len(tec[1])):
                        if tec[1].count(tec[1][n]) > 1:
                            tec[1][n] = 'Potencializar Dano'
                    self.tec.append(tec)
            else:
                pass
        return self



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

        
