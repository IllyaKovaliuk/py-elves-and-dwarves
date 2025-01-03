from app.players.elves.elf import Elf


class ElfRanger(Elf):
    def __init__(self,
                 bow_level: int,
                 nickname: str,
                 musical_instrument: str) -> None:
        super().__init__(musical_instrument, nickname)
        self.bow_level = bow_level

    def get_rating(self) -> int:
        return 3 * self.bow_level

    def player_info(self) -> str:
        return (f"Elf ranger {self.nickname}. {self.nickname} "
                f"has bow of the {self.bow_level} level")
