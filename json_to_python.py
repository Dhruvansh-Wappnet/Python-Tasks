'''
To work with JSON data python has built in package called json.
We can call it by using  import statement: import json
There are two main methods provided by the json module to work with JSON data, namely dumps and load.
1) json.dumps() method can convert a Python object into a JSON string.

  Syntax: json.dumps(dictionary, indent) 
  
  Parameters:
  dictionary - name of dictionary which should be converted to JSON object.
  indent - defines the number of units for indentation
  
2)  json.load() method is used to parse a JSON file and return the result as a Python object.

  Syntax: json.loads(json_string)
  
Let's see an example on how to use these functions.
"""
import json
# Creating a simple dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Original Dictionary:\n", my_dict)

# Converting Python dict to JSON String
json_data = json.dumps(my_dict, indent=4)
print("\nJSON Data:\n", json_data)

# Now let's try to convert back JSON String to Python Object
parsed_json = json.loads(json_data)
print("\nParsed JSON:\n", parsed_json)
"""

There is one another method called dump.
This method works exactly like dumps but instead of returning a string, it writes the output directly to a file.
  Syntax: json.dump(dict, file_pointer) 

  Parameters:
  
  dictionary - name of dictionary which should be converted to JSON object.
  file pointer - pointer of the file opened in write or append mode.
  
Let's see an example on how to use these function.
  """
  import json
  
# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
  """


'''









