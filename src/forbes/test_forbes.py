"""Test forbes."""

import pytest
from forbes import oldest_and_youngest


def test_oldest_and_youngest():
    """Test the oldest and yougnest function."""
    assert oldest_and_youngest() == ({'name': 'Phil Knight', 'net_worth (USD)': 24400000000, 'source': 'Nike'}, {'name': 'Mark Zuckerberg', 'net_worth (USD)': 44600000000, 'source': 'Facebook'})
