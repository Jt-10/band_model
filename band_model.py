import random

ensemble = {}

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
            for i in range(len(self.sounds)):
                print(self.sounds[i], end=", ")


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
        super().__init__(["Thump", "Cymbal", "Wham"])
        
    def count(self):
        print("One, two, three, four!")
        
    def combust(self):
        print("Spontaneously combust!")
        

class Band(Musician):
    def __init__(self):
        super().__init__(["Twang", "Thrumb", "Bling","Boink", "Bow", "Boom", 
        "Thump", "Cymbal", "Wham"])
    
    def hire_musicians(self):
        for player in musicians.keys():
            hired_musician = random.choice(musicians[player])        
            ensemble[player] = hired_musician
        return ensemble

    def fire_musicians(self):
        ensemble.clear()
        return ensemble
            
    def perform(self):
        if "Drummer" in ensemble:
            ensemble["Drummer"] = Drummer()
            ensemble["Bassist"] = Bassist()
            ensemble["Guitarist"] = Guitarist()
            ensemble["Drummer"].count()
            Band.solo(self,3)
        else:
            print("How do you expect to practice when you fired the drummer?")


TheEgrets = Band()
TheEgrets.hire_musicians()
print(ensemble)
TheEgrets.perform()