#Read File
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    filename = "day2.txt"
    data = read_file(filename)
    instructions = []
    for line in data.strip().split(','):
        if line:
            pair = line[0:].strip().split('-')
            start = pair[0]
            end = pair[1]
            obj = {
                'start': start,
                'end': end
            }
            instructions.append(obj)
print(f"instructs {instructions[0]}")

invalidIDtotal = 0
sample = instructions[1:2]
    
#for each item in instructions
for item in instructions:
    print(item)
    length = len(item['end'])
    #if (len(item['start']) % 2 == 0) or (len(item['end']) % 2 == 0):
    #if (length == 2) or (length == 4) or (length == 6) or (length == 8) or (length == 10): #even means there can be two halves
    midPoint = int(length/2)
    print(midPoint)
    #create counter
    counter = item['start']
    #start counting and checking
    
    while int(counter) <= int(item['end']):
        counter = int(counter) + 1
        counter = str(counter)
        if (counter[0:midPoint] == counter[midPoint:]):
            counter = int(counter)
            invalidIDtotal += counter
            counter = str(counter)
            print(f"matches omg {counter}")

print(invalidIDtotal)

# Part 1 asnwer: 19605500130

