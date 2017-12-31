# Thomas Huang 26768493
import re
import os

token_list = []

text = ""

def add_token(word: str, t_list: list)->list:
    if word not in t_list:
        t_list.append(word)
    return t_list

def tokenize(TextFilePath: str)->list:
    global text
    text = TextFilePath
    token_list = []
    with open(text) as f:
        lines = f.readlines()
    regex = "[A-Za-z0-9][A-Za-z0-9]*"
    for line in lines:
        for word in re.findall(regex, line):
            token_list = add_token(word.lower(), token_list)
    return token_list

def computeWordFrequencies(t_list: list)->dict:
    regex = "[A-Za-z0-9][A-Za-z0-9]*"
    f_list = {}
    with open(text) as f:
        lines = f.readlines()
    for line in lines:
        for word in re.findall(regex, line):
            word = word.lower()
            if word in t_list:
                if word in f_list:
                    f_list[word] = f_list[word]+1
                else:
                    f_list[word] = 1
    return f_list

def printFreq(f_list: dict)->None:
    #print("printFreq")
    p_list = []
    for k, v in f_list.items():
        p_list.append( (k, v) )
        p_len = len(p_list)
        if p_len > 1:
            for i in range(p_len-1):
                curr_pos = p_len-i-1
                prev_pos = p_len-i-2
                if(p_list[prev_pos][1] < p_list[curr_pos][1]):
                    temp = p_list[curr_pos]
                    p_list[curr_pos] = p_list[prev_pos]
                    p_list[prev_pos] = temp
                else:
                    break
    #print(p_list)
    for k, v in p_list:
        print(str(k) + " - " + str(v))

if __name__ == '__main__':
    string1 = "my name is Thomas thomas hu.ang hus-sang hua'ng f9203ded"
    file = ""
    while True:
        file = input("File Name: ")
        if(os.path.isfile(file)):
            break
        print("File does not exist.  Please enter an existing file name.")
    t_list = tokenize(file)
    f_list = computeWordFrequencies(t_list)
    printFreq(f_list)

    print("Runtime complexity: O(n)")
    
