def fullname(first_name, last_name):
    return first_name + " " + last_name

def string_alternative(full_name):
    return full_name[::2]

def main():
    first_name = "murali"
    last_name = "krishna"

    full_name = fullname(first_name, last_name)
    print("Full name:", full_name)

    alternative_chars = string_alternative(full_name)
    print("Every other character in full name:", alternative_chars)

if __name__ == "__main__":
    main()
