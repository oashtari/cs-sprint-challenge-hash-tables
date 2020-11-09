def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    twins = {}
    result = {}

    for number in a:
        twins[number] = number
        # print('twins', twins)

    for k,v in twins.items():
        # print('k', k)
        if k * -1 in twins:
            result[abs(k)] = 1
            # print('result', result)

    result_array = []

    if result == {}:
        return []

    for item in result.items():
        # print('result', result)
        # print('item', item)
        if item[0] != 0:
            result_array.append(item[0])
    
    return result_array

    # for i in range(len(a)):
    #     if a[i] > 0:
    #         twins[a[i]] = a[i]
    #     else:


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
