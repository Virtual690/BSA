password = 'B.S.A'
p = input('password : ')

if p == password :
    print()

    print('๑۞๑,¸¸,ø¤º°`°๑۩   🎀  CALCULATOR  🎀   ۩๑°`°º¤ø,¸¸,๑۞๑')
    print('˜”*°•.˜”*°• Made By The B.S.A Group •°*”˜.•°*”˜')

    print()

    while True:   # for starting the infinity loop

        a = int(input('1st Number : '))
        s = input("'+','-','*','/' Here : ")

        if s.lower() == 'q':  # for exit the function [ varial name . lower() ]
            print('Exiting...')
            break  # for take a rest . and aging continue

        b = int(input('2nd Number : '))

        if s == '+':
            print()
            print('𝓐𝓷𝓼𝔀𝓮𝓻 : ')
            print(a + b)
            print()



        elif s == '-':
            print()
            print('𝓐𝓷𝓼𝔀𝓮𝓻 : ')
            print(a - b)
            print()


        elif s == '*':
            print()
            print('𝓐𝓷𝓼𝔀𝓮𝓻 : ')
            print(a * b)
            print()


        elif s == '/':
            print()
            print('𝓐𝓷𝓼𝔀𝓮𝓻 : ')
            print(a / b)
            print()


        else:
            print(' ---🅴🆁🅾🆁🆁 - --')

            print()
            print()
else :
    print('Worng')
    while True :
        print('Wrong Password')
