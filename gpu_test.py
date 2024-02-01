import argparse
from transformers import pipeline
import random

text_pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j,' 'k', 'l', 'm',       \
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',       \
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J,' 'K', 'L', 'M',       \
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',       \
                '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',                      \
                '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',  \
                ',', '.', ' ', ' ', ' ']

def generate_random_text():
    len = random.randint(20, 100)
    text = ""
    for i in range(len):
        text += text_pool[random.randint(0, 78)]
    return text

parser = argparse.ArgumentParser()
parser.add_argument('--device', type=int, default=0)
args = parser.parse_args()

generator = pipeline(task="text-generation", model="gpt2-xl", device=args.device)
while True:
    prompt = generate_random_text()
    generated = generator(prompt, max_length=100, num_return_sequences=1)