def apply_periodic_filter(filter_type):
    if filter_type == "vertical noise":
        return 1
    elif filter_type == "horizontal noise":
        return 2
    elif filter_type == "right diagonal noise":
        return 3
    elif filter_type == "left diagonal noise":
        return 4
    else:
        return 0
