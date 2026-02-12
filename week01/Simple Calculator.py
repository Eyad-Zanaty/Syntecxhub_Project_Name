def calculator(num01, num02, operator):
    '''
    calculator function
    '''
    
    result= 0

    if operator.strip() == '+':
        result= num01 + num02

    elif operator.strip() == '-':
        result= num01 - num02

    elif operator.strip() == '*':
        result= num01 * num02

    elif operator.strip() == '/':
        if num02 == 0:
            return "math error"
        else:
            result= num01 / num02

    else:
        return "unvalid operator"
    
    return result


x= True

while x== True:
    
    try: # handling input type error
        num01= int(input("Input your first number: "))
        num02= int(input("Input your seconed number: "))
        operator= input("Input your operator(+,-,*,/): ").strip()
    
    except:
        print("input Error")
        continue

    result= calculator(num01, num02, operator)
    
    print(result)
    
    while True: # handling repeating answer
        
        ask= input("Do you want to perform repeated calaculation (yes/no): ")
        
        if ask == 'yes':
            x= True
            continue
            
        elif ask == 'no':
            x= False
            break
        
        else:
            print('invalid')
