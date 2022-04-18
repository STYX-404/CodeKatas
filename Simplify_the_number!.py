def simplify(number):
    x = str(number)
    length = len(x) - 1
    result =""
    for i in range(len(x)):
        
        if x[i] == "0" :
            i+=1
            length -= 1
        else:
            if i >0:
                result += "+"
            if i == len(x)-1:
                sub_result = x[i]
                result += sub_result 
            else:
                sub_result = x[i] +"*"+ str(10**length)
                length -= 1
                result += sub_result 
    return result