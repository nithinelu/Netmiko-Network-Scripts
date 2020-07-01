"""SSH TELENT and SERIAL conenction
functions using NETMIKO Library"""
from netmiko import (
    ConnectHandler,
    redispatch,
    NetmikoAuthenticationException,
    NetMikoTimeoutException,
)
import time
import csv
import os


class SINGLE_SSH_TELNET:
    """Function to Connect with the device
    using SSH and TELNET"""

    def __init__(
        self, ip, username, password, device_type, config_file,
    ):
        # Argument IP,USERNAME,PASSWORD,DEVICE TYPE,CONFIG FILE.
        self.ip = ip
        self.username = username
        self.password = password
        self.device_type = device_type
        self.config_file = config_file

    def connect(self):

        device = {
            "device_type": self.device_type,
            "ip": self.ip,
            "username": self.username,
            "password": self.password,
        }
        with open(self.config_file) as f:
            lines = f.read().splitlines()
        print("==========================")
        print("Connecting" + device["ip"])
        print("==========================")
        try:
            net_connect = ConnectHandler(**device)
        except NetmikoAuthenticationException:
            print("Entered Credentials are Invalid.")
        except NetMikoTimeoutException:
            print("Cannot connect to this device.")

        output = net_connect.send_config_set(lines)
        print(output)
        print("========================")
        print("Configuration Completed")
        print("========================")


class MULTI_SSH_TELNET:
    """Function to Connect with the Multiple device
    using SSH and TELNET"""

    def __init__(self, config_file, device_details):
        # Argument IP,USERNAME,PASSWORD,DEVICE TYPE,CONFIG FILE.
        self.config_file = config_file
        self.device_details = device_details

    def connect(self):
        with open(self.config_file) as f:
            lines = f.read().splitlines()
        device_list = csv.DictReader(open(self.device_details, encoding="utf-8-sig"))
        for devices in device_list:
            # Itrate the process for all devices in DEVICE CSV File
            print("==========================")
            print("Connecting" + devices["ip"])
            print("==========================")
            try:
                net_connect = ConnectHandler(**devices)
            except NetmikoAuthenticationException:
                print("Entered Credentials are Invalid." + devices["ip"])
            except NetMikoTimeoutException:
                print("Cannot connect to this device." + devices["ip"])
                break
            net_connect = ConnectHandler(**devices)
            print("Configuring " + devices["ip"])
            output = net_connect.send_config_set(lines)
            print(output)
        print("========================")
        print("Configuration Completed")
        print("========================")


class SINGLE_SSH_TELNET_SENDCMD:
    """Function to Connect with the device
    using SSH and TELNET and Send User Specific Command"""

    def __init__(
        self,
        ip,
        username,
        password,
        device_type,
        user_cmd,
        client_name,
        project_type,
        project_name,
    ):
        # Argument User Specific Command .
        self.ip = ip
        self.username = username
        self.password = password
        self.device_type = device_type
        self.user_cmd = user_cmd
        self.client_name = client_name
        self.project_type = project_type
        self.project_name = project_name

    def connect(self):

        device = {
            "device_type": self.device_type,
            "ip": self.ip,
            "username": self.username,
            "password": self.password,
        }
        client_directory = self.client_name
        project_type_directory = self.project_type
        project_directory = self.project_name
        # Parent Directory path
        parent_dir = "/Users/nithineluvathingal/Documents/Office_Backup/"

        # Path
        path = os.path.join(parent_dir, client_directory)
        # Client  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        path = os.path.join(path, project_type_directory)
        # project_type  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        path = os.path.join(path, project_directory)
        device_path = path
        # Client/project_type  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        print("==========================")
        print("Connecting " + device["ip"])
        print("==========================")
        try:
            net_connect = ConnectHandler(**device)
        except NetmikoAuthenticationException:
            print("Entered Credentials are Invalid.")
        except NetMikoTimeoutException:
            print("Cannot connect to this device.")
        output = net_connect.send_command(self.user_cmd)
        print(output)
        f = open(path + "/" + device["ip"] + "-" + self.user_cmd + ".txt", "w")
        f.write(output)
        print("===============================================================")
        print("Output Saved at " + path)
        print("===============================================================")


