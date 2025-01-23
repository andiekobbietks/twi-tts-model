# FILE: /twi-tts-model/twi-tts-model/scripts/preprocess_text.py

import os
import re
import json
import numpy as np
from typing import List
from src.data_preprocessing import normalize_tonal_variations, restore_diacritics

def load_raw_text(file_path: str) -> List[str]:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def save_processed_text(processed_text: List[str], output_path: str):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(processed_text)

def normalize_text(text: str) -> str:
    text = normalize_tonal_variations(text)
    text = re.sub(r'\d{1,2}:\d{2}', lambda x: convert_time_to_words(x.group()), text)
    return text

def convert_time_to_words(time_str: str) -> str:
    hours, minutes = map(int, time_str.split(':'))
    return f"{num_to_words(hours)} {num_to_words(minutes)}"

def num_to_words(num: int) -> str:
    # Simple number to words conversion for demonstration
    # Extend this function for larger numbers as needed
    words = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
        18: "eighteen", 19: "nineteen", 20: "twenty"
    }
    return words.get(num, str(num))

def preprocess_text(input_file: str, output_file: str):
    raw_text = load_raw_text(input_file)
    processed_text = []

    for line in raw_text:
        line = line.strip()
        if line:
            line = normalize_text(line)
            line = restore_diacritics(line)
            processed_text.append(line + '\n')

    save_processed_text(processed_text, output_file)

if __name__ == "__main__":
    input_path = os.path.join('data', 'raw', 'input.txt')  # Example input file
    output_path = os.path.join('data', 'processed', 'output.txt')  # Example output file
    preprocess_text(input_path, output_path)