tuples_str = input("Enter a list of non-empty tuples: ")
tuples_list = [tuple(int(elem.strip()) for elem in tup.split(",")) for tup in tuples_str.split()]

for i in range(len(tuples_list)):
    for j in range(i+1, len(tuples_list)):
        if tuples_list[i][-1] > tuples_list[j][-1]:
            tuples_list[i], tuples_list[j] = tuples_list[j], tuples_list[i]
print(tuples_list)
