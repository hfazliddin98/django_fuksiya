import random
ism  = input('Username kiriting ')
try:
    def user_name(x):
        son = random.randint(0,9)
        teskari = x[::-1]
        print(f'{teskari}{son}')

    user_name(ism)
except:
    print('Ismni tog`ri kiritmadingiz ')
