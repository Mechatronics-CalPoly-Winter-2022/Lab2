import time
import serial


def main():
    with serial.Serial('COM5', 115201) as ser:
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        kp = input('Enter Kp: ')
        try:
            float(kp)
        except ValueError:
            print('Kp must be a number.')
            return
        ser.write((kp + '\r\n').encode())
        time.sleep(0.1)

        # get rid of the value we just gave it
        ser.readline()

        with open('data.txt', 'w') as f:
            while True:
                line: str = ser.readline().decode()
                if line == 'end.\r\n':
                    break
                elif ',' in line:
                    f.write(line.strip() + '\n')


if __name__ == '__main__':
    main()
