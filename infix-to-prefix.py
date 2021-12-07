from stack import Stack

def inToPre(infixexp):
    infixList = infixexp.split()
    infixList.reverse()
    output = []
    stack = Stack()
    prec = {"^": 4 , "*": 3 , "/": 3 , "+": 2, "-":2 , ")": 1}

    for token in infixList:
        if token not in "^*/+-)(":
            output.append(token)

        elif token == ")":
            stack.push(token)

        elif token == "(":
            top = stack.pop()
            while top != ")":
                output.append(top)
                top = stack.pop()

        elif token == "^":
            while not stack.isEmpty() and prec[token] <= prec[stack.peek()]:
                output.append(stack.pop())   
            stack.push(token)

        elif stack.isEmpty() or prec[token] >= prec[stack.peek()]:
            stack.push(token)    

        elif prec[token] < prec[stack.peek()]:
            while not stack.isEmpty() and prec[token] < prec[stack.peek()]:
                output.append(stack.pop())   
            stack.push(token)

    while not stack.isEmpty():
        output.append(stack.pop())

    output.reverse()   

    return " ".join(output) 