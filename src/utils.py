import pandas as pd
from datetime import datetime
import json

file_path = "../data/farmers-protest-tweets-2021-2-4.json"

def load_json(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data.append(json.loads(line))
    return pd.json_normalize(data)

def parse_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S%z').date()