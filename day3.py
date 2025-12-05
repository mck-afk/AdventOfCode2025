#Read File
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    filename = "day3.txt"
    data = read_file(filename)
    instructions = []
    for line in data.strip().split('\n'):
        if line:
            instructions.append(line)

print(f"instructs {instructions[0]}")

#loop through each digit looking for the highest one, stop loop if found a 9
#once found the highest, then only loop through after that point to find second highest

totalJoltage = 0

for bank in instructions:
    highestDigit = 0
    highestDigitIndex = 0
    secondDigit = 0
    secondDigitIndex = 0
    bankJoltage = 0
    print(bank)
    for index, (digit) in enumerate(bank):
        
        digit = int(digit)
        if (digit > highestDigit) and (index < 99):
            highestDigit = digit
            highestDigitIndex = index
            print(f"highest digit {highestDigit} with index {highestDigitIndex}")

    for index, (digit) in enumerate(bank[highestDigitIndex+1:]):
        digit = int(digit)
        if digit > secondDigit:
            secondDigit = digit
            
    print(f"second highest digit {secondDigit}")
    bankJoltage = str(highestDigit)+str(secondDigit)
    print(bankJoltage)
    totalJoltage += int(bankJoltage)
    print(totalJoltage)

#Part 1 Answer: 17158
#Part 2 Answer: 