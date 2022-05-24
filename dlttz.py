# coding=utf-8
import random
import datetime


def dlt_number():
    red = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
           "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35"]
    blue = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    slice = random.sample(red, 5)  # 从35个前区号码中随机获取5个数字，作为红色球号码
    blice = random.sample(blue, 2)  # 从12个后区号码中随机获取2个数字，作为蓝色球号码，加入到红色球号码后面
    slice.sort()
    blice.sort()
    s = '-'.join(slice)
    b = '-'.join(blice)
    print('\n', '前区：', s, '  ', '后区：', b)
    str_save = '\n' + '   ' + '前区：' + s + '    ' + '后区：' + b + '\n'
    f = open(r'E:\sea\tz.txt', 'a')
    f.write(str_save)
    f.close()


def dlt_menu():
    print('\n******欢迎使用Seaside大乐透机选程序******')
    while True:
        n = input('\n请输入您要机选的注数：')
        if n.isdigit():
            n = int(n)
            a = 1
            print('\n以下是为您机选的号码：')
            now = datetime.datetime.now()
            t = now.strftime('%Y-%m-%d %H:%M:%S')
            t = '\n' + t + '\n' + '\n' + '   本次为您机选的大乐透号码是：' + '\n'
            f = open(r'E:\sea\tz.txt', 'a')
            f.write(t)
            f.close()
            while n > 0:
                print('\n第', a, '注号码是：')
                dlt_number()
                n -= 1
                a += 1
            break
        else:
            print('\n你的输入有误，请输入正整数！')
            continue
    print("\n您的大乐透机选完成，祝您发财中大奖！")
