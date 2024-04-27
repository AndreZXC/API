def get_scale(toponym):
    x = str(abs(float(toponym['boundedBy']['Envelope']['lowerCorner'].split()[0]) -
                float(toponym['boundedBy']['Envelope']['upperCorner'].split()[0])))
    y = str(abs(float(toponym['boundedBy']['Envelope']['lowerCorner'].split()[1]) -
                float(toponym['boundedBy']['Envelope']['upperCorner'].split()[1])))
    return x, y