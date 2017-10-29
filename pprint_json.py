import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as handle:
        return json.load(handle)


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4, sort_keys=True))


if __name__ == '__main__':
    json_data = load_data(sys.argv[1])
    pretty_print_json(json_data)
