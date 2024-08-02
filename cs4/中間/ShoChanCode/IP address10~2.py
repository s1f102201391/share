def decimal_to_binary_ip(decimal_ip):
    # Split the decimal IP into 4 segments
    segments = decimal_ip.split('.')

    # Convert each segment to 8-bit binary
    binary_segments = [format(int(segment), '08b') for segment in segments]

    # Join the segments with spaces to form the binary IP address
    binary_ip = ' '.join(binary_segments)
    return binary_ip

# Example usage
decimal_ip_example = "88.122.77.49"
binary_ip = decimal_to_binary_ip(decimal_ip_example)
print(binary_ip)
