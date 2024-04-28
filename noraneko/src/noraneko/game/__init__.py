# from uuid import uuid4


# class Card: ...


# class Player:
#     def __init__(self, uid: str) -> None:
#         self.uid = uid
#         self.hand: list[Card] = []
#         self.graveyard: list[Card] = []
#         self.deck: list[Card] = []


# class Game:
#     def __init__(self, players: tuple[str, str]) -> None:
#         self.players = players
#         self.uid = str(uuid4())


# class GameStore:
#     def __init__(self) -> None:
#         self.games: list[Game] = []

#     def create(self, players: tuple[str, str]) -> str:
#         game = Game(players)
#         self.games.append(game)
#         return game.uid
