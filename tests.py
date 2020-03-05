from pyswip import Prolog
import argparse


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


PROLOG_FILE = "37-0930.pl"

parser = argparse.ArgumentParser(description='Automate prolog testing')
parser.add_argument('--accepted',
                    default=False,
                    action='store_true',
                    help='test only accepted queries')

args = parser.parse_args()

queries = open('queries.txt', 'r')

prolog = Prolog()
prolog.consult(PROLOG_FILE)

errors = 0

for query in queries.readlines():
    answer = query[:6]
    prolog_query = query[7:]

    if args.accepted and answer != "accept":
        continue

    result = list(prolog.query(prolog_query))
    if not result and answer == "accept":
        errors += 1
        print(prolog_query, "Error!")

    if result and answer == "reject":
        errors += 1
        print(f"{bcolors.FAIL}Expected False got True!{bcolors.ENDC}")
        print(f"{bcolors.BOLD}{prolog_query}{bcolors.ENDC}")
        print(f"{bcolors.FAIL}-----------------------------{bcolors.ENDC}")

if not errors:
    print(f"{bcolors.OKGREEN}All Tests Passed!{bcolors.ENDC}")
else:
    print(f"{bcolors.FAIL}You have {errors} errors{bcolors.ENDC}")
