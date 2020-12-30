import aocd
data = aocd.get_data(year=2015, day=8)

lines = data.split('\n')
literal_chars = 0
encoded_chars = 0
for line in lines:
    literal_chars += len(line)
    encoded_chars += len(line) + 2
    for char in line:
        if char in ('"', '\\'):
            encoded_chars += 1
print(encoded_chars - literal_chars)
