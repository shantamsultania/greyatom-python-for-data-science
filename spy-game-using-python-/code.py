# --------------
#Code starts here

#Function to read file
def read_file(path):
    #Opening of the file located in the path in 'read' mode
    file = open(path,'r')
    #Reading of the first line of the file and storing it in a variable
    sentence = file.readline()
    #Closing of the file
    file.close()
    #Returning the first line of the file
    return sentence
    

#Calling the function to read file
sample_message = read_file(file_path)
#Printing the line of the file

print(sample_message)

message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

print(message_1)
print(message_2)
#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    message_a = int(message_a)
    message_b = int(message_b)
    quotient = message_b // message_a
    #Returning the quotient in string format
    return str(quotient)


#Calling the function 'fuse_msg'
secret_msg_1 = fuse_msg(message_1,message_2)

#Calling the function to read file
message_3 = read_file(file_path_3)


#Printing the secret message 


#Function to substitute the message
def substitute_msg(message_c):
    
    #If-else to compare the contents of the file
    if (message_c == 'Red'):
        sub = 'Army General'
    elif (message_c == 'Green'):
        sub= 'Data Scientist'
    else:
        seb = 'Marine Biologist'
    #Returning the substitute of the message
    return sub
    

#Calling the function 'substitute_msg'
secret_msg_2 = substitute_msg(message_3)


#Printing the secret message
print(secret_msg_2)


message_4=read_file(file_path_4)
message_5=read_file(file_path_5)
print(message_4)
print(message_5)
#Function to compare message
def compare_msg(message_d,message_e):
    #Splitting the message into a list
    a_list = message_d.split()
    b_list = message_e.split()
    
    #Splitting the message into a list
    c_list = [i for i in a_list if i not in b_list]
    
    #Comparing the elements from both the lists
    final_msg = " ".join(c_list)
    
    #Combining the words of a list back to a single string sentence
    
    
    #Returning the sentence
    return final_msg
    

#Calling the function to read file
secret_msg_3 = compare_msg(message_4,message_5)

#Calling the function to read file

print(secret_msg_3)
#Calling the function 'compare messages'


#Printing the secret message
message_6 = read_file(file_path_6)

print(message_6)
#Function to filter message
def extract_msg(message_f):

    #Splitting the message into a list
    a_list = message_f.split()
    even_word = lambda x: len(x) %2 == 0
    #Creating the lambda function to identify even length wordd
    #Splitting the message into a list
    b_list = filter(even_word,a_list)
    
    #Combining the words of a list back to a single string sentence
    final_msg = " ".join(b_list)
    
    #Returning the sentence
    return final_msg
    
#Calling the function to read file

secret_msg_4 = extract_msg(message_6)

#Calling the function 'filter_msg'


#Printing the secret message

print(secret_msg_4)
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
secret_msg= " ".join(message_parts)

# define the path where you 
final_path= user_data_dir + '/secret_message.txt'

#Combine the secret message parts into a single complete secret message


#Function to write inside a file
def write_file(secret_msg,path):
    #Opening a file named 'secret_message' in 'write' mode
    file = open(path,'a+')
    file.write(secret_msg)

    #Writing to the file


    #Closing the file
    file.close

#Calling the function to write inside the file    
write_file(secret_msg,final_path)

#Printing the entire secret message

print(secret_msg)
#Code ends here


