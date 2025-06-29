import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    if port.device == 'COM5':
        print(f"COM5 found:")
        print(f"  Device: {port.device}")
        print(f"  Description: {port.description}")
        print(f"  HWID: {port.hwid}")
    else:
        print(f"Other port: {port.device} - {port.description}")