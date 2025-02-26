import numpy as np

notas_turma_A = [70, 72, 74, 76, 78, 80, 82, 84, 86, 88] 
notas_turma_B = [50, 60, 70, 80, 90, 100, 70, 60, 90, 100]

media_turma_A = np.mean(notas_turma_A) # Usando NumPy
media_turma_B = sum(notas_turma_B) / len(notas_turma_B) # Usando Python

print("Média da turma A:", media_turma_A)
print("Média da turma B:", media_turma_B)

variancia_turma_A = np.var(notas_turma_A)
variancia_turma_B = np.var(notas_turma_B)

print("Variância da turma A:", variancia_turma_A)
print("Variância da turma B:", variancia_turma_B)

desvio_padrao_turma_A = np.std(notas_turma_A)
desvio_padrao_turma_B = np.std(notas_turma_B)

print("Desvio padrão da turma A:", desvio_padrao_turma_A)
print("Desvio padrão da turma B:", desvio_padrao_turma_B)

# Conclusão: A turma B tem mais variabilidade e dispersão do que a turma A, pois suas notas estão mais espalhadas. A turma A é mais homogênea.
