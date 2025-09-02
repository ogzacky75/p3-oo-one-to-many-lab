class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string")
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type")
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an Owner instance")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    pass