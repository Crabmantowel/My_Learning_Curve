def zero_fuel(distance_to_pump, mpg, fuel_left):
    return(False if fuel_left * mpg < distance_to_pump else True)
