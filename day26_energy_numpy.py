import numpy as np
energy=np.array([450,520,610,480,550])
print("Original energy array:", energy)
print("average energy:", np.mean(energy))
print("maximum energy:", np.max(energy))
print("minimum energy:", np.min(energy))
print("hypothethical 10% increase in energy:", energy * 1.10)