#Read File
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    filename = "day5ranges.txt"
    data = read_file(filename)
    ranges = []
    for line in data.strip().split('\n'):
        if line:
            pair = line.strip().split('-')
            pairList = [int(pair[0]), int(pair[1])]
            ranges.append(pairList)

    total = 0
    #merge intervals
    ranges.sort(key=lambda x: x[0])
    merged = []
    for interval in ranges:
        if not merged or merged[-1][1] < interval[0] - 1:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    print("Merged intervals:")
    for interval in merged:
        count = interval[1] - interval[0] + 1
        total += count
    print(f"Total unique numbers: {total}")



#Answer 366181852921027
