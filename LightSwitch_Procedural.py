def turnOn():
    global switchIsOn
    # turn the light on
    switchIsOn = True

def turnOff():
    global switchIsOn
    # turn the light off
    switchIsOn = False

# Main code
switchIsOn = False

# Test code
print(switchIsOn)
turnOn()
print(switchIsOn)
turnOff()
print(switchIsOn)
turnOn()
print(switchIsOn)