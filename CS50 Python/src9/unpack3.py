# Unpacks enumerations where order is preserved
# will not work with sets
# will work in dictionaries which perserves order
#     unpacks5.py & unpacks6.py has proper syntax for dictionaries


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

# unpack *coins
print(total(*coins), "Knuts")
