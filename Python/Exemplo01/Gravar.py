arquivo = open('exemplo01.txt','w')

arquivo.write('Curso Python v3.0 \n')
arquivo.write('Aula Prática')
arquivo.close()


#leitura do arquivo texto

leitura = open('exemplo01.txt','r')
print(leitura.read())
leitura.close()

