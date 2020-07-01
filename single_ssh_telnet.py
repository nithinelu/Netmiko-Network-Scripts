"""Configure a Cisco Device Using SSH/TELNET method for
a single device and Configuration Template"""
# Import the Connection Library created on the same folder
# And getpass for colelcting password
import connection
import getpass

ip_add = input("Enter The Device IP Adress:-")
user_name = input("Enter The Username:-")
pass_word = getpass.getpass()
device_type = input("Enter the Device Type:-")
config_file = input("Enter the Config File Name:-")
# SINGLE_SSH_TELNET is a class defined in connection library
device_data = connection.SINGLE_SSH_TELNET(
    ip_add, user_name, pass_word, device_type, config_file
)
device_data.connect()
