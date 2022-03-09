from abc import ABC, abstractmethod

class Band:
    """ 
    Band class takes in 2 arguments (band name, members in a list)
    Methods used: 
    play_solos: make the members play in the order they were added
    __repr__: return a string representation
    __str__ : return a string with band name
    to_list : list of previous bands

    """
    instances = []
    members = []


    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)
    

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
       
 
    #if
    def __repr__(self):
        return f'This Band has {self.members}'
    
    def __str__(self):
        return f'I am a {self.name}'

    @classmethod
    def to_list(cls):
        return cls.instances 


class Musician():

    """ 

    Musician a super-class for Guitarist, Bassist, Drummer and takes in 2 arguments (Musician name, instrument)

    Methods used under abstractmethod:

    __repr__: to be defined in the subclasses
    __str__ : to be defined in the subclasses
    get_instrument : to be defined in the subclasses
    play_solo : to be defined in the subclasses
    """



    def __init__(self,name,instrument):
        self.instrument = instrument
        self.name = name


    @abstractmethod    
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass



class Guitarist(Musician):

    """ 

    Guitarist a sub-class and takes in 1 argument (Musician name)
    and 2 attributes

    Methods used under abstractmethod:

    __repr__:  return a string representation
    __str__ : return a string 
    get_instrument : returns string of the instrument used
    play_solo : return a string sound of instrument
    """

    def __init__(self,name):
        self.name = name
        self.instrument = 'guitar'

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__ (self):
        return f'Guitarist instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):
    """ 

    Bassist a sub-class and takes in 1 argument (Musician name)
    and 2 attributes

    Methods used under abstractmethod:

    __repr__:  return a string representation
    __str__ : return a string 
    get_instrument : returns string of the instrument used
    play_solo : return a string sound of instrument
    """
    
    def __init__(self,name):
        self.name = name
        self.instrument = 'bass'
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'

    def __repr__ (self):
        return f'Bassist instance. Name = {self.name}'

    def get_instrument(self):
        return self.instrument

    
    def play_solo(self):
        return 'bom bom buh bom'



class Drummer(Musician):
    """ 

    Drummer a sub-class and takes in 1 argument (Musician name)
    and 2 attributes

    Methods used under abstractmethod:

    __repr__:  return a string representation
    __str__ : return a string 
    get_instrument : returns string of the instrument used
    play_solo : return a string sound of instrument
    """

    def __init__(self,name):
        self.name = name
        self.instrument = 'drums'

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'  

    def __repr__ (self):
        return f'Drummer instance. Name = {self.name}'    


    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        return 'rattle boom crash'



if __name__ == '__main__':

    
   
    the_nobodies = Band("The Nobodies", ['Guitar','Bass'])
    print(Band.members)
    # with str calling print zaid would give i am a but print zaid.name will pring just the name

    player1 = Drummer('AHMAD')

    