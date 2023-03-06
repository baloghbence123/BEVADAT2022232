# %%
# Create a function that returns with a subsest of a list.
# The subset's starting and ending indexes should be set as input parameters (the list aswell).
# return type: list
# function name must be: subset
# input parameters: input_list,start_index,end_index

# %%
inputList1 = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
inputList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
inputListTuples = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
inputList3 = []


# %%
def subset(input_list, start_index, end_index):
    tmpList = []
    if len(input_list) > 0:
        for i in range(start_index, end_index):
            tmpList.append(input_list[i])
        return tmpList
    else:
        return tmpList


# %%
# Create a function that returns every nth element of a list.
# return type: list
# function name must be: every_nth
# input parameters: input_list,step_size


# %%
def every_nth(input_list, step_size):
    tmpList = []
    for i in range(0, len(input_list), step_size):
        tmpList.append(input_list[i])
    return tmpList


# %%
# Create a function that can decide whether a list contains unique values or not
# return type: bool
# function name must be: unique
# input parameters: input_list


# %%
def unique(input_list):
    for i in input_list:
        if input_list.count(i) > 1:
            return False

    return True


# %%
# Create a function that can flatten a nested list ([[..],[..],..])
# return type: list
# fucntion name must be: flatten
# input parameters: input_list


# %%
def flatten(input_list):
    flattened_list = []
    for i in input_list:
        for j in i:
            flattened_list.append(j)
    return flattened_list


# %%
# Create a function that concatenates n lists
# return type: list
# function name must be: merge_lists
# input parameters: *args


# %%
def merge_lists(*args):
    tmpList = []
    for arg in args:
        for item in arg:
            tmpList.append(item)
    return tmpList


# %%
# Create a function that can reverse a list of tuples
# example [(1,2),...] => [(2,1),...]
# return type: list
# fucntion name must be: reverse_tuples
# input parameters: input_list


# %%
def reverse_tuples(input_list):
    tmpList = []
    for i in input_list:
        tmpList.append(tuple(reversed(i)))

    return tmpList


# %%
# Create a function that removes duplicates from a list
# return type: list
# fucntion name must be: remove_tuplicates
# input parameters: input_list


# %%
def remove_duplicates(input_list):
    output_list = []

    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list


# %%
# Create a function that transposes a nested list (matrix)
# return type: list
# function name must be: transpose
# input parameters: input_list


# %%
def transpose(input_list):
    outputList = []
    if len(input_list) > 0:
        for i in range(len(input_list)):
            outputList.append([])
            for j in range(len(input_list[i])):
                outputList[i].append([])

        for i in range(len(input_list)):
            for j in range(len(input_list[i])):
                outputList[i][j] = input_list[j][i]
        return outputList
    else:
        return outputList


# %%
# Create a function that can split a nested list into chunks
# chunk size is given by parameter
# return type: list
# function name must be: split_into_chunks
# input parameters: input_list,chunk_size


# %%
def split_into_chunks(input_list, chunk_size):
    outputList = []
    tmpList = []
    ctr = 0

    for i in input_list:
        tmpList.append(i)
        ctr += 1
        if ctr == chunk_size:
            outputList.append(tmpList)
            ctr = 0
            tmpList = []

    return outputList


# %%
# Create a function that can merge n dictionaries
# return type: dictionary
# function name must be: merge_dicts
# input parameters: *dict

# %%


def merge_dicts(*args):
    outputDict = {}
    for i in args:
        outputDict = outputDict | i
    return outputDict


# %%
# Create a function that receives a list of integers and sort them by parity
# and returns with a dictionary like this: {"even":[...],"odd":[...]}
# return type: dict
# function name must be: by_parity
# input parameters: input_list


# %%
def by_parity(input_list):
    numDict = {"even": [], "odd": []}
    for i in range(len(input_list)):
        if input_list[i] % 2 == 0:
            numDict["even"].append(input_list[i])
        else:
            numDict["odd"].append(input_list[i])
    return numDict


# %%
# Create a function that receives a dictionary like this: {"some_key":[1,2,3,4],"another_key":[1,2,3,4],....}
# and return a dictionary like this : {"some_key":mean_of_values,"another_key":mean_of_values,....}
# in short calculates the mean of the values key wise
# return type: dict
# function name must be: mean_key_value
# input parameters: input_dict


# %%
def mean_key_value(input_dict):
    for key in input_dict.keys():
        input_dict[key] = sum(input_dict[key]) / len(input_dict[key])
    return input_dict


# %%
# If all the functions are created convert this notebook into a .py file and push to your repo
