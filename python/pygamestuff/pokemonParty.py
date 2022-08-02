



class Party():
    def __init__(self):
        # these aren't working but the list does ???
        self.slot_one = None
        self.slot_two = None
        self.slot_three = None
        self.slot_four = None
        self.slot_five = None
        self.slot_six = None

        self.party_list = [self.slot_one, self.slot_two, self.slot_three, self.slot_four, self.slot_five, self.slot_six]
    
    def add_to_party(self, pokemon):
        for i, slot in enumerate(self.party_list):
            if slot == None:
                self.party_list[i] = pokemon
                pokemon.party_slot = i + 1
                break

    def switch_pokemon(self, from_pokemon , to_pokemon):
        x = from_pokemon.party_slot
        y = to_pokemon.party_slot
        from_pokemon.party_slot = y
        to_pokemon.party_slot = x