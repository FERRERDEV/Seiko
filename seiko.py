#!/usr/bin/python3
# python_version  3.8

# Imports
from consolemenu import *
from consolemenu.items import *

# Vars
target_ip = "127.0.0.1"
target_port = "80"
attacker_ip = "127.0.0.1"
attacker_port = "4444"

################################
# NMAP Scan
################################
def nmap_scan():
    return

################################
# MSFVenom
################################
def msfvenom_generator():
    return

################################
# Reverse shell payloads
################################
def reverse_shell_generator():
    return

################################
# IP Handling
################################
def set_ip_port(ip, port):
    input_ip = input("Target IP: ")

    try:
        socket.inet_aton(input_ip)
    except:
        print("Invalid IP address.")

    input_port = input("Target PORT: ")

    ip = input_ip
    port = input_port

################################
# MENU
################################

# Create the menu
menu = ConsoleMenu("Seiko", "Multi hacking tool")

# Set target ip/port
set_target_menu_item = FunctionItem("Set target -> " + target_ip + ":" + target_port, set_ip_port, [target_ip, target_port])

# Set attacker ip/port
set_attacker_menu_item = FunctionItem("Set attacker -> " + attacker_ip + ":" + attacker_port, set_ip_port, [attacker_ip, attacker_port])

# Stagged nmap scan
nmap_menu_item = FunctionItem("Staged nmap scan", nmap_scan)

# Generate msfvenom payloads
msfvenom_selection_menu = SelectionMenu(["Payload 1", "Payload 2", "Payload 3"])
msfvenom_menu_item = SubmenuItem("MSFVenom payload generator", msfvenom_selection_menu, menu)

# Generate reverse shell payloads
reverse_shell_selection_menu = SelectionMenu(["Payload 1", "Payload 2", "Payload 3"])
reverse_shell_menu_item = SubmenuItem("Reverse shell generator", reverse_shell_selection_menu, menu)

# Add the items to the menu
menu.append_item(set_target_menu_item)
menu.append_item(set_attacker_menu_item)
menu.append_item(nmap_menu_item)
menu.append_item(msfvenom_menu_item)
menu.append_item(reverse_shell_menu_item)

# Show the menu
menu.show()