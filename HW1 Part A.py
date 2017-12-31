# Thomas Huang 26768493
import re
import os
import cProfile

token_list = []

def tokenize(TextFilePath: str)->list:
    token_list = []
    regex = "[a-z0-9]+"
    pattern = re.compile(regex)
    with open(TextFilePath, encoding='utf-8') as f:
        for line in f:
            token_list.extend(pattern.findall(line.lower()))
##            token_list.extend(re.findall(regex, line.lower()))
    #
    #prog = re.compile(regex)
#    for line in lines:
##        print(prog.match(line.lower()).search())
##        token_list.extend(prog.match(line.lower()).groups())
##        token_list.extend(re.findall(regex, line.lower()))
##        token_list[0:0] = re.findall(regex, line.lower()) ## http://stackoverflow.com/questions/12088089/python-list-concatenation-efficiency
    return token_list

def computeWordFrequencies(t_list: list)->dict:
    f_list = {}
    for word in t_list:
        if word in f_list:
            f_list[word] = f_list[word]+1
        else:
            f_list[word] = 1
    return f_list                

def printFreq(f_list: dict)->None:
    #print("printFreq")
    p_list = []
    v_list = {}
##    for k, v in f_list.items():
##        if v in v_list:
##            v_list[v].append(k)
##        else:
##            v_list[v] = [k]
##    for i in sorted(v_list.keys(), reverse=True):
##        for word in v_list[i]:
##            print(word + " - " + str(i) + " time(s)")
    for k, v in sorted(f_list.items(), key=lambda kv: kv[1], reverse=True):
        print(k + " - " + str(v) + " time(s)")


if __name__ == '__main__':
    file = ""
    while True:
        file = input("File Name: ")
        if(os.path.isfile(file)):
            break
        print("File does not exist.  Please enter an existing file name.")
##    cProfile.run('tokenize(file)')
    t_list = tokenize(file)
##    cProfile.run('computeWordFrequencies(t_list)')
    f_list = computeWordFrequencies(t_list)
##    cProfile.run('printFreq(f_list)')
    printFreq(f_list)

    print("\nRuntime complexity: O(n)")
