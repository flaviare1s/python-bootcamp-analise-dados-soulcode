import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTgdqgDOHWvjft1Aqp7YQ5YZXZR0BcZLQPFu3H25qEzcYYjnzCdTTYZKRlV6ZRhLZp2JhRvwR1x1U7i/pub?gid=265510342&single=true&output=csv')

print(df)

idade = df['Idade']

print(idade)

horas_exercicio = df['Horas de Exercício']

print(horas_exercicio)
