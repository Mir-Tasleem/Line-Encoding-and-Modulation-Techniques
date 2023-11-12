import matplotlib.pyplot as plt
import numpy as np

def nrz_i_encoding(bits):
    encoded_bits = []
    current_level = 1  # Start with a high level

    for bit in bits:
        if bit=='1':
            current_level = -current_level  # Invert the level for a binary 1
        print(current_level)
        encoded_bits.append(current_level)
    return encoded_bits

binary_data =input("Enter the data: ")
nrz_i_data = nrz_i_encoding(binary_data)
print("Binary Data:", list(binary_data))
print("NRZ-I Encoded Data:", nrz_i_data)

def plot(nrz_i_data):
    plt.step(range(len(nrz_i_data)), nrz_i_data, where='post', color='blue', linewidth=4)
    plt.title('NRZ-I Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(nrz_i_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(nrz_i_data)