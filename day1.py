import math 

class Dial:
    def __init__(self, start=50, min_value=0, max_value=99):
        self.value = start
        self.min_value = min_value
        self.max_value = max_value

    def increment(self, amount=1):
        self.value = (self.value + amount) % (self.max_value + 1)

    def decrement(self, amount=1):
        self.value = (self.value - amount) % (self.max_value + 1)

    def get(self):
        return self.value
        
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    filename = "day1.txt"
    data = read_file(filename)
    instructions = []
    for line in data.strip().split('\n'):
        if line:
            direction = line[0]
            clicks = int(line[1:])
            obj = {
                'direction': direction,
                'clicks': clicks
            }
            instructions.append(obj)

    
    dial = Dial()
    zero_lands = 0 #dial ends on 0 #Part 1 Answer: 1118
    zero_visits = 0 #dial visits 0 during rotation #Part 2 Answer: >5000
    for inst in instructions:
        # Check if clicks exceeds max_value
        if inst['clicks'] > dial.max_value: #991. #doesn't work for case L2 R3
            remainder = inst['clicks'] % dial.max_value #modulo to find effective clicks #1
            zero_visits += math.floor(inst['clicks'] / dial.max_value) #diviser to find how many times it wraps #10
            #add remainder to dial
            if inst['direction'] == 'R':
                dial.increment(remainder)
                #if remainder also clicks over dial.max_value, increment zeroclicks accordingly
                if (remainder+dial.get()) > dial.max_value:
                    zero_visits += 1
                    dial.increment(remainder)
            elif inst['direction'] == 'L':
                
                if (remainder+dial.get()) > dial.max_value:
                    zero_visits += 1
                    dial.decrement(remainder)
            print(f"Instruction {inst} has clicks {zero_visits} exceeding max_value by {remainder}.")
        if inst['direction'] == 'R':
            dial.increment(inst['clicks'])
        elif inst['direction'] == 'L':
            dial.decrement(inst['clicks'])
        print(f"dial value: {dial.get()}")
        if dial.get() == 0:
            zero_lands += 1
    print(f"dial ends on 0 {zero_lands} times. Dial visits 0 {zero_visits} times. Total: {zero_lands+zero_visits}.")

