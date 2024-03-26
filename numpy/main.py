#!/usr/bin/python3

# The entrypoint of the script
import sys
import os
import numpy as np
import ast
import yaml

def test():
    input_data = os.getenv("INPUT").replace('"', '')
    print("output: '" + input_data + "'")
    
def zeros():
    shape = ast.literal_eval(os.getenv("SHAPE").replace('"', ''))
    arr = np.zeros(shape)
    yaml.dump({"output": arr})
    


if __name__ == "__main__":
    # Make sure that at least one argument is given, that is either 'encode' or 'decode'
    # if len(sys.argv) != 2 or (sys.argv[1] != "test" and sys.argv[1] != "zeros"):
    #     print(f"Usage: {sys.argv[0]} encode|decode")
    #     exit(1)

    # If it checks out, call the appropriate function
    command = sys.argv[1]
    if command == "test":
            test()
    elif command == "zeros":
            zeros()

    # Done!
    # print("output: '" + str(cmds) + "'")
    # print("output: '" + cmds + "'")
