class ValidationError(Exception):
    pass

class ExistException(Exception):
    pass


def setup_():
    while True:
        try:
            input_ = int(input("\n1.Create Parking Lot\n2.Park\n3.Leave\n4.Status\n5.Regi No of Vehicles with Color \
            \n6.Slot No for Cars with Color\nEnter your Choice: "))
            if 0 < input_ <= 6:
                break
            else:
                raise ValueError()
        except ValueError as e:
            print("\nThat is not an Option, Please choose correct option")

    mapper_ = {1: create_parking_lot, 2: park_car, 3: leave_slot,
               4: show_status, 5: show_vehicle_attr, 6: get_slot_detail_on_color}
    mapper_.get(input_)()


def create_parking_lot():
    try:
        parking_slots = int(input("Please enter No to Create No of Slots :"))
        global slot_dict
        slot_dict = {i: None for i in range(1, parking_slots + 1)}
        print("Paking Lot for your System has been Created Successfully..!!")
    except ValueError as e:
        print("Please enter Correct Input")
    finally:
        setup_()


def validate_parking_full():
    try:
        if all(slot_dict.values()):
            raise Exception
    except Exception as e:
        print("Parking Lot is Full")
        raise ExistException


def park_car():
    try:
        validate_parking_full()
        color, car_no = input("Please enter color and Car No: ").split()
        for key, value in slot_dict.items():
            if not value:
                slot_dict.update({key: (color, car_no)})
                break
        print(slot_dict)
    except ValueError as e:
        print("Please Input Correct data eg: White MH12DL4567")
    finally:
        setup_()


def leave_slot():
    print("Leave Car Slot")


def show_status():
    print("Show Status")


def show_vehicle_attr():
    print("Show Vehicle Attribute")


def get_slot_detail_on_color():
    print("Get Slot details")


def validate_slot_created():
    try:
        if not slot_dict:
            raise ValidationError()
    except ValidationError as e:
        print("Please Create Slot First")
        setup_()

setup_()
# park_car()

