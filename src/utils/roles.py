def is_landlord(user):
    if user["is_landlord"]:
        return True
    return False


def is_property_manager(user):
    if user["is_propertymanager"]:
        return True
    else:
        return False


def is_admin(user):
    if user["is_admin"]:
        return True
    else:
        return False

