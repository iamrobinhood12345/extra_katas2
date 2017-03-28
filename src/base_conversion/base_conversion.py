"""Module for base_conversion method."""


def convert(input_, source, target):
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

    if source == target:
        return
    elif len(alphabets[source]) > len(alphabets[target]):
        long_base = source
        long_len = len(alphabets[source])
        small_base = target
        small_len = len(alphabets[target])
    else:
        long_base = target
        long_len = len(alphabets[target])
        small_base = target
        small_len = len(alphabets[source])

    def convert_to_dec(convert):
        """Convert the input to decimal."""
        if source == 'dec':
            return convert
        num = 0
        power = len(convert) - 1
        for each in convert:
            num += (alphabets[source].index(each)) * ((len(alphabets[source])) ** power)
            power -= 1
        return num

    num_dec = convert_to_dec(input_)

    def convert_from_dec(convert):
        """Convert decimal form of input to target."""
        if target == 'dec':
            return str(convert)
        num = 0
        div = 0
        power = 0
        while True:
            if div > convert:
                break
            first_div = len(alphabets[target]) ** power
            power += 1
        while power > 0:
            num = convert / first_div
            remainder = convert % first_div
        return str(num)

    num_target = convert_to_dec(num_dec)

    return div, long_base, small_base, num_target
