import math

def calcum_cal(r_list: list):
    total_sum = 0.0
    simense = 0.0
    for item in r_list:
        if item == 0:
            return -1
        simense += 1/item

    total_sum = 1/simense
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


def sum_volt():
    e = list(map(float, input("[전압들...] >> ").split()))
    print(sum(e))

def cal_express(express: str):
    plus_list = express.split("+")
    total_sum = 0
    for e_plus in plus_list:
        if not "||" in e_plus:
            total_sum += float(e_plus.strip())
            continue
        var_list = e_plus.split("||")
        for i, e in enumerate(var_list):
            var_list[i] = float(e.strip())
        total_sum += calcum_cal(var_list)
    print(express + " : " + str(total_sum))
    return total_sum

def bracket_splitter(express:str):
    stack = []
    br_open = 0
    br_close = 0

    tmp_str = ""
    total_line = ""
    for ch in express:
        if "(" == ch:
            if len(tmp_str) != 0:
                stack.append(tmp_str)
                tmp_str = ""
            br_open += 1
        elif ")" == ch:
            print(tmp_str)
            if len(stack) != 0:
                tmp_str = stack.pop() + str(cal_express(tmp_str))
            elif tmp_str != "":
                total_line += str(cal_express(tmp_str))
            tmp_str = ""
            br_close += 1
        else:
            tmp_str += ch

    stack.append(tmp_str)
    if br_open != br_close:
        print("Your Express is wrong")
        return []
    else:
        if tmp_str == "":
            return total_line
        else:
            return round(cal_express(stack[0]), 3)

if __name__ == "__main__":
    s = input("식 : ")
    print(bracket_splitter(s))
