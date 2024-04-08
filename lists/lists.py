#Finding the Maximum Element in a List:
def find_maximum(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num
# Example usage:
numbers = [5, 2, 9, 1, 6]
max_number = find_maximum(numbers)
print("The maximum number is:", max_number)
###########################################################
#Removing Duplicates from a List:
def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums

# Example usage:
numbers_with_duplicates = [1, 2, 3, 3, 4, 5, 5, 6]
unique_numbers = remove_duplicates(numbers_with_duplicates)
print("List with duplicates removed:", unique_numbers)
#############################################################

#Reversing a List:
def reverse_list(lst):
    return lst[::-1]

# Example usage:
original_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original_list)
print("Reversed list:", reversed_list)
##############################################################

#Checking for Palindromes:
def is_palindrome(word):
    return word == word[::-1]
# Example usage:
test_word = "radar"
if is_palindrome(test_word):
    print(test_word, "is a palindrome.")
else:
    print(test_word, "is not a palindrome.")
##############################################################

#Finding Common Elements in Two Lists:
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common_elements = find_common_elements(list_a, list_b)
print("Common elements:", common_elements)
##############################################################


#Calculating the Average of Elements in a List:
def calculate_average(nums):
    return sum(nums) / len(nums)

# Example usage:
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("Average:", average)

#############################################################
#Finding the Second Largest Element in a List:
def find_second_largest(nums):
    sorted_nums = sorted(nums)
    return sorted_nums[-2]

# Example usage:
numbers = [5, 10, 15, 20, 25]
second_largest = find_second_largest(numbers)
print("Second largest number:", second_largest)

#############################################################3
#Merging Two Sorted Lists:

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

# Example usage:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print("Merged list:", merged_list)

##########################################################
#Counting Occurrences of Elements in a List:

def count_occurrences(nums):
    occurrence_count = {}
    for num in nums:
        occurrence_count[num] = occurrence_count.get(num, 0) + 1
    return occurrence_count

# Example usage:
numbers = [1, 2, 3, 2, 1, 3, 2, 1, 1]
occurrences = count_occurrences(numbers)
print("Occurrences:", occurrences)


##########################################################################
#Splitting a List into Chunks of a Given Size:

def split_into_chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunked_list = split_into_chunks(my_list, 3)
print("Chunked list:", chunked_list)