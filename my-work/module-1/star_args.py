# *args

def add_all_numbers(list_of_nums):
    total = 0
    for num in list_of_nums:
        total += num
    return total

answer = add_all_numbers([1, 2, 3, 4, 5])
print(answer)

def add_all_numbers_star(*args):
    print("Args:", args)
    print("Type Args:", type(args))
    total = 0
    for num in args:
        total += num
    return total

answer = add_all_numbers_star(1, 2, 3, 4, 5)
print(answer)