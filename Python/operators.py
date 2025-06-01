

# Preciso consertar !

numI = input(int("Iº: "))
numII = input(int("IIº: "))

print ("\n Dados os números: ", numI," e ", numII)


# Os resultados são numéricos

print ("\n\n==============================\n", "Operadores Aritméticos")


print ("Soma: ", numI + numII)
print ("Subtração: ", numI - numII)
print ("Multiplicação: ", numI * numII)
print ("Divisão: ", numI / numII)
print ("Parte Inteira da Divisão: ", numI // numII)
print ("Potência: ", numI ** numII)
print ("Resto da Divisão: ", numI % numII)







# Os resultados são true e false, incremento de valores e comparações

print ("\n\n=============================\n", "Operadores de Atribuitivos")

print (" Implicação ", numI = numII, numII = numI) 
print ("\n")

print ("Atribuição de Valor com Soma: \n")
numI += 2
numII += 3
print ("\n")

print ("Atribuição de Valor com Subtração: \n")
numI += 2
numII += 3
print ("\n")

print ("Atribuição de Valor com Multiplicação:\n")
numI *= 2
numII *= 3
print ("\n")

print ("Atribuição de Valor com Divisão:\n")
numI /= 2
numII /= 3
print ("\n")


print ("Atribuição de Walrus:\n")
(numI := 2)
(numII := 3)



# Os resultados são true ou false somente

print ("\n\n=============================================\n", "Operadores de Comparação\n")

print ("Operador de Igualdade : ", numI == numII, "ou", numII == numI)
print ("\n")

print ("Operador de Diferença: ", numI != numII, "ou", numII != numI)
print ("\n")

print ("Operadores de Comparação: ", numI > numII, " ou ", numII < numI)
print ("\n")

print ("Operadores de Comparação com Igualdade: ", numI >= numII, "ou", numII <= numI)
print ("\n")



# Os resultados são baseados nas operações entre true ou false

print ("\n\n==============================================\n", "Operadores Lógicos\n")

print ("And: ", numI and numII, " ou ", numII and numI)
print ("\n")

print ("Or: ", numI or numII, "ou", numII or numI)
print ("\n")

print ("Not: ", not numI, "ou" ,not numII)
print ("\n")





# Compara se dois resultados estão inclusos um no outro como na teoria de conjuntos com true ou false

print ("\n\n================================================\n", "Operador de Identidade\n")

print ("Is: ", numI is numII, "ou", numII is numI)





# Verifica se tais valores estão pertencentes em outro como na teoria dos conjuntos com true ou false ou "Membership"

print ("\n\n====================================================\n", "Operador de Pertencimento\n")

print ("In: ", numI in numII, "ou", numII in numI)
print ("\n")