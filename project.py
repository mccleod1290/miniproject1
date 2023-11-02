import dns.resolver
import argparse
import socket

# List of common DNS record types to enumerate
DNS_RECORD_TYPES = ["A", "AAAA", "CNAME", "MX", "TXT", "PTR", "NS", "SOA", "SRV", "CAA", "SPF", "DNSKEY", "DS", "NAPTR", "TLSA", "SSHFP"]

def is_valid_domain(target):
    try:
        # Check if the input is a valid domain name
        dns.resolver.query(target, 'A')
        return True
    except dns.exception.DNSException:
        pass
    return False

def is_valid_ip(target):
    try:
        # Check if the input is a valid IP address
        socket.inet_pton(socket.AF_INET, target)
        return True
    except socket.error:
        pass
    try:
        socket.inet_pton(socket.AF_INET6, target)
        return True
    except socket.error:
        pass
    return False

def enumerate_dns(target, record_type):
    try:
        answers = dns.resolver.query(target, record_type)
        print(f'{target} {record_type} records:')
        for answer in answers:
            print(answer)
    except dns.resolver.NXDOMAIN:
        pass  # Subdomain does not exist
    except dns.resolver.NoAnswer:
        pass  # No records found for the subdomain
    except dns.exception.Timeout:
        print(f'Timed out while querying {record_type} for {target}.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

def enumerate_all_dns(target, wordlist):
    for record_type in DNS_RECORD_TYPES:
        print(f"Enumerating {record_type} records for {target}:")
        enumerate_dns(target, record_type)

    if is_valid_domain(target):
        print(f"\nEnumerating subdomains of {target} for all record types from wordlist {wordlist}:")
        for record_type in DNS_RECORD_TYPES:
            enumerate_subdomains(target, wordlist, record_type)
    else:
        print(f"\nTarget is an IP address. Skipping subdomain enumeration.")

def enumerate_subdomains(target, wordlist, record_type):
    for line in open(wordlist):
        subdomain = line.strip()
        subdomain_target = f"{subdomain}.{target}"
        enumerate_dns(subdomain_target, record_type)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='DNS Enumeration Tool')
    parser.add_argument('target', help='The domain name or IP address to enumerate DNS records for')
    parser.add_argument('wordlist', help='Path to the subdomain wordlist file')

    args = parser.parse_args()
    target = args.target
    wordlist = args.wordlist

    enumerate_all_dns(target, wordlist)

