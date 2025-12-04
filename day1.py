import math 

#Read File
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

#Instantiate Dial
class Dial:
    def __init__(self, start=50, min_value=0, max_value=99, zero_visits=0):
        self.value = start
        self.min_value = min_value
        self.max_value = max_value
        self.zero_visits = zero_visits

    def increment(self, amount=1):
        for i in range(amount):
            self.value += 1
            if self.value > self.max_value:
                self.value = self.min_value
            if self.value == 0:
                self.zero_visits += 1

    def decrement(self, amount=1):
        for i in range(amount):
            self.value -= 1
            if self.value < self.min_value:
                self.value = self.max_value
            if self.value == 0:
                self.zero_visits += 1

    def get(self):
        return self.value
        

#Process Instructions
dial = Dial()

for inst in instructions:
    print("START")
    print(f"Processing instruction: {inst}")
    print(f"Pre-processing dial value: {dial.get()}")
    
    if inst['direction'] == 'R':
        dial.increment(inst['clicks'])
        
    elif inst['direction'] == 'L':
        dial.decrement(inst['clicks'])
        
    print(f"Post-processing dial value: {dial.get()}")
    print(f"Total zero visits: {dial.zero_visits}")

#Part 1 Answer: total times it ends on 0: 1118  
#Part 2 Answer: total times it visits 0: 6289 
