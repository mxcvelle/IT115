#
import json



#Create the data dictionary

data = {

    'name': 'Michelle Nguyen',
    'age': 30,
    'city':'Mountlake Terrace, WA',
    'interests': ['graphic novels','video games','working out'],
    'is_student': True

}

##
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')