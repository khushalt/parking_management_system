slot_dict, parking_slots = {}, None


class ValidationError(Exception):
    pass


class ExistException(Exception):
    pass


def setup_():
    while True:
        try:
            input_ = int(input("\n1.Create Parking Lot\n2.Park\n3.Leave\n4.Status\n5.Slot no on regi No of Vehicle\
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
        global slot_dict, parking_slots
        parking_slots = int(input("Please enter No to Create No of Slots :"))
        slot_dict.update({i: None for i in range(1, parking_slots + 1)})
        print(slot_dict)
        print("Paking Lot for your System has been Created Successfully..!!")
    except ValueError as e:
        print("Please enter Correct Input")
    finally:
        setup_()


def validate_parking_full():
    try:
        if slot_dict and all(slot_dict.values()):
            raise Exception
    except Exception as e:
        print("Parking Lot is Full")
        raise ExistException


def park_car():
    try:
        validate_slot_created()
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
    try:
        validate_slot_created()
        free_lot = int(input("Please Enter Lot to be emptied: "))
        if not 0 < free_lot <= parking_slots:
            raise ValueError
        # not checking if slot is already emptied since both operation will cost
        slot_dict.update({free_lot: None})
        print("Lot no %s got empty successfully" % free_lot)
        print(slot_dict)
    except Exception as e:
        print("Please enter Correct Input")
    finally:
        setup_()


def show_status():
    try:
        validate_slot_created()
        for i,v in slot_dict.items():
            print("Parking Slot %s  %s %s" %(i, v[0] if v else "Empty", v[1] if v else "Lot"))
    except Exception as e:
        print("Something Went wrong")
    finally:
        setup_()


def show_vehicle_attr():
    try:
        validate_slot_created()
        vehicle_no = str(input("Please Specify No to get Slot No: "))
        for i,v in slot_dict.items():
            if v and vehicle_no in v:
                print("Slot for %s is %s" %(vehicle_no, i))
                break
        else: print("No Does not exist in system")
    except Exception as e:
        print("Please Input correct data")
    finally:
        setup_()


def get_slot_detail_on_color():
    try:
        validate_slot_created()
        color = str(input("Please Specify color to get slot no: "))
        req_slot = ''
        try:
            for i,v in slot_dict.items():
                if v and color in v:
                    req_slot += str(i) + ","
            print("Slots for Color %s %s" %(color, req_slot if req_slot else "Does Not Exist") )
        except Exception as e:
            print("Some Exception", e)
    except ValueError as e:
        print("Please give Correct Input")
    finally:
        setup_()


def validate_slot_created():
    try:
        print(slot_dict)
        if not slot_dict:
            raise ValidationError()
    except ValidationError as e:
        print("\nPlease Create Slot First")
        setup_()


setup_()

