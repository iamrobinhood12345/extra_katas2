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
    print num_dec

    def convert_from_dec(convert):
        """Convert decimal form of input to target."""
        if target == 'dec':
            return str(convert)
        num = ''
        div = 0
        power = 0
        while True:
            div = len(alphabets[target]) ** power
            if div > convert:
                power -= 1
                break
            power += 1
        remainder = convert
        while power >= 0:
            num += str(remainder / (len(alphabets[target]) ** power))
            remainder = remainder % (len(alphabets[target]) ** power)
            power -= 1
        return num

    num_target = convert_from_dec(num_dec)

    return num_target
