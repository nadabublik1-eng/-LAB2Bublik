class NetworkDevice:
    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

    def handle_packet(self, packet):
        return f"{self.name}: пакет отримано"

    def __str__(self):
        return f"{self.name} ({self.ip_address})"


class Router(NetworkDevice):
    def __init__(self, name, ip_address, routes):
        super().__init__(name, ip_address)
        self.routes = routes  # Словник: адреса призначення -> шлюз

    def handle_packet(self, packet):
        destination = packet["dst_ip"]
        gateway = self.routes.get(destination)
        if gateway is None:
            return f"Маршрутизатор {self.name}: маршруту до {destination} немає"
        return f"Маршрутизатор {self.name}: пакет до {destination} через {gateway}"


class Switch(NetworkDevice):
    def __init__(self, name, ip_address, mac_table):
        super().__init__(name, ip_address)
        self.mac_table = mac_table  # Словник: MAC-адреса -> номер порту

    def handle_packet(self, packet):
        mac = packet["dst_mac"]
        port = self.mac_table.get(mac)
        if port is None:
            return f"Комутатор {self.name}: MAC {mac} невідомий, широкомовне розсилання"
        return f"Комутатор {self.name}: кадр на порт {port}"


class Firewall(NetworkDevice):
    def __init__(self, name, ip_address, allowed_ports):
        super().__init__(name, ip_address)
        self.allowed_ports = set(allowed_ports)

    def handle_packet(self, packet):
        port = packet["dst_port"]
        action = "дозволено" if port in self.allowed_ports else "заблоковано"
        return f"Міжмережевий екран {self.name}: порт {port} — {action}"


def demo_task1():
    print("\n=== ЗАВДАННЯ 1: НАСЛІДУВАННЯ ТА ПОЛІМОРФІЗМ ===")
    devices = [
        Router("R1", "192.168.1.1", {"8.8.8.8": "10.0.0.1"}),
        Switch("SW1", "192.168.1.2", {"AA:BB:CC:DD:EE:FF": 5}),
        Firewall("FW1", "192.168.1.3", {80, 443}),
    ]
    packet = {
        "dst_ip": "8.8.8.8",
        "dst_mac": "AA:BB:CC:DD:EE:FF",
        "dst_port": 443,
    }
    for device in devices:
        print(f"{device}: {device.handle_packet(packet)}")
    print("isinstance(devices[0], NetworkDevice):", isinstance(devices[0], NetworkDevice))
    print("issubclass(Firewall, NetworkDevice):", issubclass(Firewall, NetworkDevice))
    assert len({device.handle_packet(packet) for device in devices}) == 3

if __name__ == "__main__":
    demo_task1()
    