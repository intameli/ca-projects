

try:
    n = int(input('num: '))
    d = int(input('num: '))
    q = n / d
    print(q)
except ZeroDivisionError:
    print("can't divide by 0")
except ValueError:
    print('Wrong input value type')
except Exception as e:
    print(e)
