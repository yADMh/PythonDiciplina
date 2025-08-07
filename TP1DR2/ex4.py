ano_2_digitos = 25            
tempo_minutos = 150 + ano_2_digitos 
tempo_horas = 2.25         

horas_equivalentes = tempo_minutos / 60  
minutos_equivalentes = tempo_horas * 60  

print("Horas equivalentes a", tempo_minutos, "minutos:", round(horas_equivalentes, 2))
print("Minutos equivalentes a", tempo_horas, "horas:", round(minutos_equivalentes, 2))