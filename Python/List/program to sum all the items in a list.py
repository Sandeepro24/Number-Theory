#Write a Python program to sum all the items in a list.
list = [1,2,3,4,5,6,7,8,9,10]

li = sum(list)
print(f"The sum of all the items in a list = {li}")


#2nd method
def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
    return sum_numbers
print(sum_list([1,2,-8]))