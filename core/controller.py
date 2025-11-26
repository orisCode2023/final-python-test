from operator import itemgetter
from csv_handler import *


def sort_by_distance():
    with open('data.csv') as f:
        data = read_csv(f)
    sorted_list = sorted(data, key=itemgetter('distance'), reverse=True)
    print(sorted_list)

