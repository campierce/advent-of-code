import aocd
import hashlib
data = aocd.get_data(year=2015, day=4)

i = 1
while True:
    msg = data + str(i)
    h = hashlib.md5(msg.encode()).hexdigest()
    if h[:5] == '00000':
        print(i)
        break
    i += 1
