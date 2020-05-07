#!/usr/bin/env python3
from FTPYacc import parser
import csv


in_filename = 'urls.txt'

stats = {}
stats_filename = 'stats.csv'

INCORRECT = 0


def main():

    global stats
    global INCORRECT

    with open(in_filename) as f:

        sname  = str()

        for line in f:
            try:
                sname = parser.parse(line.strip())
                if not sname:
                    raise Error()
            except:
                INCORRECT += 1
                continue

            if sname not in stats:
                stats[sname]  = 1
            else:
                stats[sname] += 1

        # print(stats)
        # print("INCORRECT: " + str(INCORRECT))

        with open(stats_filename, 'w') as sf:

            field_names = ['URL', 'NumOccurences']

            writer = csv.DictWriter(sf, fieldnames=field_names)

            writer.writeheader()

            writer.writerow({'URL': '<INCORRECT>', 'NumOccurences': str(INCORRECT)})

            for k, v in stats.items():
                writer.writerow({'URL': k, 'NumOccurences': v})


if __name__ == '__main__':
    main()

