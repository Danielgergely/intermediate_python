"""Provide saving (writing) options to permanent datafiles to enable the storage of specific queries."""
import csv
import json


def write_to_csv(results, filename: str):
    """Write result(s) of a query into a specified .csv file."""
    header = ['datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km',
              'potentially_hazardous']
    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=header)
        writer.writeheader()
        for r in results:
            line = {}
            line['datetime_utc'] = r.time
            line['distance_au'] = r.distance
            line['velocity_km_s'] = r.velocity
            line['designation'] = r._designation
            if r.neo.name is None:
                line['name'] = ''
            else:
                line['name'] = r.neo.name
            line['diameter_km'] = r.neo.diameter
            if r.neo.hazardous:
                line['potentially_hazardous'] = 'True'
            else:
                line['potentially_hazardous'] = 'False'

            writer.writerow(line)


def write_to_json(results, filename: str):
    """Write result(s) of a query into a specified .json file."""
    with open(filename, 'w') as outfile:
        output = []
        for r in results:
            approach = {}
            neo = {}
            neo['designation'] = r.neo.designation
            if r.neo.name is None:
                neo['name'] = ''
            else:
                neo['name'] = r.neo.name
            neo['diameter_km'] = r.neo.diameter
            neo['potentially_hazardous'] = r.neo.hazardous
            approach['datetime_utc'] = r.time_str
            approach['distance_au'] = r.distance
            approach['velocity_km_s'] = r.velocity
            approach['neo'] = neo
            output.append(approach)
        json.dump(output, outfile, indent=4)
