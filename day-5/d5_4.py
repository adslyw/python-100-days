def foo():
    a = 100
    print('a = %d' % a)

def bar():
    global b
    b = 200
    print('b = %d' % b)

def main():
    foo()
    bar()

if __name__ == '__main__':
    main()
