import re
try:
    with open('crime_scene_report.csv', 'r') as inp, open('results.csv', 'w') as out:
        data = inp.read() 
        relatorio = re.findall(r'(20180115,murder,.+?,"SQL City")',data)
        relatorio = list(set(relatorio))
        for dado in relatorio:
            out.write(dado + "|\n")
except IOError as e:
    print('Operation failed: %s' % e.strerror)




##### RESULTADOS #####

# 20180115,murder,"Security footage shows that there were 2 witnesses. 
# The first witness lives at the last house on ""Northwestern Dr"". 
# The second witness, named Annabel, lives somewhere on ""Franklin Ave"".","SQL City"|

