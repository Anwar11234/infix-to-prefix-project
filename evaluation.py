from stack import Stack
       
def evaluation(prefixexp):
    prefixList = prefixexp.split()
    s = Stack()

    for i in range(len(prefixList) - 1 , -1 , -1):
        if prefixList[i] in "+-*/^":
            first = s.pop()
            second = s.pop()
            result = doMath(first , second , prefixList[i])
            s.push(result)

        else:    
            s.push(float(prefixList[i]))

    return s.pop()        

def doMath(op1 , op2 , operator):
    
    if operator == '*':
        return op1 * op2
    elif operator == '/':
        return op1 / op2               
    elif operator == '-':
        return op1 - op2               
    elif operator == '+':
        return op1 + op2    
    elif operator == '^':
        return op1 ** op2    