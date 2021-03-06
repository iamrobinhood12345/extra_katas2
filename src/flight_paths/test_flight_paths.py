"""Test module for flight_paths.py."""

import pytest
import sys

AIRPORTS = "airports.json"


def test_get_data_from_json_file():
    """Test that the airport-data JSON file imports."""
    from flight_paths import get_data_from_json_file
    data = get_data_from_json_file(AIRPORTS)
    assert type(data) == list
    assert data[0] == {"city": "Fart", "destination_cities": ["New York City", "Code Fellows", "Atlantis", "Ben"], "lat_lon": [0.0, 0.0]}, {"city": "New York City", "destination_cities": [], "lat_lon": [10.0, 0.0]}


def test_data_converted_to_dict():
    """Test that read data converts to dictionary."""
    from flight_paths import format_data
    airports_dict = format_data(AIRPORTS)
    assert type(airports_dict) == dict
    assert airports_dict["Iraq"] == {'destination_cities': [u'Heck'], 'lat_lon': [50.0, 0.0]}


def test_airports_graph():
    """Test airports_graph is graph."""
    from flight_paths import airports
    airports_graph = airports(AIRPORTS)
    assert str(type(airports_graph)) == "<class 'weighted_graph.Graph'>"


def test_airports_graph_nodes():
    """Test airport graph content from the airport data."""
    from flight_paths import airports
    airports_graph = airports(AIRPORTS)
    if sys.version_info[0] == 2:
        assert airports_graph.nodes() == [u'Jerusalem', u'Ben', u'Code Fellows', u'New York City', u'Dagobah', u'Fart', u'Heck', u'Atlantis', u'Iraq']
    else:
        assert airports_graph.nodes() == ['Fart', 'New York City', 'Code Fellows', 'Atlantis', 'Ben', 'Jerusalem', 'Dagobah', 'Iraq', 'Heck']


def test_airports_graph_edges():
    """Test airport graph content from the airport data."""
    from flight_paths import airports
    airports_graph = airports(AIRPORTS)
    if sys.version_info[0] == 2:
        assert airports_graph.edges() == [(u'Jerusalem', (u'Ben', 2072.8048761211194)), (u'Ben', (u'New York City', 690.9349587070396)), (u'Ben', (u'Code Fellows', 690.9349587070396)), (u'Ben', (u'Atlantis', 690.9349587070396)), (u'Ben', (u'Jerusalem', 2072.8048761211194)), (u'Code Fellows', (u'New York City', 1381.8699174140793)), (u'Code Fellows', (u'Atlantis', 0.0)), (u'Code Fellows', (u'Ben', 690.9349587070396)), (u'Dagobah', (u'Code Fellows', 3454.6747935351987)), (u'Dagobah', (u'Atlantis', 3454.6747935351987)), (u'Dagobah', (u'Ben', 2763.7398348281586)), (u'Fart', (u'New York City', 690.9349587070396)), (u'Fart', (u'Code Fellows', 2072.8048761211194)), (u'Fart', (u'Atlantis', 2072.8048761211194)), (u'Fart', (u'Ben', 1381.8699174140793)), (u'Heck', (u'Iraq', 690.9349587070396)), (u'Atlantis', (u'New York City', 1381.8699174140793)), (u'Atlantis', (u'Code Fellows', 0.0)), (u'Atlantis', (u'Fart', 2072.8048761211194)), (u'Atlantis', (u'Ben', 690.9349587070396)), (u'Iraq', (u'Heck', 690.9349587070396))]
    else:
        assert airports_graph.edges() == [('Fart', ('New York City', 690.9349587070396)), ('Fart', ('Code Fellows', 2072.8048761211194)), ('Fart', ('Atlantis', 2072.8048761211194)), ('Fart', ('Ben', 1381.8699174140793)), ('Code Fellows', ('New York City', 1381.8699174140793)), ('Code Fellows', ('Atlantis', 0.0)), ('Code Fellows', ('Ben', 690.9349587070396)), ('Atlantis', ('New York City', 1381.8699174140793)), ('Atlantis', ('Code Fellows', 0.0)), ('Atlantis', ('Fart', 2072.8048761211194)), ('Atlantis', ('Ben', 690.9349587070396)), ('Ben', ('New York City', 690.9349587070396)), ('Ben', ('Code Fellows', 690.9349587070396)), ('Ben', ('Atlantis', 690.9349587070396)), ('Ben', ('Jerusalem', 2072.8048761211194)), ('Jerusalem', ('Ben', 2072.8048761211194)), ('Dagobah', ('Code Fellows', 3454.6747935351987)), ('Dagobah', ('Atlantis', 3454.6747935351987)), ('Dagobah', ('Ben', 2763.7398348281586)), ('Iraq', ('Heck', 690.9349587070396)), ('Heck', ('Iraq', 690.9349587070396))]


def test_flight_path_exists_airports():
    """Test flight path for existing path."""
    from flight_paths import flight_path
    a = flight_path("Code Fellows", "Atlantis", "airports.json")
    if sys.version_info[0] == 2:
        assert a == "0.0 ['Code Fellows', u'Atlantis']"
    else:
        assert a == "0.0 ['Code Fellows', 'Atlantis']"


def test_flight_path_does_not_exist():
    """Test flight path for non-existent path."""
    from flight_paths import flight_path
    with pytest.raises(ValueError):
        flight_path("Iraq", "New York City", "airports.json")
