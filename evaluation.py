from stack import Stack
       
def prefixEval(prefixExpr):
    operandStack = Stack()
    tokenList = prefixExpr.split()
    tokenList.reverse()
    operatorList = ['+', '-', '*', '/', '^', '**']

    for token in tokenList:
        if token not in operatorList:
            operandStack.push(float(token))
        else:
            operand1 = operandStack.pop()
            operand2 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(float(result))
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "^" or op == "**":
        return op1 ** op2
    else:
        return op1 - op2