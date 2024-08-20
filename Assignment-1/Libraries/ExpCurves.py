def expCurve(expType):
    '''Defines experience curves for all pokemons. Returns a list of experience points required to reach a certain level for a given experience curve type.
    
    All valid from generation 3 onwards. Does not take into account gen 5+ experience bonus from level difference.
    '''
    expCurve = {
        'erratic': [0],
        'fast': [0],
        'medium': [0],
        'medium slow': [0],
        'slow': [0],
        'fluctuating': [0]
    }

    for i in range(2, 101):
        expCurve['fast'].append(int(4*pow(i,3)/5))
        expCurve['medium'].append(int(pow(i,3)))
        expCurve['medium slow'].append(int(6*pow(i,3)/5 - 15*pow(i,2) + 100*i-140))
        expCurve['slow'].append(int(5*pow(i,3)/4))
        if i < 50:
            expCurve['erratic'].append(int(pow(i,3)*(100-i)/50))
        elif i in range(50, 68):
            expCurve['erratic'].append(int(pow(i,3)*(100-i)/100))
        elif i in range(68, 98):
            expCurve['erratic'].append(int(pow(i,3)*(1911-10*i)/1500))
        else:
            expCurve['erratic'].append(int(pow(i,3)*(160-i)/100))
        
        if i < 15:
            expCurve['fluctuating'].append(int(pow(i,3) * ((i + 1) / 3 + 32) / 50))
        elif i in range(15, 36):
            expCurve['fluctuating'].append(int(pow(i,3) * (i + 14) / 50))
        else:
            expCurve['fluctuating'].append(int(pow(i,3) * (i / 2 + 32) / 50))

    return expCurve[expType]

