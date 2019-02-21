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


def main():
    try:
        path = sys.argv[1]
        bars_list = load_data(path)
        user_inp = input("Please input your location (lat, lon): ")
        (user_lat, user_lon) = list(map(float, user_inp.split(",")))
        closest = get_closest_bar(bars_list, user_lon, user_lat)
        biggest = get_biggest_bar(bars_list)
        smallest = get_smallest_bar(bars_list)
    except FileNotFoundError:
        sys.exit("File '{}' not found".format(path))
    except json.JSONDecodeError:
        sys.exit("Invalid file '{}'".format(path))
    except ValueError:
        sys.exit('Invalid input')
    except IndexError:
        sys.exit("Invalid command line arguments")

    print("Closest bar:", closest['properties']['Attributes']['Name'],
          "Address:", closest['properties']['Attributes']['Address'])

    seats_count = biggest['properties']['Attributes']['SeatsCount']
    print("Biggest bar:", biggest['properties']['Attributes']['Name'],
          "Seats count:", seats_count)

    seats_count = smallest['properties']['Attributes']['SeatsCount']
    print("Smallest bar:", smallest['properties']['Attributes']['Name'],
          "Seats count:", seats_count)


if __name__ == '__main__':
    main()
