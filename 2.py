#thanks for your valuable review ,recent submission was my submission only with reference from geeksforgeeks
#and its also on leetcode problems 
def search(nums, target) :
        if not nums:
            return -1
        l,h=0 ,len(nums)-1

        while l<=h:
            mid=(l+h)//2
            if target == nums[mid]:
                return mid
            if nums[l]<=nums[mid]:
                if nums[l]<= target <= nums[mid]:
                    h= mid-1
                else:
                    l=mid+1
            else:
                if nums[mid] <= target <=nums[h]:
                    l=mid+1
                else:
                    h=mid=1
        return -1
    
                
            
                
def linear_search(arr, key):
    for index, element in enumerate(arr):
        if element == key:
            return index
    return -1

def test_function(test_case):
    arr = test_case[0]
    #n=len(arr)
    key = test_case[1]
    if linear_search(arr, key) == search(arr, key):
        print("Pass")
    else:
        print("Fail")
#Given cases
print("Given Cases -----------------------------------------")
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #pass
test_function([[6, 7, 8, 1, 2, 3, 4], 6]) #pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])#pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])#pass
#edge cases
print("edge Cases ------------------------------------------")
test_function([[1], 0])#pass
test_function([[], -1])#pass
test_function([[], -1])#pass
test_function([[0], 10000]) #pass
test_function([["a"], "A"]) #pass

#egde test 2  large list
test_list=[i for i in range (1011,10000)]
print(test_list)
print("Length of the test_list for edge test 2-",len(test_list))
test_function([test_list, 6])
#egde test 3  large list with negative numbers
test_list=[i for i in range (1011,10000)]#
print(test_list)
print("Length of the test_list for edge test 3-",len(test_list))

#test_list.append([i for i in range (-1000,1011)])
test_function([test_list, -1000])




