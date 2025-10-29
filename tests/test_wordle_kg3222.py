from wordle_kg3222.wordle_kg3222 import validate_guess, check_guess

def test_validate_guess():
    """
    -Valid guesses: the correct word with lowercase, 5 letters, alphabetic
    """
    assert validate_guess("crane") is True
    """
    -Invalid guesses: wrong length, i.e. 3 letters
    """
    assert validate_guess("cat") is False
    """
    -Invalid guesses: uppercase
    """
    assert validate_guess("CRANE") is False
    """
    -Invalid guesses: non-alphabetic, i.e. numbers string
    """
    assert validate_guess("12345") is False
    """
    -Edge case: empty string
    """
    assert validate_guess("") is False
    """
    -Edge case: none
    """
    assert validate_guess(None) is False
    """
    -Edge case: none-string, i.e. numeric input
    """
    assert validate_guess(12345) is False

    
def test_check_guess_basic():
    """
    Test basic check_guess functionality.
    """
    """
    - Perfect match (all green): guess the exact word and get all green result.
    """
    result = check_guess("crane", "crane")
    expected = [('c','green'), ('r','green'), ('a','green'), ('n','green'), ('e','green')]
    assert result == expected
    """
    - No matches (all gray): guess a word that has no letter right.
    """
    result = check_guess("crane", "moist")
    expected = [('m','gray'), ('o','gray'), ('i','gray'), ('s','gray'), ('t','gray')]
    assert result == expected
    """
    - Mixed results (green, yellow, gray combinations): guess a word that has correct and incorrect alphabets at the same time 
    """
    result = check_guess("crane", "cream")
    expected = [('c','green'), ('r','green'), ('e','yellow'), ('a','yellow'), ('m','gray')]
    assert result == expected
    """
    - Edge cases (different lengths): wrong length, i.e. 3 letters
    """
    result = check_guess("crane", "cat")
    assert result == []