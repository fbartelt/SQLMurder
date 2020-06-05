import re
try:
    with open('get_fit_now_member.csv', 'r') as memb, open('drivers_license.csv', 'r') as car, open('get_fit_now_check_in.csv', 'r') as chk, open('person.csv', 'r') as ppl, open('interview.csv', 'r') as ivw, open('results4.csv', 'w') as out:
        members = memb.read()
        cars = car.read()
        check_in = chk.read()
        people = ppl.read()
        interview = ivw.read()
        possible_murderers = re.findall(r'48Z.+?,\d+,".+?",\d+,gold',members)
        out.write("Possible murderers:\n")
        for m in possible_murderers:
            out.write(''.join(m)+"\n")
        possible_cars = re.findall(r'(\d+,\w+,\d+,\w+,\w+,\w+,.*?H42W.*?,\w+,.+?)\n', cars)
        out.write("\nPossible cars:\n")
        for m in possible_cars:
            out.write(''.join(m)+"\n")
        id_list = re.findall(r'(48Z.+?),\d+,".+?",\d+,gold',possible_murderers[0])
        for i in range(1,len(possible_murderers)):
            atual = re.findall(r'(48Z.+?),\d+,".+?",\d+,gold',possible_murderers[i])
            id_list = "".join(id_list)+'|'+"".join(atual)
        checkin_list = re.findall('((?:'+ id_list+r'),\d+0109,\d+,\d+)\n',check_in)
        out.write("\nPossible checkins:\n")
        for m in checkin_list:
            out.write(''.join(m)+"\n")
        for i in range(len(checkin_list)):
            gym_id = re.findall(r'(.+?),\d+0109,\d+,\d+',checkin_list[i])
            name = re.findall("".join(gym_id) + r',\d+,(".+?"),\d+,gold',"".join(possible_murderers))
            person = re.findall(r'(\d+),'+''.join(name)+ r',.+?,.+?,".+?",.+\n',people)
            confession = re.findall(''.join(person) + r',(".*?\n?"\n)', interview)
            out.write("\n"+''.join(name) + " Confession was:\n" + ''.join(confession)+"\n")
        
except IOError as e:
    print('Operation failed: %s' % e.strerror)




