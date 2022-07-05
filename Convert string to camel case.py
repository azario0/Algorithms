#Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
#The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

#Examples
#"the-stealth-warrior" gets converted to "theStealthWarrior"
#"The_Stealth_Warrior" gets converted to "TheStealthWarrior"



#SOLUTION 

def to_camel_case(text):
    txt=list(text)
    rtr=list(text)
    km=0
    for i in range(len(txt)) :
        if txt[i]=="-" or txt[i]=="_" :
            rtr[i-km+1]=rtr[i-km+1].upper()
            del(rtr[i-km])
            km=km+1
    s = ''.join(rtr)
    return s ;
