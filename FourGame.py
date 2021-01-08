from PukeGameBase import PukeGameBase
from Peasant import Peasant
from Landlord import Landlord
import random


class FourGame(PukeGameBase):
    def __init__(self):
        """This is 4 person Game"""
        PukeGameBase.__init__(self)
        p1 = Landlord(4, "landlord")
        p2 = Peasant(4, "peasant1")
        p3 = Peasant(4, "peasant2")
        p4 = Peasant(4, "peasant3")
        self.players = [p1, p2, p3, p4]
        self.cards = [x for x in range(1, 55)]*2

    def deliverCards(self):
        """Start deliver cards to players"""

        ll = random.randint(0, 3)
        for i in range(4):
            self.players[i].handCards = self.cards[(ll+i) % 4:-8:4]
        self.players[0].handCards += self.cards[-8:]
        for p in self.players:
            p.handCards.sort(reverse=True)
