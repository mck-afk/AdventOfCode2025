#Read File
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    filename = "day5.txt"
    data = read_file(filename)
    checkIDs = []
    for line in data.strip().split('\n'):
        if line:
            checkIDs.append(line)
            

if __name__ == "__main__":
    filename = "day5ranges.txt"
    data = read_file(filename)
    ranges = []
    for line in data.strip().split('\n'):
        if line or (line == '\n'):
            pair = line.strip().split('-')
            obj = {
                'start': pair[0],
                'end': pair[1]
            }
            ranges.append(obj)
            

print(f"ranges {ranges[0]}")
print(f"check it: {checkIDs[0]}")

freshCounter = 0

#for each check id
for index, (thisID) in enumerate(checkIDs):
    freshFlag = 1
    print(f"index {index} is this ID {thisID}")
    if freshFlag == 1:
        for thisRange in ranges:
            if int(thisRange['start']) < int(thisID) < int(thisRange['end']):
                freshCounter += 1
                freshFlag = 0
                print(f"id {thisID} is in {thisRange}")
                break

print(freshCounter)

#Part 1 Answer: 798