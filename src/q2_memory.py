from typing import List, Tuple
import json
import re
from collections import Counter
from utils import file_path

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_counter = Counter()
    emoji_pattern = re.compile(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF]+')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                tweet = json.loads(line)
                emojis = emoji_pattern.findall(tweet['content'])
                emoji_counter.update(emojis)
    
    return emoji_counter.most_common(10)
