import serial
import time


def main():
    with serial.Serial('COM4', 115200) as ser:
        kp = input('Enter Kp: ')
        try:
            float(kp)
        except ValueError:
            print('Kp must be a number.')
            return
        ser.write(kp.encode())

        # wait for the response to finish
        time.sleep(15)


if __name__ == '__main__':
    main()