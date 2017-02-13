"""Module for string pyramid."""


def watch_pyramid_from_the_side(characters):
    """View pyramid from the side."""
    if characters is None:
        return None
    if characters == '':
        return ''
    side = ''
    for i in range(len(characters) - 1, -1, -1):
        side += ' ' * i + characters[i] * ((len(characters) - i) * 2 - 1) + ' ' * i + '\n'
    return side[:-1]


def watch_pyramid_from_above(characters):
    """View pyramid from above."""
    if characters is None:
        return None
    if characters == '':
        return ''
    above = ''
    for i in range(len(characters)):
        above += characters[:i] + (characters[i] * ((len(characters) * 2 - 1) - i * 2)) + characters[:i][::-1] + '\n'
    for i in range(len(characters) - 2, -1, -1):
        above += characters[:i] + (characters[i] * ((len(characters) * 2 - 1) - i * 2)) + characters[:i][::-1] + '\n'
    return above[:-1]


def count_visible_characters_of_the_pyramid(characters):
    """Number of visible blocks of the pyramid."""
    if characters is None:
        return -1
    if characters == '':
        return -1
    return (len(characters) * 2 - 1) ** 2


def count_all_characters_of_the_pyramid(characters):
    """Number of blocks of the pyramid."""
    if characters is None:
        return -1
    if characters == '':
        return -1
    return sum([i ** 2 for i in [(j * 2) -1 for j in range(1, len(characters) +1)]])
