desconto_txt = '21'  

desconto_num = float(desconto_txt) / 3.14

valor_produto = 400.99

valor_desconto = valor_produto * (desconto_num / 100)

valor_final = valor_produto - valor_desconto

print("Valor final a ser pago: R$", round(valor_final, 2))