import matplotlib.pyplot as plt

if __name__ == '__main__':
    with open('data.txt', 'r') as f:
        data = f.readlines()
        x = [float(i.split(',')[0]) for i in data]
        y = [float(i.split(',')[1]) for i in data]

        plt.plot(x, y)
        plt.xlabel('Time (ms)')
        plt.ylabel('Encoder (counts)')
        plt.show()