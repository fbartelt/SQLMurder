import re
try:
    with open('person.csv', 'r') as inp, open('results2.csv', 'w') as out:
        data = inp.read()
        witness1 = re.findall(r'(\d+,.+?,.+?,.+?,"Northwestern Dr",.+\n)',data)
        #witness1 = list(set(witness1))
        atual = witness1[0]
        for line in witness1:
            number_line = re.findall(r'\d+,.+?,.+?,(.+?),"Northwestern Dr",.+\n',line)
            number_atual = re.findall(r'\d+,.+?,.+?,(.+?),"Northwestern Dr",.+\n',atual)
            if(int("".join(number_line)) > int("".join(number_atual))):
                atual = line
        out.write("Witness1|" + "".join(atual))
        witness2 = re.findall(r'(\d+,"Annabel.+?,.+?,.+?,"Franklin Ave",.+\n)',data)
        witness2 = list(set(witness2))
        out.write("Witness2|" + "".join(witness2))
        
except IOError as e:
    print('Operation failed: %s' % e.strerror)


#### RESULTADOS ####
#99826,"Ivy Kazarian",994470,892,"Northwestern Dr",208359813
#16371,"Annabel Miller",490173,103,"Franklin Ave",318771143


