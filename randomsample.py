import numpy as np


# target
os_list = ['Windows', 'Linux', 'Darwin']

"""
    p 매개변수에 모두 합이 1이 되어야 하고, 각 확률을 지정해줄 수 있다. 
"""
sample_result = np.random.choice(os_list, 3, p=[0.1,0.4,0.5])
print(sample_result)

