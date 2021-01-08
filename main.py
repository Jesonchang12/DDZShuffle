# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import cv2
from ThreeGame import ThreeGame
from FourGame import FourGame


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    game = FourGame()
    # game = ThreeGame()
    game.shuffleCards()
    game.deliverCards()
    for p in game.players:
        img = p.getCards()
        cv2.imwrite(p.getPlayerName()+".jpg", img)
        cv2.imshow(p.getPlayerName(), img)
    cv2.waitKey()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
