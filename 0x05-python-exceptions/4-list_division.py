#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(list_length):
        try:
            n_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            n_list.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            n_list.append(0)
            print("division by 0")
            continue
        except IndexError:
            n_list.append(0)
            print("out of range")
            continue
        finally:
            return (n_list)
