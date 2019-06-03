想用python实现这样一个功能，当我在程序中输入1时，把excel表中A列列名输出出来，例如：我输入1，程序打印A，我输入2，程序打印B，我输入3，
程序打印C，我输入26，程序打印Z，我输入27，程序打印AA等等这样以此类推，我随便输入一个数，Python程序就把对应EXCEL表的列名返回给我，程序该怎么实现。
input_num = 21485
 convert_list = []
 excel_column = ""
 char_list = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
 
 while True:
     quotient = input_num//26
     mod = input_num%26
     convert_list.insert(0,mod)
     if quotient > 26:
         input_num = quotient
     elif quotient == 0:
         break
     else:
         convert_list.insert(0,quotient)
         break
 for i in convert_list:
     excel_column = excel_column + char_list[i-1]
 print(excel_column)
 
更好的写法：
def convertToTitle(n: int) -> str:
    return ('' if n <= 26 else convertToTitle((n-1)//26)) + chr((n-1)%26+ord('A'))
或者也可以用组合子的方式写，比如求第703列的列名：
(lambda f,n:f(f,n))(lambda f,n:('' if n <= 26 else f(f,(n-1)//26)) + chr((n-1)%26+ord('A')),703)
