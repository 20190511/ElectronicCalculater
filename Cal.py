import math

def calcum_cal(r_list: list):
    total_sum = 0.0
    simense = 0.0
    for item in r_list:
        if item == 0:
            return -1
        simense += 1/item

    total_sum = 1/simense
    print(r_list, end=" : ")
    print(round(total_sum, 3))
    return total_sum

def calcumR():
    r_list = map(float, input("Put Your number : ").split())
    calcum_cal(r_list=r_list)




def serial_volt():
    r = list(map(float, input("(volt, [저항들...]) >> ").split()))
    volt = r[0]
    regit = r[1:]
    total_regit = sum(regit)
    for i, r_ in enumerate(regit):
        regit[i] = r_ / total_regit * volt

    print(list, end=" : ")
    print(regit)

def sum_volt():
    e = list(map(float, input("[전압들...] >> ").split()))
    print(sum(e))

if __name__ == "__main__":
    while(1):
        s = input("식 : ")
        plus_list = s.split("+")
        total_sum = 0
        for e_plus in plus_list:
            if not "||" in e_plus:
                total_sum += float(e_plus.strip())
                continue
            var_list = e_plus.split("||")
            for i, e in enumerate(var_list):
                var_list[i] = float(e.strip())
            total_sum += calcum_cal(var_list)
        print(total_sum)

    '''
    while(1):
        check = int(input("1:병렬계산, 2:직렬전압계산, 3:+ >> "))
        if check == 1:
            calcumR()
        elif check == 2:
            serial_volt()
        elif check == 3:
            sum_volt()
        else:
            break
    '''
