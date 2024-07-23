from argparse import ArgumentParser
from time import sleep

parser = ArgumentParser()
parser.add_argument("sleep_sec",type=int)
args = parser.parse_args()
print("Starting the timer of {args.sleep_sec} seconds")
start = args.sleep_sec

for _ in range(args.sleep_sec):
    print(start)
    sleep(1)
    start-=1
