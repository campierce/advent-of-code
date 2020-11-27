from aocd import get_data
data = get_data(year=2015, day=8)

lines = data.split('\n')
literal_chars = 0
mem_chars = 0
for line in lines:
    n = len(line)
    literal_chars += n
    i = 0
    while i < n:
        char = line[i]
        if char != '"':
            mem_chars += 1
        if char == '\\':
            if line[i+1] == 'x':
                i += 3
            else:
                i += 1
        i += 1
print(literal_chars - mem_chars)
