a, b = (int(x) for x in input().split())



def calc_area(a, b):
    return a*b

def calc_lap_length(a, b):
    return a*2 + b*2

print(calc_area(a, b), calc_lap_length(a, b))

