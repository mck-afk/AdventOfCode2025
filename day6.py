def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.readlines()

if __name__ == "__main__":
    lines = read_file("day6.txt")
    numbers = [int(x) for x in lines[0].split()]
    lists = [[num] for num in numbers]
    for line in lines[1:4]:
        values = [int(x) for x in line.split()]
        for i, value in enumerate(values):
            if i < len(lists):
                lists[i].append(value)

    operations = [op for op in lines[4].split()]
    print(f"Operations: {operations}")
    total = 0

    for i, x in enumerate(lists):
        print(f"Calculating {x}")
        if i < len(operations):
            if operations[i] == '+':
                result = sum(x)
                print(f"Addition = {result}")
                total += result
            elif operations[i] == '*':
                result = 1
                for v in x:
                    result *= v
                print(f"Multiplication = {result}")
                total += result
    
    print(f"Total: {total}")
# Part 1 Answer: 4580995422905

