import socket

def get_network_interfaces():
    interfaces = []
    for interface in socket.if_nameindex():
        interface_name = interface[1]
        interfaces.append(interface_name)
    return interfaces

network_interfaces = get_network_interfaces()
print(network_interfaces)