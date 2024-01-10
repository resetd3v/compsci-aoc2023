import re

#part 1
dict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

# part 2
pattern = r"\d|one|two|three|four|five|six|seven|eight|nine"

def solvePart1(file):
    result = 0
    for line in file.readlines():
        numList = [char for char in line if char.isdigit()]
        result += int(numList[0] + numList[-1])
    return result

"""
- if num (key) is word version (in dict) find the value from the key and add it to the list else just add it (int)
- we cast to str cuz when we newNumList[0] + newNumList[-1] its concat not adding ints, to find that lines number
- take current lines number from the string concat and add to result (int addition this time +=)
"""
def solvePart2(file):
    result = 0
    for line in file.readlines():
        numList = []
        match = re.search(pattern, line)
        while match:
            numList.append(match.group())
            # go past current match
            next = match.start() + 1
            # remove past values for when we regex again
            line = line[next:]
            match = re.search(pattern, line)
        newNumList = [str(dict[num]) if num in dict else num for num in numList]
        result += int(newNumList[0] + newNumList[-1])
    return result