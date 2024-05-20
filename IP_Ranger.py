def expand_ip_range(ip_address: str) -> None:
    """Expands the given IP address by iterating over the last octet from 0 to 255."""
    try:
        ip_parts = ip_address.strip().split('.')
        
        if len(ip_parts) != 4:
            raise ValueError("IP address must have exactly four octets")

        base_ip = '.'.join(ip_parts[:3])
        with open("Ranged_IPs.txt", "a") as file:
            for i in range(256):
                file.write(f"{base_ip}.{i}\n")

    except ValueError as e:
        print(f"\t\t [!] Invalid IP: {ip_address} - {str(e)}")

print('''
    ██████╗ ██╗  ██╗██╗███████╗██████╗ ███╗   ██╗
   ██╔═══██╗╚██╗██╔╝██║╚══███╔╝╚════██╗████╗  ██║
   ██║   ██║ ╚███╔╝ ██║  ███╔╝  █████╔╝██╔██╗ ██║
   ██║   ██║ ██╔██╗ ██║ ███╔╝   ╚═══██╗██║╚██╗██║
   ╚██████╔╝██╔╝ ██╗██║███████╗██████╔╝██║ ╚████║
    ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═════╝ ╚═╝  ╚═══╝                           
\t\t               IPs Ranger''')
input_filename = input("\t\t [!] Enter IPs List : ")

try:
    with open(input_filename, 'r', errors="ignore", encoding="utf8") as base_file:
        unique_ips = list(dict.fromkeys(base_file.readlines()))

    for ip in unique_ips:
        expand_ip_range(ip)
        print(f"\t\t [+] Completed: {ip.strip()}")

except FileNotFoundError:
    print("\t\t ! The file specified does not exist !")
except Exception as e:
    print(f" ! An error occurred: {str(e)} !")

