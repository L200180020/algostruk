def bilanganPrima():
    lower = 2 
    upper = 1000
    print("Bilangan prima antara",lower,"and",upper,":")
    for num in range(lower,upper + 1): 
        if num > 1: 
            for i in range(2,num): 
                if (num % i) == 0: 
                    break 
            else: 
                print(num)
