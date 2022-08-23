import os
import linecache

temp = 298.15
target1 = 'Step           Time'

filelog = open('file.log', 'r')
count = 0
for line in filelog:
    count=count+1
    if target1 in line:
        linea = count

particular_line = linecache.getline('file.log',linea+1)
step = particular_line[0]
time  = particular_line[1]

step= float(particular_line.split()[0])
time= float(particular_line.split()[1])

datos = open('Energy', 'w')
datos.write('Density')

energy = 'gmx energy -f file.edr -b  ' + str(time/4) + ' < Energy'

os.system(energy)
print(energy)

