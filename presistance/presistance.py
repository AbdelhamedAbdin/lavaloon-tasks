def presistance(num):
    while True:
        mult = 1
        arr = []
        # check if num > 9 or not
        if num > 9:
            for n in str(num):
                arr.append(int(n))
            for n in arr:
                mult *= n
            num = mult
            print(num)
        else:
            num = 0
            print(num)
            break


presistance(39)
presistance(999)
presistance(4)