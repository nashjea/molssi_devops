"""
molssi_math.py
A sample repo for the 2019 MolSSI Software Fellow Bootcamp

Handles the primary functions
"""


def mean(num_list):
    """
    Computes the mean of a list of numbers.

    Parameters
    ----------
    num_list: list
        List to calculate mean of

    Returns
    -------
    list_mean: float
        Mean of list of numbers
    """

    # Check that input is type list
    if not isinstance(num_list, list):
        raise TypeError('Invalid input %s - must be type list' % (num_list))
    # Check that list has length greater than 0
    if len(num_list) == 0:
        raise ZeroDivisionError('Cannot calculate mean of empty list.')

    list_mean = sum(num_list) / len(num_list)

    return list_mean


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
