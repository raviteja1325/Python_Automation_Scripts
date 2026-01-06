#In python we have in built functions for file operation to read or write a file
#script to make changes to server config file or any such file using python


def update_server_config(file_path, key, value):

#open is an inbuilt function which helps in reading adn writing changes to any file in python
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    with open(file_path, "w") as file:

        for line in lines:

            if key in line:
                file.write(key + "=" + value + "\n" )
            
            else:
                file.write(line)

server_config_file_path = "server.conf"
key_to_update= "MAX_CONNECTIONS"
new_value= "1000"

update_server_config(server_config_file_path, key_to_update, new_value)
