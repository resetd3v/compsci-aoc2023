import os, sys
import glob, importlib, pathlib

"""
    i hate this lang, php in comp sci pls
"""

# my magnum opus
cls = lambda: os.system('cls || clear')

# i wonder what this does
def openFile(path, part):
    try:
        return open(f'{path}\input{str(part)}.txt', 'r')
    except Exception as e:
        print(e)

# https://stackoverflow.com/questions/47558704/python-dynamic-import-methods-from-file 90 % of coding is knowing what to google, i learned something fuck yoy
def solve(path, part):
    module = None
    inputFile = None
    # idk if u need this ngl dont see y u cant get it from filename
    # add to path so we can reference
    sys.path.append(path)
    # get all files in dir eg. we can use *.py to get all py files
    pyFiles = glob.glob(os.path.join(path, 'lmao.py'))
    
    try:
        for file in pyFiles:
            moduleName = pathlib.Path(file).stem
            module = importlib.import_module(moduleName)
            print(f"{module} | {moduleName}")
            inputFile = openFile(path, part)
            print(f"{inputFile} | {inputFile.name}")
        
        # p100 null check 1337
        if module == None or inputFile == None:
            print(f"cry about it | m: {module} | f: {inputFile}")
            return
        # list comprehension go brrrr no ''.join() needed but y not pass in dayPath cuz fuck u thats y (this is meant to show off my knowledge idk lil bro also map() faster)
        day = [w for w in path.split('\\')][-1]
        print(f"\nday: {day} | part: {part}")
        print(" -> ", end="")
        print(module.solvePart1(inputFile) if part == 1 else module.solvePart2(inputFile))
        print()
            
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while True:
        try:
            dayPath = int(input("day (1-30): "))
            if dayPath not in range(1,30): raise SystemError

            # have to be ran in dir fuck string concat all my homies hate string concat
            path = os.path.join(f'{__file__.replace("main.py", "")}2023\\{str(dayPath)}')
            # sys.path.append(inputPath)
            part = int(input("part (1-2): "))
            cls()
            # BUFFER OVERFLWO!!1111!!!!!3137
            if part not in (1,2): raise OverflowError

            solve(path, part)
        except: SystemError:
            print(f"Enter a day 1-30 bozo | {dayPath}")            
        except OverflowError:
            print(f"Enter a part 1-2 dumbass | {part}")
        except Exception as e:
                print(e)
