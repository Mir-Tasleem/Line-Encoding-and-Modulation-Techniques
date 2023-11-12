import numpy as np 
import matplotlib.pyplot as plt
from delta import delta_modulated_signal

def nrz_l_encoding(data):
    encoded_data = []

    for bit in data:
        if bit == '1':
            encoded_data.append(1)  # High voltage for '1'
        else:
            encoded_data.append(-1)  # Low voltage for '0'

    return encoded_data

# # Example usage:
# binary_data =input("Enter the data: ")
# nrz_l_data = nrz_l_encoding(binary_data)
print("Binary Data:", list(binary_data))
print("NRZ-L Encoded Data:", nrz_l_data)


def plot(nrz_l_data):
    plt.step(range(len(nrz_l_data)), nrz_l_data, where='post', color='blue', linewidth=4)
    plt.title('NRZ-L Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(0, len(nrz_l_data)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(nrz_l_data)

dm_data=delta_modulated_signal
print(dm_data)
# def dm_data_encoding(dm_data):
#     print(dm_data)
#     print(nrz_l_encoding(dm_data))
#     plot(dm_data)

# dm_data_encoding(dm_data)

