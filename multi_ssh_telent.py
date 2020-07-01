"""Configure a Cisco Device Using SSH/TELNET method for
multiple devices using Device CSV and Configuration Template"""
# Import the Connection Library created on the same folder
import connection

device_details = input("Enter Device List CSV File Name:-")
config_file = input("Enter the Config File Name:-")
# MULTI_SSH_TELNET is a class defined in connection library
device_data = connection.MULTI_SSH_TELNET(config_file, device_details)
device_data.connect()
