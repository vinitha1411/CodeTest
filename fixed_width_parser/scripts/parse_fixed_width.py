import csv
import json

# Load spec.json
with open('../data/spec.json', 'r') as spec_file:
    spec = json.load(spec_file)

column_names = spec["ColumnNames"]
offsets = list(map(int, spec["Offsets"]))
fixed_width_encoding = spec["FixedWidthEncoding"]
delimited_encoding = spec["DelimitedEncoding"]
include_header = spec["IncludeHeader"].lower() == "true"

# Parse the fixed-width file
input_file = "../data/input_fixed_width.txt"
output_file = "../data/output.csv"

def parse_fixed_width(input_file, output_file, column_names, offsets, include_header):
    with open(input_file, 'r', encoding=fixed_width_encoding) as infile, \
         open(output_file, 'w', newline='', encoding=delimited_encoding) as outfile:
        
        writer = csv.writer(outfile)
        if include_header:
            writer.writerow(column_names)

        for line in infile:
            row = []
            start = 0
            for offset in offsets:
                row.append(line[start:start+offset].strip())
                start += offset
            writer.writerow(row)

# Run the parser
parse_fixed_width(input_file, output_file, column_names, offsets, include_header)
