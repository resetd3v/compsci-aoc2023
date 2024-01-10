import os, sys
import glob, importlib, pathlib

"""
for skids: 
    = assignment
    == selection
    other langs:
        == means can be diff type 
        === means same type
        eg.
        '1' == 1 - true
        '1' === 1 - false
        1 === 1 - true

    i hate this lang php in comp sci pls
"""

# my magnum opus
def cls(): os.system('cls || clear')

# i wonder what this does
def openFile(path, part):
    try:
        return open(path + '\input' + str(part) + '.txt', 'r')
    except Exception as e:
        print(e)

# https://stackoverflow.com/questions/47558704/python-dynamic-import-methods-from-file 90 % of coding is knowing what to google, i learned something fuck yoy
def solve(path, part):
    # add to path so we can reference
    sys.path.append(path)
    # get all files in dir we can use *.py to get all py files
    pyFiles = glob.glob(os.path.join(path, 'lmao.py'))

    for file in pyFiles:
        moduleName = pathlib.Path(file).stem
        module = importlib.import_module(moduleName)
        print(f'{module} | {moduleName}')
        inputFile = openFile(path, part)
        print(f'{inputFile} | {inputFile.name}')
    
    # p100 null check 1337
    if module != None and file != None:
        print('\n-> ', end="")
        if part == 1:
            print(module.solvePart1(inputFile))
        elif part == 2:
            print(module.solvePart2(inputFile))
        print()
    else:
        print(f'cry about it | m: {module} | f: {file}')

if __name__ == "__main__":
    # my amazing pattened reset input validation
    cls()
    while True:
        try:
            dayPath = int(input('day (1-30): '))
            if dayPath not in (1,30): raise SystemError

            # have to be ran in dir
            path = os.path.join(os.path.dirname(os.getcwd()), 'ADVENTOFCODE\\2023\\' + str(dayPath))
            # sys.path.append(inputPath)
            part = int(input('part (1-2): '))
            # BUFFER OVERFLWO!!1111!!!!!3137
            if part not in (1,2): raise OverflowError

            cls()
            solve(path, part)
        except Exception as e:
            cls()
            if type(e) == SystemError:
                print(f"Enter a day 1-30 bozo | {dayPath}")
            elif type(e) == OverflowError:
                print(f"Enter a part 1-2 dumbass | {part}")
            else:
                print(e)