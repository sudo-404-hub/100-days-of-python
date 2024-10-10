## Day 3
# **3. Find the domain name using an IP address**
# For this Python challenge, you’ll want to import the Python socket library. That’s the only hint. 
# Write a function that accepts an IP address, makes a DNS request, and returns the domain name.


import socket

while True:
    try: 
        input_domain = input("Enter domain to get ip: ")
        print(socket.gethostbyname(input_domain))
        # socket.gethostbyaddr(ip) # ip to domain name.
    except:
        print("plz enter vaild domain name like [https://google.com] or [google.com]")


