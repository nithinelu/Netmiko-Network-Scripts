"""Enter Show Command and save the Ouput on Project
folder for single and multiple Cisco Devices"""
# Import the Connection Library created on the same folder
# And getpass for colelcting password
import connection
import getpass

user_input = input("Enter 1 for single Device or 2 for Multiple Device:-")
# Number of devices to be configured will be idenfied base on User input
if int(user_input) == 1:
    ip_add = input("Enter The Device IP Adress:-")
    user_name = input("Enter The Username:-")
    pass_word = getpass.getpass()
    device_type = input("Enter the Device Type:-")
    user_cmd = input("Enter the Command:-")
    client_name = input("Enter the Client Name:-")
    projet_type = input("Enter the Project Type:-")
    project_name = input("Enter the Project Name:-")
    # SINGLE_SSH_TELNET_SENDCMD is a Class in connection library
    device_data = connection.SINGLE_SSH_TELNET_SENDCMD(
        ip_add,
        user_name,
        pass_word,
        device_type,
        user_cmd,
        client_name,
        projet_type,
        project_name,
    )
    device_data.connect()
if int(user_input) == 2:
    user_cmd = input("Enter the Command:-")
    device_details = input("Enter the Devie List CSV file  Name:-")
    client_name = input("Enter the Client Name:-")
    projet_type = input("Enter the Project Type:-")
    project_name = input("Enter the Project Name:-")
    # MULTI_SSH_TELNET_SENDCMD is a Class in connection library
    device_data = connection.MULTI_SSH_TELNET_SENDCMD(
        user_cmd, device_details, client_name, projet_type, projet_type, project_name
    )
    device_data.connect()
