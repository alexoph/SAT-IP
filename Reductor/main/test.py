'''
Created on Jul 22, 2019

@author: alejandro
'''

zincified = ''
clause = 0
variables = []
file = open("../../InstanciasSAT/test.cnf", "r")
for line in file:
    if line[0] == 'c':
        zincified += '%' + line[1:]
    elif line[0] == 'p':
        words = line[0:].split(' ')
        if words[1] != 'cnf':
            print('Error en el formato del archivo (no es cnf)')
            exit()
        else:
            numvar = int(words[2])
            numclause = int(words[3])
            for x in range(numvar):
                variables.append('X' + str(x))
            for var in variables:
                zincified += 'var 0..1: ' + var + '; var 0..1: n_' + var + ';\n'
            zincified += '\n'
            for var in variables:
                zincified += 'constraint ' + var + ' + ' +  'n_' + var + ' = 1\n'
            zincified += '\n'
    else:
        clause += 1
        words = line[0:].split(' ')
        for var in words:
            variable = int(var)
            literal = variables[abs(variable) - 1]
            if variable < 0:
                print('nell')
#print(zincified)







