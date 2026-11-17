#import json class library
import json

#json data
data1 = { 
    
    'name':'Mr bob',
    'age':'36',
    'city':'omaha, NE',
    'interests':['DIY', 'bull riding', 'history'],
    'is_student': False,
}


#
with open ('data1.json','w') as json_file:

    #Dump data dictionary into JSON file
    json.dump(data1, json_file, indent=4)

print("You have successfully written to data1")