"""Test the string pyramid module."""

import pytest


PARAMS_SIDE = [
    (None, None),
    ('', ''),
    ('#', '#'),
    ('#*', ' * \n###'),
    ('abc', '  c  \n bbb \naaaaa')
]

PARAMS_ABOVE = [
    (None, None),
    ('', ''),
    ('#', '#'),
    ('#*', '###\n#*#\n###'),
    ('abc', 'aaaaa\nabbba\nabcba\nabbba\naaaaa')
]

PARAMS_COUNT_VISIBLE = [
    (None, -1),
    ('', -1),
    ('#', 1),
    ('#*', 9),
    ('abc', 25)
]

PARAMS_COUNT_ALL = [
    (None, -1),
    ('', -1),
    ('#', 1),
    ('#*', 10),
    ('abc', 35)
]


@pytest.mark.parametrize('characters, result', PARAMS_SIDE)
def test_side(characters, result):
    """Test view from side."""
    from string_pyramid import watch_pyramid_from_the_side
    assert watch_pyramid_from_the_side(characters) == result


@pytest.mark.parametrize('characters, result', PARAMS_ABOVE)
def test_above(characters, result):
    """Test view from above."""
    from string_pyramid import watch_pyramid_from_above
    assert watch_pyramid_from_above(characters) == result


@pytest.mark.parametrize('characters, result', PARAMS_COUNT_VISIBLE)
def test_count_visible(characters, result):
    """Test count visible blocks in pyramid."""
    from string_pyramid import count_visible_characters_of_the_pyramid
    assert count_visible_characters_of_the_pyramid(characters) == result


@pytest.mark.parametrize('characters, result', PARAMS_COUNT_ALL)
def test_count_all(characters, result):
    """Test count all blocks in pyramid."""
    from string_pyramid import count_all_characters_of_the_pyramid
    assert count_all_characters_of_the_pyramid(characters) == result
