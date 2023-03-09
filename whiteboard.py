# Create a function that given a list which represents street lights given as a parameter(l_street),
# determine if an outage has occurred.
# A street light is represented as a “T” or “F”.

# A street with a total number of “F” greater than or equal to
# 2 returns “Outage”, anything below returns “Power”

# Example Input
["T", "F", "F", "F"]
#
# Example Output:
# “Outage”

def lights(list):
    F=list.count("F")

    if F >= 2:
        return "Outage"
    else:
        return "Power"
    
lights([0, 0, 0, 0,])
        