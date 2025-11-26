import csv 
from csv import DictReader


def read_csv(csv_data):
    dict_reader = DictReader(csv_data)
    list_of_dict = list(dict_reader)
    return list_of_dict

