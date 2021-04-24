import unittest
import neutral_function
from neutral_function import dict_neutral

class TestCalc(unittest.TestCase):

    def test_neutral_converter(self):
        ### Femenine and masculine nouns
        self.assertEqual(neutral_function.neutral_converter('woman', dict_neutral), 'person')
        self.assertEqual(neutral_function.neutral_converter('policeman', dict_neutral), 'police officer')
        ### Proof of exceptions, i.e. proper noun vs. common noun United Kingdom vs. a kingdom
        self.assertEqual(neutral_function.neutral_converter('She is living in the United Kingdom.', dict_neutral), 'They are living in the United Kingdom.')
        ### Not including exceptions
        self.assertEqual(neutral_function.neutral_converter('His Kingdom was the most powerful.', dict_neutral), 'Their Realm was the most powerful.')
        ### Converting "her" into "them" and "their"
        self.assertEqual(neutral_function.neutral_converter('Mrs Clark called her up.', dict_neutral), 'Mx Clark called them up.')
        self.assertEqual(neutral_function.neutral_converter('Ms Byron called her father.', dict_neutral), 'Mx Byron called their parent.')
        ### Plural nouns and adjectives with gender connotation
        self.assertEqual(neutral_function.neutral_converter('Girls are always so bossy.', dict_neutral), 'Kiddos are always so assertive.')
        ### Yes/No question using 3rd singular person pronoun and to be verb 
        self.assertEqual(neutral_function.neutral_converter('Is she engaged to a congressman?', dict_neutral), 'Are they engaged to a member of congress?')
        ### Two cases: (1) 3rd singular person pronoun + (2) possesive pronoun + to be verb
        self.assertEqual(neutral_function.neutral_converter('''She's read every book written by him. His are bestsellers everywhere.''', dict_neutral), '''They've read every book written by them. Theirs are bestsellers everywhere.''')


if __name__ == '__main__':
    unittest.main()