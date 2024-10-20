import sys
import csv
from collections import Counter
import re
import itertools


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")
    with open(sys.argv[1]) as File:
        reader = csv.reader(File)
        rows = list(reader)
        keys = rows[0]
        keys.remove("name")
    with open(sys.argv[2]) as dnafile:
        for row in csv.reader(dnafile):
            dnalist = row
    dna = dnalist[0]
    sequences = {}
    for i in range(len(keys)):
        sequences[keys[i]] = consecutive(keys[i], dna)
    with open(sys.argv[1]) as File:
        data = csv.DictReader(File)
        for row in data:
            count = 0
            for key in sequences:
                if sequences[key] == int(row[key]):
                    count += 1
            if count == len(keys):
                sys.exit(row['name'])
        sys.exit("No match")


def consecutive(substring, full_string):
    pattern = "(?=((" + re.escape(substring) + ")+))"
    matches = re.findall(pattern, full_string)
    try:
        return max(len(m[0]) // len(substring) for m in matches)
    except ValueError:
        pass


main()