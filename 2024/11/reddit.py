from functools import cache
from math import floor, log10
import time

# in response  to:
# https://www.reddit.com/r/adventofcode/comments/1hcou41/2024_day_11_part_2_python_request_for_code/

@cache
def count(x, d=75):
    if d == 0: return 1
    if x == 0: return count(1, d-1)

    l = floor(log10(x))+1
    if l % 2: return count(x*2024, d-1)

    return (count(x // 10**(l//2), d-1)+
            count(x %  10**(l//2), d-1))

with open('input.txt', 'r', encoding='utf8') as file_handle:
    inp = file_handle.readline().strip()

data = map(int, inp.split())
print(sum(map(count, data)))
