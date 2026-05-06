import pygame, dice

class Cup:
    def __init__(self):
        self.dice = [dice.Dice() for _ in range(5)]