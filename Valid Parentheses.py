#Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, 
#and false if it's invalid.

#Examples
#"()"              =>  true
#")(()))"          =>  false
#"("               =>  false
#"(())((()())())"  =>  true




#SOLUTION 
def valid_parentheses(string):
    cmp=0
    cp=0
    lst=list(string)
    if string !='':
        for i in lst:
            cmp=cp
            if i=='(':
                sign=False
                for j in lst[cmp:]:
                    print(lst)
                    
                    if j==')':
                        sign=True
                        del (lst[cmp])
                        break
                    cmp=cmp+1
            elif i==')':
                return False
            cp=cp+1
        cp=0    
        return sign
    else : 
        return True
    
