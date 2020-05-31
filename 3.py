def quicksort(arr, start, end):
    if end - start > 1:
        p = partition(arr, start, end)
        quicksort(arr, start, p)
        quicksort(arr, p + 1, end)
 
 
def partition(arr, start, end):
    pivot = arr[start]
    i = start + 1
    j = end - 1
 
    while True:
        while (i <= j and arr[i] <= pivot):
            i = i + 1
        while (i <= j and arr[j] >= pivot):
            j = j - 1
 
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            arr[start], arr[j] = arr[j], arr[start]
            return j 


def rearrange_digits(input_list):
    
    if len(input_list) < 2:
        return input_list

    quicksort(input_list,0,len(input_list)-1)  # O(nlogn)
    first, second = '', ''
    for i in range(len(input_list) - 1, -1, -2):
        first += str(input_list[i])
        if i - 1 >= 0:
            second += str(input_list[i - 1])

    # print(first, second)
    return [int(first), int(second)]  # O(n + nlogn) gives O(nlogn)





def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

print((rearrange_digits([1, 2, 3, 4, 5])))
print((rearrange_digits([4, 6, 2, 5, 9, 8])))
print((rearrange_digits([2, 1])))
print((rearrange_digits([123])))
print((rearrange_digits([None])))
print((rearrange_digits([])))
print((rearrange_digits([2,9,7,1,8])))
print((rearrange_digits([7,5,1,6,4,2,6,5,3,7,4,1,0])))
print((rearrange_digits([123,456,789,103,1456,254,11456])))
print((rearrange_digits([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])))
print((rearrange_digits(["1","3","4","999","33333333"])))


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function([[2, 1], [2, 1]])
test_function([[123], [123]])
test_function([[], []])
test_function([[2,9,7,1,8], [871,92]])
test_function([[7,5,1,6,4,2,6,5,3,7,4,1,0], [765431, 765421]])
test_function([[123,456,789,103,1456,254,11456], [11456789254103, 1456456123]])
test_function([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0]])
test_function([[1,3,4,999,33333333], [3333333341, 9993]])



