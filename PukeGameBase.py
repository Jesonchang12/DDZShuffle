import random


class PukeGameBase:
    def __init__(self):
        """ This is game base"""
        self.players = []
        self.cards = []
        # self.playerCards = {}

    def shuffleCards(self):
        """Start shuffle cards"""

        if (len(self.players) == 3) and (len(self.cards) == 54):
            print("mode:", 3)
            pass
        elif (len(self.players) == 4) and (len(self.cards) == 108):
            print("mode:", 4)
            pass
        else:
            return

        random.shuffle(self.cards)

    def deliverCards(self):
        """Start deliver cards"""
        print("Start deliver cards")

    # def dealCards(self):
    #     for k, v in self.playerCards.items():
    #         print("Player name: %\n" % k.name)
    #         for x in v:
    #             print("Cards: {}".format(x), end=' ')
    #         print('\n')

