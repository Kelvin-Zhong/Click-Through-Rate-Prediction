
# coding: utf-8

# In[1]:

#!/usr/bin/python

### for training set at the first 7 days ##########

'''
targets are
No. attribute description: index
1. click: 1
2. banner_pos: 4
3. site_category: 7
4. app_category: 10
5. device_model: 13
6. device_type: 14

Filter time range: hour : 2
training set:
14102100 - 14102400
testing set:
14102400 - 14102500

'''

input_file = "Data/train"
train_file = "Data/train_3days.txt"
test_file = "Data/test_4th.txt"

count = 0
train_count = 0
test_count = 0

target_index = [1,4,7,10,13,14]

with open(input_file,'r') as infile:
    for line in infile:
        count += 1
        
        attributes = line.split(',')        
        hour = attributes[2]
        if hour >= '14102500':
            continue

        elif hour < '14102400':
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
                test_count += 1
            
print count,train_count,test_count


###################################################################

