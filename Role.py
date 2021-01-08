import cv2
import numpy as np


class Role:
    def __init__(self, mode, name):
        """Create a Role"""
        self.mode = mode
        self.name = name
        self.handCards = []

    def getPlayerName(self):
        return self.name

    def getCards(self):
        """ Get cards"""
        # if self.mode == 3:
        #     print("3:" + self.name)
        # else:
        #     print("4:" + self.name)
        print(self.name)

        return self._outputCards()

    def _outputCards(self):
        """Output hand cards"""
        count = len(self.handCards)
        img = np.zeros((150, 80 + 25 * count, 3), np.uint8)
        for i in range(count):
            img0 = cv2.imread("./pukeImage/{}.jpg".format(self.handCards[i]))
            img[0:150, i * 25:i * 25 + 105] = img0
        # deprecated
        # img = cv2.imread("./pukeImage/" + str(self.handCards[0]) + ".jpg")
        # for i in range(1, len(self.handCards)):
        #     img = cv2.hconcat([img, cv2.imread("./pukeImage/" + str(self.handCards[i]) + ".jpg")])
        # For test
        for n in self.handCards:
            value = Role._getCardValue(n)
            tp = Role._getCardType(n)
            print(value + tp, end=' ')
        print('\n' + str(len(self.handCards)))
        # print('\n')

        return img

    @classmethod
    def _getCardValue(cls, n):
        if n == 53:
            value = "Little Joker"
        elif n == 54:
            value = "Big Joker"
        else:
            value = (n - 1) // 4
            if value < 8:
                value += 3
            else:
                if value == 8:
                    value = "J"
                elif value == 9:
                    value = "Q"
                elif value == 10:
                    value = "K"
                elif value == 11:
                    value = "A"
                elif value == 12:
                    value = 2

        # print(str(n)+":", end='')
        # print(n, ":", end='')
        return str(value)
        print("kkk")

    @classmethod
    def _getCardType(cls, n):
        if n > 52:
            return ""

        t = n % 4
        if t == 1:
            return "♦"
        elif t == 2:
            return "♣"
        elif t == 3:
            return "♥"
        elif t == 0:
            return "♠"
