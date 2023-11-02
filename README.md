# miniproject1

# DNS Enumeration and Subdomain Discovery Tool

The DNS Enumeration and Subdomain Discovery Tool is a versatile Python script that simplifies the process of gathering information. 
This tool is designed for network professionals, penetration testers, and security researchers to automate DNS record enumeration and discover associated subdomains.

## Features

- Enumerate various DNS record types, including A, AAAA, CNAME, MX, TXT, and more.
- Supported DNS Record Types
    A
    AAAA
    CNAME
    MX
    TXT
    PTR
    NS
    SOA
    SRV
    CAA
    SPF
    DNSKEY
    DS
    NAPTR
    TLSA
    SSHFP
- Discover subdomains using a user-provided wordlist.
- Isolate project dependencies in a Python virtual environment to avoid conflicts with system packages.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/dns-enumeration-tool.git
   ```
   
2. Change to the project directory:
   ```bash
   cd dns-enumeration-tool
   ```
3. Create and activate a Python virtual environment:
```bash
python3 -m venv myenv
source myenv/bin/activate

```

4. Install the dependacy for the tool.
```bash
pip install dnspython
```
5. Run the tool.
```bash
python3 project.py <target> wordlist.txt
```

## Also feel free to check the pdf documentation which acts as the report to this miniproject.

   

   
7. 
