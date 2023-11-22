# Import the JSON module to work with JSON data
import json



# Create the data dictionaryc containing various information about a person

data = {

    
    'name': 'Michelle Nguyen',
    'age': 30,
    'city':'Mountlake Terrace, WA',
    'interests': ['graphic novels','video games','working out'],
    'is_student': True

}

# Store the dictonary data into a JSON file named 'data.json' with indentation for readability 
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print('Data has been written to data.json')

# Open the 'data.json' file for reading
with open ('data.json','r') as json_file:
    # Load the JSON data from 'data.json' and print the loaded data
    loaded_data = json.load(json_file)

# Confirm successful reading of 'data.json' and print the loaded data
print("Successfully able to read data.json")
print(loaded_data)

# Modify the loaded data: change age to 29 and add 'traveling' to the interests list
loaded_data['age'] = 29
loaded_data['interests'].append('traveling')

# Write the modified data back to 'data.json' with proper indentation 
with open('data.json','w') as json_file:

    json.dump(loaded_data, json_file, indent =4)

# Confirm that the modified data has been written to 'data.json' 
print('Modified data written to data.json')