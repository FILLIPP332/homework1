def lines(line1, line2):
    if(type(line1) != str or type(line2) != str):
        return('0')
    elif(line1 == line2):
        return('1')
    elif(len(line1) != len(line2)):
        if(line2 == 'learn'):
            return(3)
        elif(len(line1) > len(line2)):
            return(2)
        else:
            return('error')

 
line1 = input('строка1')
line2 = input('строка2')
print(type(line1))
print(lines(line1, line2))
