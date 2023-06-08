arquivo = open('primeiro.txt', 'w')
arquivo.write('Módulo 6\n')
arquivo.write('Curso de Python - Fundação Bradesco')
arquivo.close()

leitura=open('primeiro.txt', 'r')
print(leitura.read())
leitura.close()