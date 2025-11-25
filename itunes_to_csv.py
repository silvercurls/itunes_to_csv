from dataclasses import dataclass
import sys 
import csv
import datetime
import argparse
from typing import Optional


def parse_next_entry(filein):
    title = filein.readline().rstrip()
    artist = filein.readline().rstrip()
    cost = filein.readline().rstrip()
    while not (cost.startswith("$") or cost == "Free"):
        cost = filein.readline().rstrip()
    
    return {
        "title": title,
        "artist": artist,
        "cost": cost
    }

def filter_list(entries):
    retval = []
    for entry in entries:
        if entry["cost"] == "Free":
            continue
        if entry['title'].startswith("Apple") or entry['title'].startswith("iCloud"):
            continue
        if entry['artist'] == "Jackbox Games, Inc.":
            continue
        # Insert your own filters here.

        retval.append(entry)

    return retval

def parse_apple_text(input_file):
    entries = []
    with open(args.input_file, encoding='utf-8') as filein:
        while line := filein.readline():
            date = line.rstrip()
            reference_number = filein.readline().rstrip()
            # Parse but Ignore the totals
            total = filein.readline().rstrip()
            print(date, reference_number, total)

            while line:= filein.readline():
                title = line.rstrip()
                if title == "":
                    break
                entry = parse_next_entry(filein)
                entry['date']=date
                entry['reference_number'] = reference_number
                entries.append(entry)
    return entries

def write_entries(output_file, entries):
    with open(output_file, 'w', newline='', encoding="utf-8") as outfile:
        fieldnames = ["date", "reference_number", "title", "artist", "cost"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, dialect="excel-tab")
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)

                
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                    prog='itunes_to_csv.py',
                    description='Parses text copied from Apple Music Purchases online',
                    epilog='')
    
    parser.add_argument('input_file', help="File containing text representation of purchases on Apple Web site")      
    parser.add_argument('output_file', help="The tab separated output file")   
    # parser.add_argument('-t', '--type', help="Type of input"  ) 
    args = parser.parse_args()
    
    entries = parse_apple_text(args.input_file)
    entries = filter_list(entries)
    write_entries(args.output_file, entries)

                
