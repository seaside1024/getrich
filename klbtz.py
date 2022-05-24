# coding=utf-8
import random
import datetime


def klb_number():
    red = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18",
           "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35","36",
           "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53","54",
           "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70","71", "72",
           "73", "74", "75", "76", "77", "78", "79", "80"]
    slice = random.sample(red, 10)  # 从80个号码中随机获取10个数字，作为选10投注号码
    slice.sort()
    s = '-'.join(slice)
    print('\n', '红球：', s, '  ', )
    str_save = '\n' + '   ' + '红球：' + s + '    ' +  '\n'
    f = open(r'E:\sea\tz.txt', 'a')
    f.write(str_save)
    f.close()


def klb_menu():
    print('\n******欢迎使用Seaside快乐8机选程序******')
    while True:
        n = input('\n请输入您要机选的注数：')
        if n.isdigit():
            n = int(n)
            a = 1
            print('\n以下是您的投注号码：')
            now = datetime.datetime.now()
            t = now.strftime('%Y-%m-%d %H:%M:%S')
            t = '\n' + t + '\n' + '\n' + '   本次为您机选的快乐8号码是：' + '\n'
            f = open(r'E:\sea\tz.txt', 'a')
            f.write(t)
            f.close()
            while n > 0:
                print('\n第', a, '注号码是：')
                klb_number()
                n -= 1
                a += 1
            break
        else:
            print('\n你的输入有误，请输入正整数！')
            continue
    print("\n您的快乐8机选完成，祝您发财中大奖！")
