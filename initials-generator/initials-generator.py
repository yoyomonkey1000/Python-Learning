# initials generator


def initials_generator(firstname, middlename, lastname):
    initials= (firstname[0] + middlename[0] + lastname[0])
    return initials


def main():
    firstname = "
    middlename = "ali"
    lastname = "arshad"

    print(initials_generator(firstname, middlename, lastname))


if __name__ == '__main__': # put this in all programs 
    main()