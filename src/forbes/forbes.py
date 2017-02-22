"""Analysis of a list of billionaires from Forbes magazine.

oldest_and_youngest: Return the name, net worth, and industry of the oldest billionaire under 80 and the youngest billionaire.
"""


def oldest_and_youngest():
    """Return the name, net worth, and industry of the oldest billionaire under 80 and the youngest billionaire."""
    import json
    with open('forbes_billionaires_2016.json') as json_data:
        billionaires = json.load(json_data)
    oldest = None
    youngest = None
    for each in billionaires:
        if oldest is None:
            oldest = each
        if youngest is None:
            youngest = each
        if each["age"] > oldest["age"] and each["age"] < 80:
            oldest = each
        if each["age"] < youngest["age"] and each["age"] > 0:
            youngest = each
    keys = ["name", "net_worth (USD)", "source"]
    oldest, youngest = {k: oldest[k] for k in keys}, {k: youngest[k] for k in keys}
    return oldest, youngest
