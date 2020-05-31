def sort_012(arr,n):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    cnt0 = 0   #count of 0
    
    cnt1 = 0 #count of 1
    cnt2 = 0 #count of 2
      
    # Count the number of 0s, 1s and 2s in the array 
    for i in range(n): 
        if arr[i] == 0: 
            cnt0+=1
          
        elif arr[i] == 1: 
            cnt1+=1
              
        elif arr[i] == 2: 
            cnt2+=1
      
    # Update the array 
    i = 0
      
    # Store all the 0s in the beginning 
    while (cnt0 > 0): 
        arr[i] = 0
        i+=1
        cnt0-=1
      
    # Then all the 1s 
    while (cnt1 > 0): 
        arr[i] = 1
        i+=1
        cnt1-=1
      
    # Finally all the 2s 
    while (cnt2 > 0): 
        arr[i] = 2
        i+=1
        cnt2-=1
      
    # Prt he sorted array
    #print(arr)
    return arr
     

def test_function(test_case):
    n=len(test_case)
    sorted_array = sort_012(test_case,n)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1])
test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
test_function([2])
test_function([])
test_function([2,2, 0])
test_function([0, 0, 0])
test_function([0, 0,  1, 1, 0])
test_function([0])
