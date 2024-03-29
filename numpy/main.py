#!/usr/bin/python3

# The entrypoint of the script
import sys
import os
import numpy as np
import ast
import yaml
    
def zeros():
    shape = ast.literal_eval(os.getenv("SHAPE").replace('"', ''))
    arr = np.zeros(shape)
    yaml.dump({"output": arr})

def array_sum():
    arr = os.getenv("ARRAY")
    res = np.sum(ast.literal_eval(arr))
    print(f"sum: {res}")

def array_dot():
    env1 = os.getenv("FIRST")
    env2 = os.getenv("SECOND")
    arr1 = ast.literal_eval(env1)
    arr2 = ast.literal_eval(env2)
    res = np.dot(arr1, arr2)
    print(f"dot: {res}")

def array_reshape():
    env1 = os.getenv("ARRAY")
    env2 = os.getenv("SHAPE")
    arr = ast.literal_eval(env1)
    shape = ast.literal_eval(env2)
    res = np.reshape(arr, shape)
    yaml.dump({'reshaped': res})

def array_add():
    env1 = os.getenv("FIRST")
    env2 = os.getenv("SECOND")
    arr1 = ast.literal_eval(env1)
    arr2 = ast.literal_eval(env2)
    res = np.add(arr1, arr2)
    yaml.dump({'add': res})


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
    elif command == 'sum':
        array_sum()
    elif command == 'dot':
        array_dot()
    elif command == 'reshape':
        array_reshape()
    elif command == 'add':
        array_add()
    
    # Done!
    # print("output: '" + str(cmds) + "'")
    # print("output: '" + cmds + "'")
