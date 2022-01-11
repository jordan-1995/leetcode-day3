# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    new_list = set()

    for element in nums:
        if element in new_list:
            print("Contains duplicate")
        else:
            new_list.add(element)
    return False

containsDuplicate([1, 2, 3, 4, 1])