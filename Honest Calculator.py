msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_ = ["Are you sure? It is only one digit! (y / n)",

        "Don't be silly! It's just one number! Add to the memory? (y / n)",

        "Last chance! Do you really want to embarrass yourself? (y / n)"]


# function:is_one_digit()
def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


# function:check()
def check(v1, v2, v3):
    msg = ''
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)
    else:
        pass


memory = 0
while True:
    flag1 = flag2 = 1
    print(msg_0)
    calc = input()
    try:
        x, oper, y = calc.split()
    except ValueError:
        print("please input operands in the correct way, such as:5 * 4. Don't ignore the white")
        continue
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    for i in [x, y]:
        try:
            float(i)
        except ValueError:
            print(msg_1)
            flag1 = 0
            break
    if flag1 == 0:
        continue
    x, y = list(map(float, [x, y]))
    if oper not in ['+', '-', '*', '/']:
        print(msg_2)
        continue
    else:
        check(x, y, oper)
        if oper == '+':
            result = x + y
        elif oper == '-':
            result = x - y
        elif oper == '*':
            result = x * y

        else:
            if y == 0:
                print(msg_3)
                continue
            result = x / y
    print(result)

    # msg_4
    while True:
        print(msg_4)
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msg_[msg_index - 10])
                    answer = input()
                    if answer == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer == 'n':
                        break
            else:
                memory = result
        elif answer != 'n':
            continue

        # msg_5
        while True:
            print(msg_5)
            answer = input()
            if answer == 'y':
                break
            elif answer == 'n':
                flag2 = 0
                break
            else:
                continue
        break
    if flag2 == 0:
        break
