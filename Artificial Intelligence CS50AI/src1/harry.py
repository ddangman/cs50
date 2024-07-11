from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

# based on the given knowledge, can we infer that it is raining?
print(model_check(knowledge, rain)) # True: it is raining
# in every possible world where the knowledge is true, it is raining
# ie. there is no possible world where the knowledge is true and it is not raining
