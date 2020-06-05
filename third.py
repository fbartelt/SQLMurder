import re
try: 
    with open('interview.csv', 'r') as inp, open('results3.csv', 'w') as out, open('results2.csv', 'r') as res:
        data = inp.read()
        previous_info = res.read()
        wit1_id = re.findall(r'Witness1\|(\d+),".+?",\d+,\d+,".+?",\d+\n',previous_info)
        wit2_id = re.findall(r'Witness2\|(\d+),".+?",\d+,\d+,".+?",\d+\n',previous_info)
        print(wit1_id,wit2_id)
        print("".join(wit1_id)+',(".*?\n")')
        confession_wit_1 = re.findall("".join(wit1_id)+',(".*?\n?"\n)',data)
        confession_wit_2 = re.findall("".join(wit2_id)+',(".*?\n?"\n)',data)
        out.write("Confession of first witness:\n" + "".join(confession_wit_1) + 
            "\nConfession of second witness:\n" + "".join(confession_wit_2))

except IOError as e:
    print('Operation failed: %s' % e.strerror)

#### RESULTADOS ####
#Confession of first witness:
#"I heard a gunshot and then saw a man run out. He had a ""Get Fit Now Gym"" bag. 
# The membership number on the bag started with ""48Z"". Only gold members have those bags. 
# The man got into a car with a plate that included ""H42W""."

#Confession of second witness:
#"I saw the murder happen, and I recognized the killer from my gym when I was working out last week on 
# January the 9th."
