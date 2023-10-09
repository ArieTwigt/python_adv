from utils.calculation_functions import calc_circle


if __name__ == '__main__':

    my_diameter = float(input("Insert the diameter:\n"))

    my_size = calc_circle(my_diameter, rounding=5)


    print(my_size)