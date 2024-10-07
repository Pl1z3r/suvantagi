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
