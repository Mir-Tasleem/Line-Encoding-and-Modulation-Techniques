import numpy as np
import matplotlib.pyplot as plt
import os
# import _nrzl

def delta_modulation(input_signal, step_size):
    delta_modulated_signal = np.zeros_like(input_signal, dtype=int)
    delta = 0
    
    plot_output=[0]
    for i in range(1, len(input_signal)):
        delta_signal = input_signal[i] - input_signal[i - 1]
        if delta_signal > delta:
            delta_modulated_signal[i] = 1
            delta += step_size
        else:
            delta_modulated_signal[i] = 0
            delta -= step_size
        plot_output.append(delta)
        # print(plot_output)
    return (delta_modulated_signal,plot_output)


# Generate a sample analog signal (sine wave)
time = np.arange(0, 1, 0.001)
amp=float(input("Enter the value of amplitude:\n"))
freq=float(input("Enter the value of frequency:\n"))
analog_signal = amp * np.sin(2 * np.pi * freq * time)

# Set the step size for delta modulation
step_size = 0.1

# Delta modulation
delta_modulated_signal, plot_output = delta_modulation(analog_signal, step_size)

# Plot the original analog signal and the delta modulated signal
plt.subplot(2, 1, 1)
plt.plot(time, analog_signal)
plt.title('Original Analog Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.step(time, plot_output, where='post')
plt.title('Delta Modulated Signal')
plt.xlabel('Time')
plt.ylabel('Delta Modulation Level (1 or 0)')

plt.tight_layout()
plt.show()

# print(delta_modulated_signal)
# x=_nrzl.nrz_l_encoding(delta_modulated_signal)
# print(x)
