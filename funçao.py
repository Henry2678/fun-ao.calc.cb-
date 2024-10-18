#calculadora
def soma_calc(num1, num2):
    soma = nm1+nm2
    return f"{soma}"
def subtraçao_calc(num1, num2):
    sub = num1-num2
    return f"{sub}"
def divisao_calc(num1, num2):
    div = num1/num2
    return f"{div}"
def multiplicaçao_calc(num1, num2):
    mult = num1*num2
    return f"{mult}"
operacao = int(input("digite o numero que corresponde a operacao "))
if operacao == 1:
    nm1 = int(input("digite o primeiro numero "))
    nm2 = int(input("digite o primeiro numero "))
    resultado_soma = soma_calc(nm1, nm2)
    print(f"o resultado da soma e {resultado_soma} ")
elif operacao == 2:
    nm1 = int(input("digite o primeiro numero "))
    nm2 = int(input("digite o primeiro numero "))
    resultado_sub = subtraçao_calc(nm1, nm2)
    print(f"o resultado da subtracao e {resultado_sub} ")
elif operacao == 3:
    nm1 = int(input("digite o primeiro numero "))
    nm2 = int(input("digite o primeiro numero "))
    reultado_mut = multiplicaçao_calc(nm1, nm2)
    print(f"o resultado da multiplicaçao e {reultado_mut} ")
elif operacao == 4:
    nm1 = int(input("digite o primeiro numero "))
    nm2 = int(input("digite o primeiro numero "))
    resultado_div = divisao_calc(nm1, nm2)
    print(f"o resultado da divisao e {resultado_div} ")




    