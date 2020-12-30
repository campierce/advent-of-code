import aocd
data = aocd.get_data(year=2015, day=10)

def look_and_say(seq, n):
    for _ in range(n):
        sb = []
        cnt = 1
        for i, char in enumerate(seq):
            if (i + 1 == len(seq) or
                    char != seq[i+1]):
                sb.append(str(cnt) + char)
                cnt = 1
            else:
                cnt += 1
        seq = ''.join(sb)
    return seq

ans = look_and_say(data, 50)
print(len(ans))
