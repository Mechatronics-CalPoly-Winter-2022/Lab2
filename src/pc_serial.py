import serial


def main():
    with serial.Serial('COM4', 115200) as ser:
        kp = input('Enter Kp: ')
        try:
            float(kp)
        except ValueError:
            print('Kp must be a number.')
            return
        ser.write(kp.encode())


if __name__ == '__main__':
    main()
