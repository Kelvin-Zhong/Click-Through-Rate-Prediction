
# coding: utf-8

# In[45]:

#!/usr/bin/python

### for training set at the first 7 days ##########

'''
targets are
No. attribute description: index
1. id: 0
2. click: 1
3. banner_pos: 4
4. site_category: 7
5. app_category: 10
6. device_model: 13
7. device_type: 14

Filter time range: hour : 2
training set:
14102100 - 14102700 -> hour smaller than 14102700
testing set:
14102700 - 14102800

'''

input_file = "Data/train"
train_file = "Data/train_7days.txt"
test_file = "Data/test_7th.txt"

count = 0
train_count = 0
test_count = 0

target_index = [0,1,4,7,10,13,14]

with open(input_file,'r') as infile:
    for line in infile:
        count += 1
        
        attributes = line.split(',')        
        hour = attributes[2]
        if hour >= '14102800':
            continue

        elif hour < '14102700':
            with open(train_file,'a') as outfile:
                for i in range(len(target_index)):
                    if i != 0:
                        outfile.write(',' + attributes[target_index[i]])
                    else:
                        outfile.write(attributes[target_index[i]])

                outfile.write('\n')
                train_count += 1
                
        else:
            with open(test_file,'a') as outfile:
                for i in range(len(target_index)):
                    if i != 0:
                        outfile.write(',' + attributes[target_index[i]])
                    else:
                        outfile.write(attributes[target_index[i]])

                outfile.write('\n')
                train_count += 1
            
print count,train_count,test_count


###################################################################

