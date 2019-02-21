import json
import sys
from geopy.distance import distance


def load_data(filepath):
    with open(filepath, 'r', encoding="utf8") as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    features = data['features']
    return max(features,
               key=lambda kv: kv['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(data):
    features = data['features']
    return min(features,
               key=lambda kv: kv['properties']['Attributes']['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    features = data['features']
    user_loc = (latitude, longitude)

    def sort_by_distance(kv):
        (lon, lat) = kv['geometry']['coordinates']
        bar_loc = (lat, lon)
        return distance(bar_loc, user_loc).km

    sorted_by_distance = sorted(features, key=sort_by_distance)
    return sorted_by_distance[0]


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Invalid command line")

    path = sys.argv[1]
    try:
        bars = load_data(path)
    except FileNotFoundError:
        sys.exit("File '{}' not found".format(path))
    except json.JSONDecodeError:
        sys.exit("Invalid file '{}'".format(path))

    user_inp = input("Please input your location (lat, lon): ")
    try:
        (user_lat, user_lon) = list(map(float, user_inp.split(",")))
    except ValueError:
        sys.exit('Invalid input')

    closest = get_closest_bar(bars, user_lon, user_lat)
    print("Closest bar:", closest['properties']['Attributes']['Name'],
          "Address:", closest['properties']['Attributes']['Address'])

    biggest = get_biggest_bar(bars)
    seats_count = biggest['properties']['Attributes']['SeatsCount']
    print("Biggest bar:", biggest['properties']['Attributes']['Name'],
          "Seats count:", seats_count)

    smallest = get_smallest_bar(bars)
    seats_count = smallest['properties']['Attributes']['SeatsCount']
    print("Smallest bar:", smallest['properties']['Attributes']['Name'],
          "Seats count:", seats_count)
