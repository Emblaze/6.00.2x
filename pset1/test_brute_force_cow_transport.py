#!/usr/bin/env python3
import brute_force_cow_transport
import unittest


class testBruteForceCow(unittest.TestCase):

    def test_brute_force_cow(self):
        result = brute_force_cow_transport.brute_force_cow_transport({"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}, 10)
        self.assertEqual(result, [['Maggie', 'Callie'], ['Jesse', 'Maybel']])
        # [["Jesse", "Callie"], ["Maybel", "Maggie"]]
        # [["Jesse", "Maybel"],["Callie", "Maggie"]]

    def test_brute_force_cow_transport2(self):
        result = brute_force_cow_transport.brute_force_cow_transport({'Milkshake': 40, 'Horns': 25, 'Lotus': 40, 'Boo': 20, 'Miss Bella': 25, 'MooMoo': 50}, 100)
        self.assertEqual(result, [['MooMoo', 'Horns', 'Miss Bella'], ['Milkshake', 'Lotus', 'Boo']])

    def test_brute_force_cow_transport3(self):
        result = brute_force_cow_transport.brute_force_cow_transport({'Betsy': 65, 'Buttercup': 72, 'Daisy': 50}, 75)
        self.assertEqual(result, [['Buttercup'], ['Daisy'], ['Betsy']])

    def test_brute_force_cow_transport4(self):
        result = brute_force_cow_transport.brute_force_cow_transport({'Starlight': 54, 'Betsy': 39, 'Buttercup': 11, 'Luna': 41}, 145)
        self.assertEqual(result, [['Starlight', 'Betsy', 'Luna', 'Buttercup']])


if __name__ == '__main__':
    unittest.main()
