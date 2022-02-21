def try_me(num1='6',num2='3',operation='+'):
    """
    Given two numbers and an arithmetic operation returns result
    """
    # convert decimal degrees to radians
    num1 = int(num1)
    num2 = int(num2)
    if operation == '-':
        result = num1 - num2
    elif operation == '/':
        result = num1 / num2
    elif operation == '*':
        result = num1 * num2
    else:
        result = num1 + num2
    return result

if __name__ == "__main__":
    num1 = 6
    num2 = 3
    result_ = try_me(num1,num2,'+')
    print(result_)
    