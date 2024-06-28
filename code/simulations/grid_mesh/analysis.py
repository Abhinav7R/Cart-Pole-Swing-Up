import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('analysis.csv', header=None, names=['Number of Points', 'Error', 'Time Taken'])

num_points = data['Number of Points']
error = data['Error']*10
time_taken = data['Time Taken']

plt.figure(figsize=(10, 6))
plt.plot(num_points, error, 'o-', label='10*Error', linewidth=2, markersize=8)
plt.plot(num_points, time_taken, 's--', label='Time Taken', linewidth=2, markersize=8)
plt.xlabel('Number of Points')
plt.ylabel('10*Error / Time Taken (s)')
plt.title('Error and Time Taken vs. Number of Points')
plt.legend()
plt.grid(True)
plt.show()
