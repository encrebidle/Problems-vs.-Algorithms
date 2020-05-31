def square_root(x):    
    if (x == 0 or x == 1): 
        return x
    elif x<0 :
        return None
   
    start = 1
    end = x    
    while start <= end: 
        mid = (start + end) // 2          
         
        if (mid*mid == x) : return mid              
        elif (mid * mid < x) :
            start = mid + 1
            ans = mid 
              
        else :
            end = mid-1
              
    return ans 

print("Given Test Cases----------------------------------")
print ("Pass" if  (3 == square_root(9)) else "Fail")
print ("Pass" if  (0 == square_root(0)) else "Fail")
print ("Pass" if  (4 == square_root(16)) else "Fail")
print ("Pass" if  (1 == square_root(1)) else "Fail")
print ("Pass" if  (5 == square_root(27)) else "Fail")
print("\n Edge cases--------------------------------------")
print ("Pass" if  (None == square_root(-1)) else "Fail")
print ("Pass" if  ( 625== square_root(390625)) else "Fail")
print ("Pass" if  (11111 == square_root(123456789)) else "Fail")
print ("Pass" if  (1 == square_root(1.2)) else "Fail")
print ("Pass" if  (351 == square_root(123456.123456)) else "Fail")
