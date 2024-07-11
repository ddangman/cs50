import numpy
import torch
from model import model


rain_values = ["none", "light", "heavy"]
maintenance_values = ["yes", "no"]
train_values = ["on time", "delayed"]
appoinment_values = ["attend", "miss"]


probability1 = model.probability(
    torch.as_tensor(
        [
            [
                rain_values.index("none"),
                maintenance_values.index("no"),
                train_values.index("on time"),
                appoinment_values.index("attend"),
            ]
        ]
    )
)
print(f"Probability of attending the appointment given no rain, no maintenance, and train on time: {probability1.item():.4f}")

probability2 = model.probability(
    torch.as_tensor(
        [
            [
                rain_values.index("none"),
                maintenance_values.index("no"),
                train_values.index("on time"),
                appoinment_values.index("miss"),
            ]
        ]
    )
)
print(f"Probability of missing the appointment given no rain, no maintenance, and train on time: {probability2.item():.4f}")