import torch
from model import model

X = torch.tensor(
    [
        [
            -1,
            -1,
            1, # delayed
            -1,
        ]
    ]
)

X_masked = torch.masked.MaskedTensor(X, mask=(X != -1))

states = (
    ("rain", ["none", "light", "heavy"]),
    ("maintenance", ["yes", "no"]),
    ("train", ["on time", "delayed"]),
    ("appointment", ["attend", "miss"]),
)

# Calculate predictions from observation that train is delayed
predictions1 = model.predict_proba(X_masked)

# Print predictions for other variables
print("\nGiven that the train is delayed, we can infer:")
for (node_name, values), prediction in zip(states, predictions1):
    if isinstance(prediction, str):
        print(f"{node_name}: {prediction}")
    else:
        print(f"{node_name}")
        for value, probability in zip(values, prediction[0]):
            print(f"    {value}: {probability:.4f}")

Y = torch.tensor(
    [
        [
            2, # heavy, 1 = light
            -1,
            1, # delayed
            -1,
        ]
    ]
)

Y_masked = torch.masked.MaskedTensor(Y, mask=(Y != -1))

# Calculate predictions from observation that train is delayed and heavy rain
predictions2 = model.predict_proba(Y_masked)

# Print predictions for other variables
print("\nGiven that the train is delayed and heavy rain was observed, we can infer:")
for (node_name, values), prediction in zip(states, predictions2):
    if isinstance(prediction, str):
        print(f"{node_name}: {prediction}")
    else:
        print(f"{node_name}")
        for value, probability in zip(values, prediction[0]):
            print(f"    {value}: {probability:.4f}")
