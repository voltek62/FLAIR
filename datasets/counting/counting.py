import random
import string
import json

LEN_STR = 30



char_list = string.ascii_lowercase
data_list = []


for _ in range(100):
    # random string generation
    num_chars = random.randint(3, 5)
    len_str = LEN_STR
    target_chars = random.sample(char_list, num_chars)
    target_str = ''.join(random.choices(target_chars, k=30))   

    # count pivot chars
    pivot_char = random.sample(target_chars, 1)[0]
    cnt_pivot_char = target_str.count(pivot_char)

    question = "What is the number of " + pivot_char + " in " + target_str + "?"
    
    data_list.append({"question": str(question), "answer": str(cnt_pivot_char)})

with open("counting.json", "w") as f:
    json.dump(data_list, f)