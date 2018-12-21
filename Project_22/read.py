# read in our data
f=open('AviationData.txt', 'r')
aviation_data=f.readlines()

# the data is split on pipe, loop through and create list of lists
aviation_list=[line.split(' | ') for line in aviation_data]
print(aviation_list[0])

### Finding a code in our data
# create list of rows for any occurrences of LAX94LA336
lax_code = []
for i in range(len(aviation_list)):
    for j in range(len(aviation_list[i])):
        if aviation_list[i][j]=='LAX94LA336':
            lax_code.append(aviation_list[i])    
print('lax_code')
print(lax_code)
# the above code will create the needed list
# however, the time complexity is O(n*m), which may be problematic for large datasets
# in addition, if the code appears mutliple times in a row, we will have duplicates

# create list of rows for any occurrences of LAX94LA336
# improve on the above implementation
lax_code_2 = []
for row in aviation_list:
    if 'LAX94LA336' in row:
        lax_code_2.append(row)
print('lax_code_2')
print(lax_code_2)

# improve further by only searching the third column
# however this requires knowledge of where the code appears in the data
lax_code_3 = []
for row in aviation_list:
    if row[2] == 'LAX94LA336':
        lax_code_3.append(row)
print('lax_code_3')
print(lax_code_3)

# instead of a list of lists, let's store our data as a list of dictionaries
aviation_dict_list = []
dict_keys = aviation_data[0].split(' | ')
aviation_data_no_header = aviation_data[1:]
for row in aviation_data_no_header:
    split_row = row.split(' | ')
    temp_dict = {}
    for i in range(len(split_row)):
        temp_dict[dict_keys[i]] = split_row[i]
    aviation_dict_list.append(temp_dict)
print(aviation_dict_list[0])

# now search through the data to find the code LAX94LA336
lax_dict = []
for dictionary in aviation_dict_list:
    if 'LAX94LA336' in dictionary.values():
        lax_dict.append(dictionary)
# the time complexity is still O(n) since we had to still search each row

### Counting accidents by state
# now use the data to count the number of accidents by state
# filter the data using Country to only look at accidents in the United States
# parse the Location field and grab state (e.g. parse 'BRIDGEPORT, CA' to extract 'CA')
# use Counter to count the occurrences of each state
from collections import Counter
state_accidents_data = []
for dictionary in aviation_dict_list:
    if dictionary['Country'] == 'United States':
        location_split = dictionary['Location'].split(', ')
        state = location_split[-1]
        state_accidents_data.append(state)
state_accidents = Counter(state_accidents_data)
print(state_accidents.most_common(10))

# from the Counter, we can see that the top states in order are CA, FL, TX, AK, AZ, CO, WA, IL, MI, and GA.

### Counting fatalities and serious injuries by month and year
# for each unique month and year, sum the number of fatalities and serious injuries
# we will need to split the event date and capture the month and year
# I will use try/except for when values are missing or invalid
monthly_injuries = {}
for dictionary in aviation_dict_list:
    count = 0
    try:
        count += int(dictionary['Total Fatal Injuries'])
    except:
        pass
    try:
        count += int(dictionary['Total Serious Injuries'])
    except:
        pass
    
    event_date_split = dictionary['Event Date'].split('/')
    try:
        mm_yyyy = event_date_split[0] + '_' + event_date_split[2]
        if mm_yyyy in monthly_injuries.keys():
            monthly_injuries[mm_yyyy] += count
        else:
            monthly_injuries[mm_yyyy] = count
    except:
        pass

# check the above dictionary - should produce a count of 4 for July 1962
print(monthly_injuries['07_1962'])

