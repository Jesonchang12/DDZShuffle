from PukeGameBase import PukeGameBase
from Peasant import Peasant
from Landlord import Landlord
import random


class ThreeGame(PukeGameBase):
    def __init__(self):
        """This is 3 person Game"""
        PukeGameBase.__init__(self)
        p1 = Landlord(3, "landlord")
        p2 = Peasant(3, "peasant1")
        p3 = Peasant(3, "peasant2")
        self.players = [p1, p2, p3]
        self.cards = [x for x in range(1, 55)]

    def deliverCards(self):
        """Start deliver cards to players"""

        ll = random.randint(0, 2)
        for i in range(3):
            self.players[i].handCards = self.cards[(ll+i) % 3:-3:3]
        self.players[0].handCards += self.cards[-3:]
        for p in self.players:
            p.handCards.sort(reverse=True)
