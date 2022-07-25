def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_freq = {}
    for ltr in phrase:
        if letter_freq.get(ltr):
            letter_freq[ltr] += 1
        else:
            letter_freq[ltr] = 1
    return letter_freq