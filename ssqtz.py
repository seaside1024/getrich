# coding=utf-8
import random
import datetime


def ssq_number():
    red = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
           "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33"]
    blue = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16']
    slice = random.sample(red, 6)  # 从35个红色球号码中随机获取6个数字，作为红色球号码
    blice = random.sample(blue, 1)  # 从12个蓝色色球号码中随机获取1个数字，作为蓝色球号码
    slice.sort()
    s = '-'.join(slice)
    b = '-'.join(blice)
    print('\n', '红球：', s, '  ', '蓝球：', b)
    str_save = '\n' + '   ' + '红球：' + s + '    ' + '蓝球：' + b + '\n'
    f = open(r'E:\sea\tz.txt', 'a')
    f.write(str_save)
    f.close()


def ssq_menu():
    print('\n******欢迎使用Seaside双色球机选程序******')
    while True:
        n = input('\n请输入您要机选的注数：')
        if n.isdigit():
            n = int(n)
            a = 1
            print('\n以下是您的投注号码：')
            now = datetime.datetime.now()
            t = now.strftime('%Y-%m-%d %H:%M:%S')
            t = '\n' + t + '\n' + '\n' + '   本次为您机选的双色球号码是：' + '\n'
            f = open(r'E:\sea\tz.txt', 'a')
            f.write(t)
            f.close()
            while n > 0:
                print('\n第', a, '注号码是：')
                ssq_number()
                n -= 1
                a += 1
            break
        else:
            print('\n你的输入有误，请输入正整数！')
            continue
    print("\n您的双色球机选完成，祝您发财中大奖！")
