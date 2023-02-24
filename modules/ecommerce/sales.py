print("Kicked in.")

def calc_tax():
    print("TAXES CALCED.")


def calc_shipping():
    pass


#This code will ONLY execute if you're running this file directly.
#If this is called elsewhere via an import, it won't run.
if __name__ == "__main__":
    print("Sales started.")
    calc_tax()
