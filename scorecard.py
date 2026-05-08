import pygame

class Scorecard:
    def __init__(self):
        self.scores = {
            "ones": None,
            "twos": None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
            "three_of_a_kind": None,
            "four_of_a_kind": None,
            "full_house": None,
            "small_straight": None,
            "large_straight": None,
            "kniffel": None,
            "chance": None
        }


def draw(window, position=(50, 50), size=(600, 600), color=(200, 200, 200)):
        pygame.draw.rect(window, color, (*position, *size)) #Hintergrund der Scorecard