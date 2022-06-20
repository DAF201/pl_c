import socket
import func_timeout

port = 1081
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(('', port))


@func_timeout.func_set_timeout(5)
def fetch_server_ip():
    data, ip_address = client.recvfrom(65535)
    return ip_address[0]
