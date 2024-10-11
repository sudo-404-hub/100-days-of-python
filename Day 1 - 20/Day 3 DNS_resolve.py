## Day 3
# **3. Find the domain name using an IP address**
# For this Python challenge, you’ll want to import the Python socket library. That’s the only hint. 
# Write a function that accepts an IP address, makes a DNS request, and returns the domain name.


import socket

while True:
    try:
        input_domain = input("Enter IP to get domain name: ")
        print(socket.getfqdn(input_domain))
        # for domain to ip use socket.gethostnamebyaddr
    except:
        print("plz enter invaild IP")

# gethostbyaddr: Returns a tuple containing the primary hostname, aliases, and a list of IP addresses.
# getfqdn: Returns a string representing the FQDN( Fully Qualified Domain Name) of the local machine.