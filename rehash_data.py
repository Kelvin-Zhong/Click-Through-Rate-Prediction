
# coding: utf-8

# In[9]:

#!/usr/bin/python

'''
This program is to rehash the value of the attributes to 0 - N, 
which is easy for further processing.
The target rehashed index is target_index = [1,4,7,10,13,14] in train file
and after running the program, the corresponding number of value is:

'''

input_file_train = "Data/train_3days.txt"
input_file_test = "Data/test_4th.txt"
output_file_train = "Data/train_3days_rehashed.txt"
output_file_test = "Data/test_4th_rehashed.txt"
dictionary_train = [{} for b in range(6)]
dictionary_count = [0 for b in range(6)]

with open(input_file_train,'r') as infile:
    for line in infile:
        attributes = line.split(',')
        for i in range(len(attributes)):
            if attributes[i] not in dictionary_train[i]:
                dictionary_train[i][attributes[i]] = dictionary_count[i]
                dictionary_count[i] += 1
        
        with open(output_file_train,'a') as outfile:
            for i in range(len(attributes)):
                if i != 0:
                    outfile.write(',' + str(dictionary_train[i][attributes[i]]))
                else:
                    outfile.write(str(dictionary_train[i][attributes[i]]))
            outfile.write('\n')
    
            


# In[10]:

delete_count = 0

with open(input_file_test,'r') as infile:
    for line in infile:
        attributes = line.split(',')
        
        nonexist = False
        for i in range(len(attributes)):
            if attributes[i] not in dictionary_train[i]:
                nonexist = True
                delete_count += 1
                break
        
        if nonexist:
            continue
        else:
            with open(output_file_test,'a') as outfile:
                for i in range(len(attributes)):
                    if i != 0:
                        outfile.write(',' + str(dictionary_train[i][attributes[i]]))
                    else:
                        outfile.write(str(dictionary_train[i][attributes[i]]))
                outfile.write('\n')
                
print delete_count

