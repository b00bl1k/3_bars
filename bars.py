import json
import sys
from geopy.distance import distance


def load_data(filepath):
    with open(filepath, 'r', encoding="utf8") as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(bars):
    return max(bars,
               key=lambda kv: kv['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars,
               key=lambda kv: kv['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    user_loc = (latitude, longitude)

    def sort_by_distance(kv):
        (lon, lat) = kv['geometry']['coordinates']
        bar_loc = (lat, lon)
        return distance(bar_loc, user_loc).km

    sorted_by_distance = sorted(bars, key=sort_by_distance)
    return sorted_by_distance[0]


if __name__ == '__main__':
    try:
        bars_list = load_data(sys.argv[1])
        user_inp = input("Please input your location (lat, lon): ")
        (user_lat, user_lon) = list(map(float, user_inp.split(",")))
    except FileNotFoundError:
        sys.exit("File '{}' not found".format(path))
    except json.JSONDecodeError:
        sys.exit("Invalid file '{}'".format(path))
    except ValueError:
        sys.exit('Invalid input')
    except IndexError:
        sys.exit("Invalid command line arguments")

    closest = get_closest_bar(bars_list, user_lon, user_lat)
    print("Closest bar:", closest['properties']['Attributes']['Name'],
          "Address:", closest['properties']['Attributes']['Address'])

    biggest = get_biggest_bar(bars_list)
    seats_count = biggest['properties']['Attributes']['SeatsCount']
    print("Biggest bar:", biggest['properties']['Attributes']['Name'],
          "Seats count:", seats_count)

    smallest = get_smallest_bar(bars_list)
    seats_count = smallest['properties']['Attributes']['SeatsCount']
    print("Smallest bar:", smallest['properties']['Attributes']['Name'],
          "Seats count:", seats_count)
