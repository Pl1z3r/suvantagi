from .base_character import Character

class PlayableCharacter(Character):
    def __init__(self) -> None:
        super().__init__()
        self.age = 11


