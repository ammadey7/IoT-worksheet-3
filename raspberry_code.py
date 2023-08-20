import serial
import time

def send_command(command):
    """
    Sends a command to the micro:bit and waits for an acknowledgment.
    """
    # Write the command to the micro:bit
    ser.write((command + "\n").encode('utf-8'))
    
    # Wait for an acknowledgment from the micro:bit
    ack = ser.readline().decode('utf-8').strip()
    return ack

# Set up the serial connection
# You might need to change the port depending on where your micro:bit is connected.
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
ser.flush()

while True:
    command = input("Enter command (LED_ON, LED_OFF, SHOW_HEART, SHOW_SAD) or 'exit' to quit: ").strip()
    
    if command.lower() == 'exit':
        break
    elif command in ["LED_ON", "LED_OFF", "SHOW_HEART", "SHOW_SAD"]:
        ack = send_command(command)
        print(f"Received acknowledgment: {ack}")
    else:
        print("Invalid command!")

    # Sleep for a short duration before next command
    time.sleep(0.5)

ser.close()
