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


from collections import deque
 

# from https://www.techiedelight.com/merging-overlapping-intervals/
# A class to represent an interval
""" class Interval:
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end
 
    def __repr__(self):
        return str((self.begin, self.end))
 
 
# Function to merge overlapping intervals
def mergeIntervals(intervals):
 
    # sort the intervals in increasing order of their starting time
    intervals.sort(key=lambda x: x.begin)
 
    # create an empty stack
    stack = deque()
 
    # do for each interval
    for curr in intervals:
 
        # if the stack is empty or the top interval in the stack does not overlap
        # with the current interval, push it into the stack
        if not stack or (curr.begin > stack[-1].end):
            stack.append(curr)
 
        # if the top interval of the stack overlaps with the current interval,
        # merge two intervals by updating the end of the top interval
        # to the current interval
        if stack[-1].end < curr.end:
            stack[-1].end = curr.end
 
    # print all non-overlapping intervals
    while stack:
        print(stack.pop())

intervals = []
allValidIDs = 0

for line in ranges: 
    intervals.append(Interval(line[0], line[1]))

mergeIntervals(intervals)

for line in intervals:
    print(line)
    print(f"difference = {(int(line.end)-int(line.begin))+1}")
    allValidIDs += (int(line.end)-int(line.begin))+1
    print(allValidIDs)
print(allValidIDs) """

# from https://blog.seancoughlin.me/mastering-the-merging-of-overlapping-intervals-in-python

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    # Sort the intervals based on the starting points
    intervals.sort(key=lambda x: x[0])
    print(intervals)

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        print("START")
        last_merged = merged_intervals[-1]
        difference = current[1] - last_merged[0]
        
        if current[1] == last_merged[1]:
            print("same end")
        if current[0] == last_merged[0]:
            print("same start")

        if current[1] == last_merged[0]:
            print("current end is next start")
        if current[0] == last_merged[1]:
            print("current start is next end")
        
        if (difference == 1) or (difference == -1) or (difference == 0):
            print(f"difference {difference}")

        if (current[1] >= last_merged[1]):
            print("overlap detected")
            current[1] = last_merged[1]

        # If the current interval overlaps with the last merged interval, merge them
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Otherwise, add the current interval to the merged list
            merged_intervals.append(current)
        print(f" {current}")
        print("END\n")

    return merged_intervals 

ranges = merge(ranges)
numberOfIDs = 0

""" print(ranges)
for line in ranges: 
    print(f"pre - numberOfIDs {numberOfIDs}")
    difference = (line[1]-line[0])+1
    print(f"difference {difference}")
    numberOfIDs += (line[1]-line[0])+1
    print(numberOfIDs)
print(numberOfIDs) """

#Answer 366181852921027 > 366181852921118 > 366181852920936 >        2924726118562 > 2924726118560
# 366181852921118
# 530445096120682
# 530445096120308


""" 
timed out

for line in ranges: #{'start': '484155089502467', 'end': '484512074248320'}
    currentID = line['start']
    
    while currentID <= line['end']:
        allValidIDs.append(currentID)
        currentID += 1

allValidIDs = set(allValidIDs)

print(allValidIDs.count()) """