#Complete the function that

#accepts two integer arrays of equal length
#compares the value each member in one array to the corresponding member in the other
#squares the absolute value difference between those two values
#and returns the average of those squared absolute value difference between each member pair.


 #SOLUTION : 
 def solution(array_a, array_b):
    val=array_a
    sum=0
    for i in range(len(array_a)):
        val[i]=abs(array_a[i]-array_b[i])
        val[i]=val[i]*val[i]
    for i in range(len(val)):
        sum=sum+val[i]
    
    return sum/len(val)
