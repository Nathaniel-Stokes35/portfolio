

def wind_chill(temp, wind):
    if wind < 3 or temp > 50:
        return round(temp, 1)
    chill = 35.74 \
        + 0.6215 * temp \
        - 35.75 * wind**0.16 \
        + 0.4275 * temp * wind**0.16
    rounded = round(chill, 1)
    return rounded

def heat_index(temp, hum):
    index = -42.379 \
        + 2.04901523 * temp \
        + 10.14333127 * hum \
        -0.22475541 * temp * hum \
        - 0.00683783 * temp**2 \
        - 0.05481717 * hum**2 \
        + 0.00122874 * temp**2 * hum \
        +0.00085282 * temp * hum**2 \
        - 0.00000199 * temp**2 * hum**2
    rounded = round (index, 1)
    return rounded