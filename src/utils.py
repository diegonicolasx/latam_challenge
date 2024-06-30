import pandas as pd
import gdown
import json

def download_and_load_json(url, output):
    gdown.download(url, output, quiet=False)
    with open(output, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return pd.json_normalize(data)
