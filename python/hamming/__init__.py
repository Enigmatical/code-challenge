def compute(dna1 = None, dna2 = None):
    """
    Determines the Hamming distance between two DNA strands.

    Parameters
    ----------
    dna1 : str
        A string representation of a DNA strand
    dna2 : str
        A string representation of a DNA strand

    Returns
    -------
    int
        This returns the Hamming distance of two DNA strands
    """

    """Added a test to ensure both inputs are provided."""
    if dna1 is None or dna2 is None:
        raise NameError('Two DNA strands are required.')

    """Converted the strings into lists"""
    dna1 = list(dna1)
    dna2 = list(dna2)

    """Enforces the requirement that DNA must be the same length"""
    if len(dna1) != len(dna2):
        raise ValueError('DNA strands must be of equal length.')

    """Summer initialized outside the scope of the for... loop"""
    distance = 0

    """Uses enumerate() which replaces range(len()) and provides index"""
    for ind, atom1 in enumerate(dna1):
        atom2 = dna2[ind]

        if (atom1 != atom2):
            distance += 1

    return distance
