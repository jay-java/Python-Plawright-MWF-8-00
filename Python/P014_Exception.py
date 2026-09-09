try:
    a = 10
    b = 2
    print(a/b)

except ZeroDivisionError as e:
    print('number cannot divide by 0 ')

except TypeError as e:
    print('data should be in type of numeric')

except Exception as e:
    print(e)

finally:
    print('this will execute always')
