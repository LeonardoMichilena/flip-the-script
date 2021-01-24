from test.util import assert_equal
from gender_function import gender_converter


def test_gender_function():
    test_cases = [
        ['gods', 'goddesses'],
        ['Gods', 'Goddesses'],
        ['ladies', 'gentlemen'],
        ['father-in-law', 'mother-in-law'],
        ['conductors', 'conductresses'],
        ['his', 'her'],
        ['My father said he was a superwomen.', 
         'My mother said she was a supermen.'], 
        ['dudes', 'ladies']
    ]

    for inp, expectation in test_cases: 
        assert_equal(gender_converter(inp), expectation)
