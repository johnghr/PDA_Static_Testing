import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_game = CardGame()


    def test_check_for_ace(self):
        card = Card("diamond", 1)
        self.assertEqual(True, self.card_game.check_for_ace(card))

    def test_highest_card(self):
        card1 = Card("heart", 2)
        card2 = Card("spade", 3)
        result = self.card_game.highest_card(card1, card2)
        self.assertEqual(3, result.value)

    def test_cards_total(self):
        card1 = Card("heart", 2)
        card2 = Card("spade", 3)
        cards = [card1, card2]
        self.assertEqual("You have a total of 5", self.card_game.cards_total(cards))