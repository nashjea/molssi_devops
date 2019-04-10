"""
util.py
A sample repository for the MolSSI Python Package Development Workshop

Misc. utility functions
"""

def title_case(sentence):
    """
    Convert a string to title case.

    Title case means that the first letter of each word is capitalized, an all other letters in the word are lowercase.

    Parameters
    ----------
    sentence: str
        String to be converted to title title case

    Returns
    -------
    ret: str
        String converted to title case.

    Example
    -------
    >>> title_case('ThIS iS a STRinG to bE ConVerTed.')
    'This Is A String To Be Converted'
    """

    # Capitalize the first letter
    ret = sentence[0].upper()

    # Loop through the rest of the characters in the string.
    for i in range(1, len(sentence)):
        if sentence[i - 1] == ' ':
            ret = ret + sentence[i].upper()
        else:
            ret = ret + sentence[i].lower()

    return ret
