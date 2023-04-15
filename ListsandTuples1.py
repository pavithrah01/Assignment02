tuples_str = input("Enter a list of non-empty tuples separated by commas: ")
tuples_list = [tuple(int(elem.strip()) for elem in tup.split(",")) for tup in tuples_str.split()]
sorted_tuples = sorted(tuples_list, key=lambda x: x[-1])
print(sorted_tuples)
