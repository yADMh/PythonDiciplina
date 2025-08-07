km_por_dia = 21              
ano_2_digitos = 25           
gasto_diario = 300 + ano_2_digitos  

total_em_uma_semana = km_por_dia * 7
diferenca_100_reais = 100 - gasto_diario
dias_que_500_cobre = 500 // gasto_diario
porcentagem_gasto_diario = gasto_diario % 100
media_diaria_custo_por_km = gasto_diario / km_por_dia

print("Total em uma semana (km):", total_em_uma_semana)
print("Diferença entre 100 reais e o gasto diário:", diferenca_100_reais)
print("Quantos dias o valor de R$500 cobre:", dias_que_500_cobre)
print("Porcentagem do gasto diário em relação a 100:", porcentagem_gasto_diario)
print("Média diária de custo por km:", media_diaria_custo_por_km)