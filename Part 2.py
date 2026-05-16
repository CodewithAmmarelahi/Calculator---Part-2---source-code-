while True:

    ask = input('Do you want to take out percentage? (yes/no): ').lower()

    if ask == 'yes':

        part = float(input('Enter part value: '))
        whole = float(input('Enter whole value: '))

        percentage = (part / whole) * 100

        print('Percentage =', percentage, '%')

    elif ask == 'no':

        A = int(input('Enter first number: '))
        B = int(input('Enter second number: '))
        C = input('Enter your operation: ')

        if C == '+':
            print(A + B)

        elif C == '-':
            print(A - B)

        elif C == '*':  # * means multiply in python
            print(A * B)

        elif C == '/':  # / means divide in python
            print(A / B)

        else:
            print('Something went wrong.....')

    else:
        print('Please type yes or no')

    cont = input('Do you want to continue? (yes/no): ').lower()

    if cont == 'no':
        print('Exiting from calculator.....')
        break
