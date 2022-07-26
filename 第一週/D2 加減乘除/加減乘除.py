print('123\'456')

#加減乘除
a=642
b=357
print(a+b)
print(a-b)
print(a*b)
print(a/b)

"""
使用input()函数獲取輸入的(字符串)
使用int()函数將輸入的值轉為整數
使用print()函數输出带占位符的字符串

Version: 1
Author: 
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))    #%d為整數之佔位符
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))     #%f為符點數之佔位符
print('%d // %d = %d' % (a, b, a // b))   #//為整除符號
print('%d %% %d = %d' % (a, b, a % b))   #%%為百分比之佔位符
print('%d ** %d = %d' % (a, b, a ** b))  #**為指數符號


a = 10
b = 3
a += b        # 同：a = a + b
a *= a + 2    # 同：a = a * (a + 2)
print(a)      # 得出195

"""
練習:將華氏溫度轉為攝氏溫度

Version: 1
Author: 
"""
f = float(input('請輸入華氏溫度: '))
c = (f - 32) / 1.8   #華氏轉攝氏公式
print('%.1f華氏溫度 = %.1f攝氏溫度' % (f, c))

