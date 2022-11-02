def calculator(number_1, number_2, operation):
    if operation == '+' :
        print ( '{} + {} = ' . format(number_1 , number_2))
        return ( number_1 + number_2 )
    elif operation == '-' :
        print ('{} - {} = ' . format(number_1 , number_2))
        return ( number_1 - number_2 )
    elif operation == '*' :
        print ('{} * {} = ' . format(number_1 , number_2))
        return ( number_1 * number_2 )
    elif operation == '/' :
        print (' {} / {} = ' . format( number_1 , number_2 ) )
        return ( number_1 / number_2 )
    else :
        return ('You have not typed a valid operator')
