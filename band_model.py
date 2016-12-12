import random

musicians = {
    "Bassist": ["John", "Paul", "Ringo", "Axel", "Spike", "Dave"],
    "Guitarist": ["John", "Paul", "Ringo", "Axel", "Spike", "Dave"],
    "Drummer": ["John", "Paul", "Ringo", "Axel", "Spike", "Dave"]
    }


class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds
        
    def solo(self, length):
        for i in range(length):
            print(self.sounds[{i}.format(len(self.sounds), end=" ")]


class Bassist(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling"])


class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink", "Bow", "Boom"])
        
    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bump", "Cymbal", "Boom"])
        
    def count(self):
        print("One, two, three, four!")
        
    def combust(self):
        print("Spontaneously combust!")
        

class Band(Musician):
    ensemble = {}
    def __init__(self):
        super().__init__(["The band music plays here."])
    
    def hire_musicians(self):
        for instrumen_player in musicians.keys():
            hired_musician = random.choice(musicians[instrumen_player])        
            ensemble[instrument_player] = hired_musician
        return ensemble

    def fire_musicians(self):
        ensemble = {}
        return ensemble
            
    def perform(self):
        if "Drummer" in ensemble:
            ensemble["Drummer"].count()
            Band.solo(6)
        else:
            print("How do you expect to practice when you didn't hire a\
            drummer?")


Stones = Band()
Stones.hire_musicians()
Stones.perform()