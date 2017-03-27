"""Module for base_conversion method."""


def convert(input, source, target):
    """Convert input from source base to target base."""
    alphabets = {
        'bin': '01',
        'oct': '01234567',
        'dec': '0123456789',
        'hex': '0123456789abcdef',
        'allow': 'abcdefghijklmnopqrstuvwxyz',
        'allup': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'alpha': 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'alphanum': '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
    }
    if source == target:
        return
    elif len(alphabets[source]) > len(alphabets[target]):
        div = int(alphabets[source]) / int(alphabets[target])
    else:
        print alphabets[target], alphabets[source]
        div = len(alphabets[target]) / len(alphabets[source])
    return div
