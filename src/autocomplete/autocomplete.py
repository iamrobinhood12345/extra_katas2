"""Module for autocomplete class."""


class AutoCompleter(object):
    """Autcompleter Class."""

    def __init__(self, vocabulary, max_completions=5):
        """Initialize the Autocompleter class."""
        self._vocabulary = vocabulary
        self._max_completions = max_completions

    def complete(self, prefix):
        """Return list of autocomplete words."""
        words = list(set([word for word in self._vocabulary if word.startswith(prefix)]))
        if len(words) <= self._max_completions:
            return words
        else:
            return words[:self._max_completions]
