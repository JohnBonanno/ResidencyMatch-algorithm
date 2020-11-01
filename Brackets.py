'''
[Abdullah A, John B]
'''

def Brackets(s):
    
    stack = []

    openBrackets = ['(','{','[']
    closedBrackets = [')','}',']']

    # get each bracket in s
    for bracket in s:

        # push to stack if it's an open bracket
        if bracket in openBrackets:
            stack.append(bracket)

        else: # it's a closed bracket

            # can't have an empty stack if it's a closed bracket 
            if len(stack) == 0:
                return False

            # pop the open bracket if it matches the closed bracket
            if (openBrackets[closedBrackets.index(bracket)] == stack[len(stack) - 1]):
                stack.pop()

    # return true if stack is empty and false otherwise
    return not len(stack)