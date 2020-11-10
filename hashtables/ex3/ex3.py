def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    array_dict = {}

    for i in arrays:
        for j in i:
            if j in array_dict:
                array_dict[j] += 1
            else:
                array_dict[j] = 1

    # print('the dict', array_dict)

    for key in array_dict.keys():
        if array_dict[key] == len(arrays):
            result.append(key)


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10,20)) + [1, 2, 3])
    arrays.append(list(range(50,60)) + [1, 2, 3])
    arrays.append(list(range(70,80)) + [1, 2, 3])

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
