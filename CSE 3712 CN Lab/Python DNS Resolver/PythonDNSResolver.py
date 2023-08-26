import socket
import struct
import csv


def resolve_dns(domain_name, dns_server):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Set a timeout for receiving responses
    client_socket.settimeout(5)

    # Build the DNS query

    # Choose any query ID you like
    query_id = 12345
    query = build_dns_query(domain_name, query_id)

    while True:
        try:
            # Send the DNS query to the DNS server
            client_socket.sendto(query, (dns_server, 53))

            # Receive the DNS response
            response, server_address = client_socket.recvfrom(1024)

            # Parse the DNS response
            ip_addresses, canonical_name, name_server = parse_dns_response(response)

            if ip_addresses:
                return ip_addresses
            elif canonical_name:
                domain_name = canonical_name.decode()
                query = build_dns_query(domain_name, query_id)
            elif name_server:
                # Convert an ip address of 32 bits binary format into string format
                dns_server = socket.inet_ntoa(name_server)
                query = build_dns_query(domain_name, query_id)
            else:
                break

        except socket.timeout:
            print("DNS resolution timed out")
            break

    client_socket.close()
    return []


def build_dns_query(domain_name, query_id):
    # Build the DNS query message as per the DNS protocol
    # This involves constructing the header and question section
    # For simplicity, we'll use a basic query without any additional options

    # Header (ID, Flags, QDCOUNT, ANCOUNT, NSCOUNT, ARCOUNT)
    header = struct.pack('!HHHHHH', query_id, 0x0100, 1, 0, 0, 0)

    # Question Section (QNAME, QTYPE, QCLASS)
    domain_parts = domain_name.split('.')
    qname = b''
    for part in domain_parts:
        qname += bytes([len(part)]) + part.encode()
    qname += b'\x00'  # End of domain name
    qtype = struct.pack('!H', 1)  # QTYPE A (IPv4 address)
    qclass = struct.pack('!H', 1)  # QCLASS IN (Internet)

    query = header + qname + qtype + qclass
    return query


def parse_dns_response(response):
    # Parse the DNS response to extract IP addresses, CNAME, and NS records from the answer section
    # This involves reading the header, question section, and answer section

    header = struct.unpack('!HHHHHH', response[:12])
    qdcount = header[2]
    ancount = header[3]
    nscount = header[4]

    # Finds the end of the domain name in the DNS question
    domain_name_end = response.find(b'\x00', 12) + 1
    # Skip over the question section and goes to the start of the answer
    answer_section = response[domain_name_end + 4:]

    # Empty list to store the ip addresses
    ip_addresses = []
    # Both CNAME and NS is initialized to none, if found we store it here
    canonical_name = None
    name_server = None

    for _ in range(ancount):
        # Unpacking the DNS response in short fields
        name, qtype, qclass, ttl, rdlength = struct.unpack('!HHHLH', answer_section[:12])
        if qtype == 1 and qclass == 1:  # A record and IN class
            ip_address = socket.inet_ntoa(answer_section[12:16])
            ip_addresses.append(ip_address)
        elif qtype == 5 and qclass == 1:  # CNAME record and IN class
            canonical_name = answer_section[12:12 + rdlength]
        answer_section = answer_section[12 + rdlength:]

    for _ in range(nscount):
        name, qtype, qclass, ttl, rdlength = struct.unpack('!HHHLH', answer_section[:12])
        if qtype == 2 and qclass == 1:  # NS record and IN class
            name_server = answer_section[12:12 + rdlength]
        answer_section = answer_section[12 + rdlength:]

    return ip_addresses, canonical_name, name_server


if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    dns_server = "8.8.8.8"  # Google Public DNS

    field_names = ['DOMAIN', 'IP ADDRESS']

    # file = open("resolved_dns.txt", "a")
    #
    # if domain_name in file.readlines():
    #     print("Found in cache_file!")
    #     print()

    ip_address = [{'DOMAIN': domain_name, 'IP ADDRESS': resolve_dns(domain_name, dns_server)}]

    with open('resolved_dns.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # writer.writeheader()
        # writer.writerows(ip_address)
        csv_writer.writerow(['DOMAIN', 'IP ADDRESS'])

    # if ip_addresses:
    #     print("Resolved IP addresses:", ip_addresses)
    # else:
    #     print("DNS resolution failed")

# Test:
# outlook.office365.com
# substrate.office.com
# server.events.data.microsoft.com
# dns.msftncsi.com
# a.root-servers.net
# 	198.41.0.4, 2001:503:ba3e::2:30
# 	Verisign, Inc.
# b.root-servers.net
# 	199.9.14.201, 2001:500:200::b
# 	University of Southern California,
# Information Sciences Institute
# c.root-servers.net
# 	192.33.4.12, 2001:500:2::c
# 	Cogent Communications
# d.root-servers.net
# 	199.7.91.13, 2001:500:2d::d
# 	University of Maryland
# e.root-servers.net
# 	192.203.230.10, 2001:500:a8::e
# 	NASA (Ames Research Center)
# f.root-servers.net
# 	192.5.5.241, 2001:500:2f::f
# 	Internet Systems Consortium, Inc.
# g.root-servers.net
# 	192.112.36.4, 2001:500:12::d0d
# 	US Department of Defense (NIC)
# h.root-servers.net
# 	198.97.190.53, 2001:500:1::53
# 	US Army (Research Lab)
# i.root-servers.net
# 	192.36.148.17, 2001:7fe::53
# 	Netnod
# j.root-servers.net
# 	192.58.128.30, 2001:503:c27::2:30
# 	Verisign, Inc.
# k.root-servers.net
# 	193.0.14.129, 2001:7fd::1
# 	RIPE NCC
# l.root-servers.net
# 	199.7.83.42, 2001:500:9f::42
# 	ICANN
# m.root-servers.net
# 	202.12.27.33, 2001:dc3::35
# 	WIDE Project
