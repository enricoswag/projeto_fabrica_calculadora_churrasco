convidados = int(input('Digite o numero de convidados: '))
# pré-definimos os valores de consumo de bebida por pessoa e o volume da garrafa
def calcular_bebidas(convidados, consumo_por_pessoa_ml=800, volume_garrafa_litro=2.25):
    total_ml = convidados * consumo_por_pessoa_ml  # calcula o consumo de bebidas total por convidado/ml
    total_litro = total_ml / 1000                  # converte o consumo para litro

    garrafas = int(total_litro / volume_garrafa_litro)  # divide o total pelo volume da garrafa
    if total_litro % volume_garrafa_litro > 0:      # se sobrar fração, acrescenta 1 garrafa
        garrafas += 1
    return total_litro, garrafas     # retorna total em litros e número de garrafas

def calcular_carne(convidados, consumo_por_pessoa_grama=400):
    total_gramas = convidados * consumo_por_pessoa_grama
    total_kg = total_gramas /1000
    return total_kg

litros, garrafas = calcular_bebidas(convidados)
carne_kg = calcular_carne(convidados)
print('\n__Quantidade total para Churrasco___')
print(f'Número de convidados: {convidados}')
print(f'Refrigerantes necessários: {litros:.2f} litros.')
