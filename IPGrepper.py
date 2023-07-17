import re

def grep_ip_addresses(file_path):
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"  # Regular expression pattern to match IP addresses

    with open(file_path, "r") as file:
        content = file.read()
        ip_addresses = re.findall(ip_pattern, content)

    # Remove duplicates and keep unique IP addresses
    unique_ip_addresses = list(set(ip_addresses))

    return unique_ip_addresses

# Example usage
file_path = "file.txt"  # Replace with the path to your file
unique_ips = grep_ip_addresses(file_path)

output_file = "IPgrepper_out.txt"
with open(output_file, "w") as file:
    file.write("Unique IP Addresses:\n")
    for ip in unique_ips:
        file.write(ip + "\n")

print("Unique IP addresses saved to", output_file)
