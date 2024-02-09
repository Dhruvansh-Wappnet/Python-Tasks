# 1. Create a program that prints the current date and time.
import datetime
current_date_time = datetime.datetime.now()
print("Current Date & Time: ", current_date_time)


# 2. Write a function to check if a given year is a leap year using the datetime module.
import datetime

def is_leap_year(year):  
    if(datetime(year, 2, 29)):
        return True
    else:
        return False

year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# 3. Write a program that sorts a list of datetime objects in ascending order.
import datetime
list = [datetime.datetime(2020, 8,  5), datetime.datetime(2019, 7, 14)]
list.sort()
print(f"Sorted List: {list}")


# 4. Create a dictionary representing a person with keys like 'name', 'age', 'country', and print each key-value pair.

person = {'name': 'John',
          'age': 25,
          'country':  'India'}

for items in person:
    print(items, ": ", person[items])
    

# 5. Write a program to merge two dictionaries.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

print("Merged dictionary:")
print(merge_dictionaries(dict1, dict2))


# 6. Write a program to find the intersection and union of two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection_of_sets = set1.intersection(set2) 
print(f"Intersection of Two Sets is : {intersection_of_sets}")
union_of_sets = set1.union(set2)
print(f"Union of Two Sets is : {union_of_sets}")


# 7. Create a function that takes a string as input and returns a dictionary containing the count of each character in the string.
string = input("Enter any string: ")
def  count_chars(string):
    char_count = {}
    for i in string:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count
print(count_chars(string))


# 8. Write a program that removes duplicates from a list.
# Method 1
# list = [1,2,3,1,2,4]
# new_list = []
# for items in list:
#     if items  not in new_list:
#         new_list.append(items)
        
# print(new_list)

# Method 2
list = [1,2,3,1,2,4]
set1 = set(list)
print(list(set1))


# 9. Create a function that takes a list of strings as input and returns a set containing unique words across all the strings.
def unique_words(strings):
    unique_words = set()

    for string in strings:
        words_set = set(string.split())
        unique_words.update(words_set)
    return unique_words

strings = ["This is a sample string", "another sample string here"]
print(unique_words(strings)) 


# 10. Write a program that counts the occurrences of words in a given string and stores them in a dictionary.
word_count = {}
string = list(input("Enter a string: "))

for word in string.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


# 11. Write a program that converts a given string to title case (capitalize the first letter of each word).
string = input("Enter a string: ")
print(string.title())


# 12. Create a function that calculates the total length of strings in a list.
def total_length(list):
    total = 0
    for item in list:
        if type(item) == str:
            total += 1
    return total

strings = ["Hello", "World", "Python", 4, 5]
print(total_length(strings))


# 13. Write a program that finds the most common element in a list.
lst = [9,1,0,6,6,2,0,8,2,1]

print(max(lst, key = lst.count))
# for i in lst:
#     dict = {}
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i]=1
# print(dict)
# max_count = max(dict.values())
# for x in dict:
#     if dict[x] == max_count:
#         print(x)

    
# 14. Create a function that checks if two lists have any common elements.
def common_elements(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
    return result

list1 = [1, 2, 5, 7, 58]
list2 = [87, 58, 0, 3, 1]
print(common_elements(list1, list2)) 


# 15. Write a program that converts a list of tuples into a dictionary.
list_of_tuple =[(1, 'a'), (2, 'b'), (3, 'c')]
print(dict(list_of_tuple))


# 16. Create a function that removes all occurrences of a specified key from a dictionary.
def remove_key(dictionary, key):
    del dictionary[key]

person = {'name': 'John',
          'age': 25,
          'country':  'India'}

print(remove_key(person,'name'))


# 17. Write a program that merges two dictionaries by adding their values for common keys.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merged_dict = merge_dictionaries(dict1, dict2)
print(merged_dict) 


# 18. Create a function that takes a list of numbers and returns the cumulative sum.
list = [9,1,0,6,6]

def  cum_sum(list):
    result = []
    total = 0
    for num in list:
        total += num
        result.append(total)
    return result

print(cum_sum(list))  


# 19. Write a program that extracts all the email addresses from a given text.
import re
text = "Please send your resume to info@company.com or john.doe@example.com"
emails = re.findall('[\w\.-]+@[\w\.-]+\.\w+', text)
print(emails)

    
# 20. Create a function that calculates the average length of words in a given sentence.
sentence = "Hello world! How are you today?"

def average_word_length(sentence):
    words = sentence.split()
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    
    return average_length

print(average_word_length(sentence))


# 21. Write a program that finds the difference between two lists.
list1 = [1,2,3,4]
list2 = [5,6,7,8]

set1 = set(list1)
set2 = set(list2)

difference_list = list(set1.difference(set2))
print(difference_list)


# 22. Create a function that returns the elements that are common to two sets.
def intersection(set1, set2):
    return list(set1.intersection(set2))

print(intersection(set1, set2))


# 23. Write a program that converts a list of strings into a single string with spaces between each word.
strings = ["Hello", "World"]
result = ' '.join(strings)
print(result)


# 24. Create a function that checks if a given string is a pangram (contains every letter of the alphabet at least once).
def check_pangram():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters = "The quick brown fox jumps over the lazy dog."
    present_letters = ""
    for letter in letters:
        if letter.lower() in alphabet:
            present_letters += letter.lower()
    if present_letters == alphabet:
        return True
    else:
        return False
        
print(check_pangram())


# 25. Write a program that finds the longest common prefix among a list of strings.
def longest_common_prefix(strs):
    shortest_str = min(strs)
    # print(shortest_str)
    for i, char in enumerate(shortest_str):
        # print(i,char)
        for other in strs:
            # print(other)
            if other[i] != char:
                # print(shortest_str[:i])
                return shortest_str[:i]
    return shortest_str

strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs)) 


# 26. Create a function that takes a list of numbers and returns the second largest number.
list = [9,1,0,6,6]

def second_largest_number(list):
    first = max(list)
    last = float('-inf')
    for i in list:
        if i > last and i < first:
            last = i
    return last
            
print(second_largest_number(list))


# 27. Write a program that converts a given string to lowercase and removes all punctuation marks.
string = "Hello Everyone!!"
string = string.lower()
for i in string:
    if not ('a' <= i <= 'z'):
        string = string.replace(i," ")
print(string)


# 28. Create a function that removes duplicates from a list while preserving the order.
list = [1,2,3,4]
set1 = set(list)
print(set1)


# 29. Write a program that finds the number of occurrences of each word in a given string.
string = input("enter")
string.split()

for i in string:
    dict = {}
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
    

# 30. Create a function that checks if a given list is sorted in ascending order.
list = [1,2,3,4,5]
def check_sorted(list):
    if  list == sorted(list):
        return True
    else:
        return False
print(check_sorted(list))


