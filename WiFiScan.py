import time
import subprocess

def scan_wifi_networks():
    command = ['airodump-ng', 'wlan1', '-w', 'scan', '--output-format', 'csv']
    subprocess.run(command)

def parse_networks():
    networks = []
    with open('scan-01.csv', 'r') as file:
        lines = file.readlines()[2:-1]
        for line in lines:
            data = line.strip().split(',')
            network = {
                'Network Name': data[13].strip(),
                'MAC Address': data[0].strip(),
                'Channel': data[3].strip(),
                'Security': data[5].strip(),
                'Signal Strength': data[8].strip()
            }
            networks.append(network)
    return networks

def save_networks_to_file(networks):
    with open('scan.txt', 'w') as file:
        for network in networks:
            file.write('Network Name: {}\n'.format(network['Network Name']))
            file.write('MAC Address: {}\n'.format(network['MAC Address']))
            file.write('Channel: {}\n'.format(network['Channel']))
            file.write('Security: {}\n'.format(network['Security']))
            file.write('Signal Strength: {}\n'.format(network['Signal Strength']))
            file.write('--------------------\n')

while True:
    scan_wifi_networks()
    networks = parse_networks()
    save_networks_to_file(networks)
    time.sleep(10)