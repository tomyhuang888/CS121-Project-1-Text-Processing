# Thomas Huang 26768493
import re
import os

def tokenize(TextFilePath: str)->set:
    token_list = []
    with open(TextFilePath,encoding='utf-8') as f:
        lines = f.readlines()
    regex = "[a-z0-9]+"
    t_set = set()
    for line in lines:
        t_set.update(re.findall(regex, line.lower()))
    return t_set

def common(t_set1: set, t_set2: set)->list:
    c_list = []
    for item in t_list1:
        if item in t_list2:
            c_list.append(item)
    return c_list

def print_common(c_list: list):
    print("Common token(s):")
    for item in c_list:
        print("  " + str(item))
    print("Total of " + str(len(c_list)) + " common token(s).")

if __name__ == '__main__':

    file1 = ""
    file2 = ""
    while True:
        file1 = input("File 1 Name: ")
        if(os.path.isfile(file1)):
            break
        print("File does not exist.  Please enter an existing file name.")
    file2 = ""
    while True:
        file2 = input("File 2 Name: ")
        if(os.path.isfile(file2)):
            break
        print("File does not exist.  Please enter an existing file name.")
    t_list1 = tokenize(file1)
    t_list2 = tokenize(file2)

    c_list = common(t_list1, t_list2)
    print_common(c_list)
    
    print("\nRuntime complexity: O(n)")
