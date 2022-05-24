# coding=utf-8
import random
import datetime


def qxc_number():
    red = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9'] #定义red为红色球列表
    blue = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    slice = (random.choice(red),random.choice(red),random.choice(red),random.choice(red),random.choice(red),random.choice(red))
    blice = random.sample(blue, 1) # 从15个蓝色色球号码中随机获取1个数字，作为蓝色球号码
    s = '-'.join(slice) #将slice从元组类型转换成字符串，并且用-分隔
    b = '-'.join(blice)
    print('\n', '红球：', s, '  ', '蓝球：', b)
    str_save = '\n' + '   ' + '红球：' + s + '    ' + '蓝球：' + b + '\n'
    f = open(r'E:\sea\tz.txt', 'a')
    f.write(str_save)
    f.close()


def qxc_menu():
    print('\n******欢迎使用Seaside七星彩机选程序******')
    while True:
        n = input('\n请输入您要机选的注数：')
        if n.isdigit():
            n = int(n)
            a = 1
            print('\n以下是您的投注号码：')
            now = datetime.datetime.now()
            t = now.strftime('%Y-%m-%d %H:%M:%S')
            t = '\n' + t + '\n' + '\n' + '   本次为您机选的七星彩号码是：' + '\n'
            f = open(r'E:\sea\tz.txt', 'a')
            f.write(t)
            f.close()
            while n > 0:
                print('\n第', a, '注号码是：')
                qxc_number()
                n -= 1
                a += 1
            break
        else:
            print('\n你的输入有误，请输入正整数！')
            continue
    print("\n您的七星彩机选完成，祝您发财中大奖！")
