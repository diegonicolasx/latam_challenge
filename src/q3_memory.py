from typing import List, Tuple
import json
import re
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_counter = Counter()
    mention_pattern = re.compile(r'@\w+')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                tweet = json.loads(line)
                mentions = mention_pattern.findall(tweet['content'])
                mention_counter.update(mentions)
    
    top_mentions = [(mention.lstrip('@'), count) for mention, count in mention_counter.most_common(10)]
    return top_mentions
