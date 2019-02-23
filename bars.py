import json
import sys
from geopy.distance import distance


def load_data(filepath):
    with open(filepath, "r", encoding="utf8") as file_handler:
        return json.load(file_handler)["features"]


def get_biggest_bar(bars):
    return max(bars, key=get_bar_seats_count)


def get_smallest_bar(bars):
    return min(bars, key=get_bar_seats_count)


def get_closest_bar(bars, longitude, latitude):
    loc = (latitude, longitude)
    return min(bars, key=lambda bar: get_bar_distance(loc, bar))


def get_bar_seats_count(bar):
    return bar["properties"]["Attributes"]["SeatsCount"]


def get_bar_address(bar):
    return bar["properties"]["Attributes"]["Address"]


def get_bar_name(bar):
    return bar["properties"]["Attributes"]["Name"]


def get_bar_distance(location, bar):
    (lon, lat) = bar["geometry"]["coordinates"]
    bar_loc = (lat, lon)
    return distance(bar_loc, location).km


def print_bar(bar):
    print(" Name: {}\n Address: {}, Seats count: {}".format(
        get_bar_name(bar),
        get_bar_address(bar),
        get_bar_seats_count(bar)
    ))


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
        sys.exit("Invalid input")
    except IndexError:
        sys.exit("Invalid command line arguments")

    print("Closest bar:")
    print_bar(closest)

    print("Biggest bar:")
    print_bar(biggest)

    print("Smallest bar:")
    print_bar(smallest)


if __name__ == "__main__":
    main()
