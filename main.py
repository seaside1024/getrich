# coding=utf-8
import dlttz
import klbtz
import qxctz
import ssqtz


def select():
    print('******欢迎使用Seaside中大奖机选程序******')
    print('      A:双色球,B:大乐透,C:七星彩,D:快乐8,Q:退出      ')
    while True:
        choose = input('\n请输入您的选择(A[双色球],B[大乐透],C[七星彩],D[快乐8],Q[退出])：')
        if choose == 'Q' or choose == 'q':
            print('\n已经为您退出，欢迎下次使用！')
            break
        elif choose == 'A' or choose == 'a':
            ssqtz.ssq_menu()
        elif choose == 'B' or choose == 'b':
            dlttz.dlt_menu()
        elif choose == 'C' or choose == 'c':
            qxctz.qxc_menu()
        elif choose == 'D' or choose == 'd':
            klbtz.klb_menu()
        else:
            print('你的输入有误，请输入A,B,C,Q！')
            continue

select()