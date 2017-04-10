"""Test module for autocomplete."""

import pytest

VOCABULARY = ['fix', 'fax', 'fit', 'fist', 'full', 'finch', 'final', 'finial']

PARAMS_TEST_FILLED_AUTO_COMPLETER = [
    ('f', ['fist', 'finch', 'finial', 'fix', 'fax']),
    ('fi', ['fist', 'finial', 'fix', 'finch', 'fit']),
    ('fin', ['finch', 'final', 'finial']),
    ('finally', []),
]

PARAMS_TEST_NUMBER_MAX_NONE = [
    ('f', 5),
    ('fi', 5),
    ('fin', 3),
    ('finally', 0),
]

PARAMS_TEST_NUMBER_MAX_1 = [
    ('f', 1),
    ('fi', 1),
    ('fin', 1),
    ('finally', 0),
]

PARAMS_TEST_NUMBER_MAX_3 = [
    ('f', 3),
    ('fi', 3),
    ('fin', 3),
    ('finally', 0),
]

PARAMS_TEST_NUMBER_MAX_6 = [
    ('f', 6),
    ('fi', 6),
    ('fin', 3),
    ('finally', 0),
]

PARAMS_TEST_NUMBER_MAX_10 = [
    ('f', 8),
    ('fi', 6),
    ('fin', 3),
    ('finally', 0),
]

PARAMS_TEST_STARTSWITH = [
    ('f'),
    ('fi'),
    ('fin'),
    ('finally'),
]


@pytest.fixture
def filled_autocompleter():
    """Return an initialized autocompleter class."""
    from autocomplete import AutoCompleter
    return AutoCompleter(VOCABULARY)


@pytest.fixture
def max_1():
    """Return a low max completions auto completer."""
    from autocomplete import AutoCompleter
    return AutoCompleter(VOCABULARY, 1)


@pytest.fixture
def max_3():
    """Return max of 3 completions auto completer."""
    from autocomplete import AutoCompleter
    return AutoCompleter(VOCABULARY, 3)


@pytest.fixture
def max_6():
    """Return max of 6 completions auto completer."""
    from autocomplete import AutoCompleter
    return AutoCompleter(VOCABULARY, 6)


@pytest.fixture
def max_10():
    """Return max of 10 completions auto completer."""
    from autocomplete import AutoCompleter
    return AutoCompleter(VOCABULARY, 10)


@pytest.mark.parametrize("n, result", PARAMS_TEST_FILLED_AUTO_COMPLETER)
def test_complete_returns_list(n, result, filled_autocompleter):
    """Test complete function."""
    assert type(filled_autocompleter.complete(n)) == list


@pytest.mark.parametrize("n, result", PARAMS_TEST_NUMBER_MAX_NONE)
def test_max_none_autocomplete(n, result, filled_autocompleter):
    """Test number returned."""
    assert len(filled_autocompleter.complete(n)) == result


@pytest.mark.parametrize("n, result", PARAMS_TEST_NUMBER_MAX_1)
def test_max_1_autocomplete(n, result, max_1):
    """Test number returned."""
    assert len(max_1.complete(n)) == result


@pytest.mark.parametrize("n, result", PARAMS_TEST_NUMBER_MAX_3)
def test_max_3_autocomplete(n, result, max_3):
    """Test number returned."""
    assert len(max_3.complete(n)) == result


@pytest.mark.parametrize("n, result", PARAMS_TEST_NUMBER_MAX_6)
def test_max_6_autocomplete(n, result, max_6):
    """Test number returned."""
    assert len(max_6.complete(n)) == result


@pytest.mark.parametrize("n, result", PARAMS_TEST_NUMBER_MAX_10)
def test_max_10_autocomplete(n, result, max_10):
    """Test number returned."""
    assert len(max_10.complete(n)) == result


@pytest.mark.parametrize("n", PARAMS_TEST_STARTSWITH)
def test_all_startswith_prefix(n, filled_autocompleter):
    """Test complete function returns words that start with prefix."""
    assert all([each.startswith(n) for each in filled_autocompleter.complete(n)])


def test_nothing_startswith(filled_autocompleter):
    """Test complete function returns an empty list when no word starts with prefix."""
    assert not filled_autocompleter.complete('a')
