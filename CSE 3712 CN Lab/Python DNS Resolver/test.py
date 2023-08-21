import socket
import struct

def resolve_dns(domain_name, dns_server):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)  # Set a timeout for receiving responses

    # Build the DNS query
    query_id = 12345  # Choose any query ID you like
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
                print(canonical_name)
                domain_name = canonical_name.decode()
                query = build_dns_query(domain_name, query_id)
            elif name_server:
                print(name_server)
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

    domain_name_end = response.find(b'\x00', 12) + 1
    answer_section = response[domain_name_end + 4:]  # Skip over the question section

    ip_addresses = []
    canonical_name = None
    name_server = None

    for _ in range(ancount):
        name, qtype, qclass, ttl, rdlength = struct.unpack('!HHHLH', answer_section[:12])
        if qtype == 1 and qclass == 1:  # A record and IN class
            ip_address = socket.inet_ntoa(answer_section[12:16])
            ip_addresses.append(ip_address)
        elif qtype == 5 and qclass == 1:  # CNAME record and IN class
            canonical_name = answer_section[12:12+rdlength]
        answer_section = answer_section[12 + rdlength:]

    for _ in range(nscount):
        name, qtype, qclass, ttl, rdlength = struct.unpack('!HHHLH', answer_section[:12])
        if qtype == 2 and qclass == 1:  # NS record and IN class
            name_server = answer_section[12:12+rdlength]
        answer_section = answer_section[12 + rdlength:]

    return ip_addresses, canonical_name, name_server

if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    dns_server = "8.8.8.8"  # Google Public DNS

    ip_addresses = resolve_dns(domain_name, dns_server)
    if ip_addresses:
        print("Resolved IP addresses:", ip_addresses)
    else:
        print("DNS resolution failed")
