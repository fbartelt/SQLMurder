import re
try:
    with open('drivers_license.csv', 'r') as car, open('person.csv', 'r') as ppl, open('get_fit_now_member.csv','r') as gym, open('facebook_event_checkin.csv', 'r') as evn, open('income.csv', 'r') as csh, open('interview.csv', 'r') as ivw, open('results5.csv', 'w') as out:
        cars = car.read()
        people = ppl.read()
        gyms = gym.read()
        evnt = evn.read()
        cash = csh.read()
        interview = ivw.read()
######### CHECK DOS CARROS
        possible_women = re.findall(r'\d+,\d+,\d+,.+?,red,female,.+?,Tesla,"Model S"', cars)
        out.write("Possible women by car and hair: \n")
        for pos in possible_women:
            out.write(''.join(pos)+"\n")
######### CHECK DOS NOMES BASEADO EM CNH
        out.write("\nPossible names: \n")
        possible_names = []
        for pos in possible_women:
            license_id = re.findall(r'(\d+),\d+,\d+,.+?,red,female,.+?,Tesla,"Model S"',pos)
            names = re.findall(r'(\d+,".+?",'+''.join(license_id) + r',\d+,".+?",\d+)\n',people)
            possible_names.append(''.join(names))
            out.write(''.join(names)+"\n")
######### CHECK DO INCOME DAS SUSPEITAS
        out.write("\n\nIncome das suspeitas\n")
        for woman in possible_names:
            ssn = re.findall(r'\d+,".+?",\d+,\d+,".+?",(\d+)',woman)
            income = re.findall(''.join(ssn)+ r',(\d+)\n',cash)
            out.write(woman + "\nIncome is:" + ''.join(income)+ "\n")
######### CHECK DE EVENTO
        out.write("\nPossible events info: \n")
        events = re.findall(r'(".+?",".+?","SQL Symphony Concert","201712\d\d")\n',evnt)
        event_list =[]
        for v in events:
            atual_id = re.match(r'(".+?"),".+?","SQL Symphony Concert","201712\d\d"',v).group(1)
            matches = re.findall(''.join(atual_id) + r',".+?","SQL Symphony Concert","201712\d\d"','\n'.join(events))
            if (len(matches)==3):
                event_list.append(matches)
        event_list = [list(x) for x in set(tuple(x) for x in event_list)]
        for v in event_list:
            out.write('\n'.join(v)+"\n\n")
######### CHEK DE MULHERES QUE COMPARECERAM AOS EVENTOS
        pp_list = []
        for v in event_list:
            person_id = re.findall(r'"(.+?)",".+?",".+?","\d+"',v[0])
            for pp in possible_names:
                pos_id = re.findall(r'(\d+),".+?",\d+,\d+,".+?",\d+', pp)
                if(''.join(person_id)==''.join(pos_id)):
                    pp_list.append(pp)
                    print(pp)

######### DEPOIMENTOS
        print(pp_list)
        for person in pp_list:
            person_id = re.findall(r'(\d+),".+?",\d+,\d+,".+?",\d+',''.join(person))
            confession = re.findall(''.join(person_id) + r',(".*?\n?")\n', interview)
            out.write("Depoimento de:\n" + ''.join(person) + "\n" + ''.join(confession)+"\n")

            
except IOError as e:
    print('Operation failed: %s' % e.strerror)




