def convert_heights_loop(heights_in_inches):
    heights_in_cm = []
    for height in heights_in_inches:
        heights_in_cm.append(round(height * 2.54, 2))
    return heights_in_cm

def convert_heights_comprehension(heights_in_inches):
    return [round(height * 2.54, 2) for height in heights_in_inches]

def main():

    heights_in_inches = [150, 155, 145, 148]


    heights_in_cm_loop = convert_heights_loop(heights_in_inches)
    print("Heights in cm using loop:", heights_in_cm_loop)


    heights_in_cm_comprehension = convert_heights_comprehension(heights_in_inches)
    print("Heights in cm using list comprehension:", heights_in_cm_comprehension)

if __name__ == "__main__":
    main()