class MULTI_SSH_TELNET_SENDCMD:
    """Function to Connect with the Multiple device
    using SSH and TELNET  and  Send User Specific Command"""

    def __init__(
        self,
        proxy_ssh,
        user_cmd,
        device_details,
        project_type,
        client_name,
        project_name,
    ):
        # Argument User Specific Command .
        self.proxy_ssh = proxy_ssh
        self.user_cmd = user_cmd
        self.device_details = device_details
        self.project_type = project_type_directory
        self.client_name = client_name
        self.project_name = project_name

    def connect(self):
        # Directory
        client_directory = self.client_name
        project_type_directory = self.project_type
        project_directory = self.project_name
        # Parent Directory path
        parent_dir = "/Users/nithineluvathingal/Documents/Office_Backup/"

        # Path
        path = os.path.join(parent_dir, client_directory)
        # Client  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        path = os.path.join(path, project_type_directory)
        # project_type  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        path = os.path.join(path, project_directory)
        device_path = path
        # Client/project_type  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        device_list = csv.DictReader(open(self.device_details, encoding="utf-8-sig"))
        for devices in device_list:
            # Itrate the process for all devices in DEVICE CSV File
            print("==========================")
            print("Connecting " + devices["ip"])
            print("==========================")
            try:
                net_connect = ConnectHandler(**devices)
            except NetmikoAuthenticationException:
                print("Entered Credentials are Invalid." + devices["ip"])
            except NetMikoTimeoutException:
                print("Cannot connect to this device." + devices["ip"])
                break
            print("====================================")
            print("Sending Command to  " + devices["ip"])
            print("====================================")
            output = net_connect.send_command(self.user_cmd)
            print(output)
            f = open(path + "/" + devices["ip"] + "-" + self.user_cmd + ".txt", "w")
            f.write(output)
        print("===============================================================")
        print("Output Saved at " + path)
        print("===============================================================")


class MULTI_SSH_TELNET_PROXY:
    """SSH Connection using Proxy"""

    def __init__(
        self,
        ip,
        username,
        password,
        device_details,
        project_type,
        client_name,
        project_name,
        config_file,
    ):
        # Argument User Specific Command .
        self.ip = ip
        self.username = username
        self.password = password
        self.device_details = device_details
        self.project_type = project_type
        self.client_name = client_name
        self.project_name = project_name
        self.config_file = config_file

    def connect(self):
        # Directory
        client_directory = self.client_name
        project_type_directory = self.project_type
        project_directory = self.project_name
        # Parent Directory path
        parent_dir = "/Users/nithineluvathingal/Documents/Office_Backup/"

        # Path
        path = os.path.join(parent_dir, client_directory)
        # Client  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        path = os.path.join(path, project_type_directory)
        device_path = path
        # project_type  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        path = os.path.join(path, project_directory)
        # Client/project_type  Directory path
        if not os.path.exists(path):
            try:
                os.mkdir(path)
            except OSError:
                print("Creation of the directory %s failed" % path)
            else:
                print("Successfully created the directory %s " % path)
        # Proxy Server Connection
        # Device type should be Termainl Server
        net_connect = ConnectHandler(
            device_type="terminal_server",
            ip=self.ip,
            username=self.username,
            password=self.password,
        )
        print("============================")
        print("Connecting SSH Porxy Server")
        print("============================")
        device_list = csv.DictReader(
            open(
                device_path + "/" + "DEVICE DETAILS" + "/" + self.device_details,
                encoding="utf-8-sig",
            )
        )
        with open(device_path + "/" + "DEVICE DETAILS" + "/" + self.config_file) as f:
            lines = f.read().splitlines()
        # Manually handle interaction in the Terminal Server (fictional example, but
        # hopefully you see the pattern)
        net_connect.write_channel("\r\n")
        time.sleep(1)
        output = net_connect.read_channel()
        print(output)
        # Should hopefully see the terminal server prompt
        print(output)
        for devices in device_list:
            # Itrate the process for all devices in DEVICE CSV File
            net_connect.write_channel("ssh " + devices["ip"] + "\r\n")
            time.sleep(10)
            max_loops = 3
            i = 1
            while i <= max_loops:
                output = net_connect.read_channel()
                print(output)
                if "Username:" in output:
                    net_connect.write_channel(net_connect.username + "\r\n")
                    time.sleep(10)
                    output = net_connect.read_channel()
                    print(output)
                    # Search for password pattern / send password
                if "password:" in output:
                    net_connect.write_channel(net_connect.password + "\r\n")
                    time.sleep(2)
                    output = net_connect.read_channel()
                    print(output)
                    # Did we successfully login
                    if ">" in output or "#" in output:
                        break
                # Search for password pattern / send password
                if "Password:" in output:
                    net_connect.write_channel(net_connect.password + "\r\n")
                    time.sleep(2)
                    output = net_connect.read_channel()
                    print(output)
                    # Did we successfully login
                    if ">" in output or "#" in output:
                        break
                # Search for password pattern / send password
                if "password" in output:
                    net_connect.write_channel(net_connect.password + "\r\n")
                    time.sleep(2)
                    output = net_connect.read_channel()
                    print(output)
                    # Did we successfully login
                    if ">" in output or "#" in output:
                        break
                if "Password" in output:
                    net_connect.write_channel(net_connect.password + "\r\n")
                    time.sleep(2)
                    output = net_connect.read_channel()
                    print(output)
                    # Did we successfully login
                    if ">" in output or "#" in output:
                        break
                net_connect.write_channel("\r\n")
                time.sleep(3)
                i += 1
            # We are now logged into the end device
            # Dynamically reset the class back to the proper Netmiko class
            redispatch(net_connect, device_type="cisco_ios")
            new_output = net_connect.send_config_set(lines)
            print(new_output)

