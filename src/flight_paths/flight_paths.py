"""Return the shortest flight path between two cities."""

from weighted_graph import Graph
import json
import sys


AIRPORTS = "cities_with_airports.json"


def calculate_distance(point1, point2):
    """
    Calculate distance between two points.

    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])
    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def get_data_from_json_file(file=None):
    """Get json file data."""
    if file is None:
        with open(AIRPORTS) as f:
            data = json.load(f)
    else:
        with open(file) as f:
            data = json.load(f)
    return data


def format_data(file=None):
    """Take data of airports and format into dictionary."""
    data = get_data_from_json_file(file)
    airport_dict = {airport['city']: {
        'destination_cities': airport['destination_cities'],
        'lat_lon': airport['lat_lon']
    } for airport in data}
    return airport_dict


def airports(file=None):
    """Return weighted graph of airports, destination_cities, and distances."""
    airport_dict = format_data(file)
    all_routes = Graph()
    for city in airport_dict:
        for destination in airport_dict[city]['destination_cities']:
            try:
                all_routes.add_edge(
                    city,
                    destination,
                    calculate_distance(airport_dict[city]['lat_lon'],
                                       airport_dict[destination]['lat_lon'])
                )
            except KeyError:
                continue
    return all_routes


def flight_path(start, destination, file=None):
    """Return the shortest routes between two cities."""
    airports_graph = airports(file)
    result = airports_graph.djikstras_shortest_path(start, destination)
    if result is None:
        raise KeyError('No path between these cities.')
    return result
