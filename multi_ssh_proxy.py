"""Configure a Cisco Device Using SSH/TELNET method for
a single device and Configuration Template"""
# Import the Connection Library created on the same folder
# And getpass for colelcting password
import connection
import getpass


ip_add = input("Enter The SSH Proxy Server IP Adress:-")
user_name = input("Enter The Username:-")
pass_word = getpass.getpass()
device_details = input("Enter the Device IP List CSV File Name:-")
client_name = input("Enter the Client Name:-")
projet_type = input("Enter the Project Type:-")
project_name = input("Enter the Project Name:-")
config_file = input("Enter the Config File Name:-")
# SINGLE_SSH_TELNET_SENDCMD is a Class in connection library
device_data = connection.MULTI_SSH_TELNET_PROXY(
    ip_add,
    user_name,
    pass_word,
    device_details,
    projet_type,
    client_name,
    project_name,
    config_file,
)
device_data.connect()
print(newdata)
