import random
import pandas as pd

# Define the number of rows you want in your dataset (n)
n = 1000  # Change this to your desired number of rows

# Define the min and max values for each feature
f1_min = 0
f1_max = 10
f2_min = 0
f2_max = 5
f3_min = -1
f3_max = 1
f4_min = -5
f4_max = 5

# Define the weights for each feature
w1 = 0.5
w2 = 0.3
w3 = -0.2
w4 = 0.1

# Define the threshold for assigning classes
threshold = 2.0

# Initialize lists to store the data
data = {'f1': [], 'f2': [], 'f3': [], 'f4': [], 'outcome': [], 'class': []}

# Generate n rows of data
for _ in range(n):
    # Generate random values for each feature within their respective min and max ranges
    f1 = int(random.uniform(f1_min, f1_max))
    f2 = int(random.uniform(f2_min, f2_max))
    f3 = int(random.uniform(f3_min, f3_max))
    f4 = int(random.uniform(f4_min, f4_max))

    # Calculate the outcome based on the weights
    outcome = f1 * w1 + f2 * w2 + f3 * w3 + f4 * w4

    # Assign a class based on the outcome and threshold
    if outcome >= threshold:
        class_label = 1
    else:
        class_label = 0

    # Append the data to the lists
    data['f1'].append(f1)
    data['f2'].append(f2)
    data['f3'].append(f3)
    data['f4'].append(f4)
    data['outcome'].append(outcome)
    data['class'].append(class_label)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('synthetic_dataset.csv', index=False)