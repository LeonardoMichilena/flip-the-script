def assert_equal(result,expectation):
    if not result == expectation:
        raise AssertionError(f'''
            expected {expectation} 
            but got  {result}
        ''') 
