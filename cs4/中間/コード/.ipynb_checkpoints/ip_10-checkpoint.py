def binary_to_decimal_ip(binary_ip):
    # Split the binary IP into 4 segments of 8 bits each
    segments = [binary_ip[i:i+8] for i in range(0, 32, 8)]

    # Convert each segment to decimal
    decimal_segments = [str(int(segment, 2)) for segment in segments]

    # Join the segments with dots to form the decimal IP address
    decimal_ip = '.'.join(decimal_segments)
    return decimal_ip

# Example usage
binary_ip_example = "10001000111100000001000001010100"
decimal_ip = binary_to_decimal_ip(binary_ip_example)
print(decimal_ip)
