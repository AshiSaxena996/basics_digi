def hypo(perp, base):
    # height_2= (perp**2) + (base**2)
    # return(height_2**0.5)

    from math import sqrt
    return sqrt((perp**2) + (base**2))

val1= int(input('enter perpendicular: '))
val2= int(input('enter base: '))
print(hypo(val1, val2))
