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

# 
with open ('data.json','r') as json_file:

    loaded_data = json.load(json_file)

print("Successfully able to read data.json")
print(loaded_data)

#
loaded_data['age'] = 29
loaded_data['interests'].append('traveling')

#
with open('data.json','w') as json_file:

    json.dump(loaded_data, json_file, indent =4)

print('Modified data written to data.json')