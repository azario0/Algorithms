#Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

#Notes:

#Only lower case letters will be used (a-z). No punctuation or digits will be included.
#Performance needs to be considered.
#Examples
#scramble('rkqodlw', 'world') ==> True
#scramble('cedewaraaossoqqyt', 'codewars') ==> True
#scramble('katas', 'steak') ==> False

#SOLUTION
def scramble(s1, s2):
    s=1
    val='a'
    for i in range(25):
        if val in s2 and val in s1 and s2.count(val)<=s1.count(val):
            s=s*1
        elif val in s2 :
            s=0
        elif val not in s1 and val in s2:
            s=1
        val=ord(val)+1
        val=chr(val)
        
    if s==1 : 
        return True
    else :
        return False
