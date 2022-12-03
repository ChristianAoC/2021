def calc(days):
    freqs = [[int(k.strip()) for k in open("inputs/06.txt").readline().split(",")].count(i) for i in range(9)]
    for _ in range(days):
        freqs.append(freqs.pop(0))
        freqs[6]+=freqs[-1]
    print(sum(freqs))

calc(80)
calc(256)
