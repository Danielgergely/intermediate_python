import csv
import json

import helper


def read_airlines(filename='airlines.dat'):
    airlines = {}  # Map from code -> name
    with open(filename, encoding='utf8') as f:
        reader = csv.reader(f)
        for line in reader:
            airlines[line[4]] = line[1]
    return airlines


def read_airports(filename='airports.dat'):
    # Return a map of code -> name
    with open(filename, 'r', encoding="utf8") as f:
        reader = csv.reader(f)
        airports = {}
        for row in reader:
            code = row[4]
            name = row[1]
            airports[code] = name
    return airports


def read_routes(filename='routes.dat'):
    # Return a map from source -> list of destinations
    with open(filename, 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        routes = {}
        for row in reader:
            source = row[2]
            destination = row[4]
            if source not in routes:
                routes[source] = []
            routes[source].append(destination)
    return routes


def find_paths(routes, source, dest, max_segments):
    # Run a graph search algorithm to find paths from source to dest.
    frontier = {source}
    seen = {source: {(source,)}}
    for steps in range(max_segments):
        next_frontier = set()
        for airport in frontier:
            for target in routes.get(airport, ()):
                if target not in seen:
                    next_frontier.add(target)
                    seen[target] = set()
                for path in seen[airport]:
                    if len(path) != steps +1:
                        continue
                    seen[target].add(path + (target, ))
        frontier = next_frontier
    return seen[dest]


def rename_path(path, airports):
    return tuple(map(airports.get, path))


def main(source, dest, max_segments):
    airlines = read_airlines()
    airports = read_airports()
    routes = read_routes()

    a = 10
    paths = find_paths(routes, source, dest, max_segments)
    output = {}  # Build a collection of output paths!
    for path in paths:
        segments = len(path) -1
        if segments not in output:
            output[segments] = []
        output[segments].append(rename_path(path, airports))
    # Don't forget to write the output to JSON!
    export_filename = f"{source} to {dest} (max {max_segments}).json"
    with open(export_filename, 'w') as f:
        json.dump(output, f, indent=4, sort_keys=True)


if __name__ == '__main__':
    # parser = helper.build_parser()
    # args = parser.parse_args()
    # main(args.source, args.dest, args.max_segments)
    main('SFO', 'BOS', 2)
