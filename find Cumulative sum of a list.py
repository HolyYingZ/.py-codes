def cumulative_sum(my_list):
    cum_sum = 0
    cumulative_sum_list = []

    for num in my_list:
        cum_sum += num
        cumulative_sum_list.append(cum_sum)

    return cumulative_sum_list

numbers_list = [1, 2, 3, 4, 5]
result = cumulative_sum(numbers_list)

print("Original list:", numbers_list)
print("Cumulative sum list:", result)
