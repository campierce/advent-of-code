import hashlib
from aocd import get_data
data = get_data(year=2015, day=4)

i = 1
while True:
    msg = data + str(i)
    h = hashlib.md5(msg.encode()).hexdigest()
    if h[:6] == '000000':
        print(i)
        break
    i += 1
