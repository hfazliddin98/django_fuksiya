

try:
    def convert_add(my_list):
        yigindi = 0
        for qiymat in my_list:
            yigindi += int(qiymat)
        return yigindi

    # Test qilish
    raqamlar = ['2', '4', 6, 8, '15']
    jami = convert_add(raqamlar)
    print("Yig'indi:", jami)
except:
    print('list malumot turida sonlardan foydalaning ')