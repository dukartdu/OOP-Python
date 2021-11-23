# When to use class methods and when to use static methods?

class Item:
    @staticmethod
    def is_integer(num):
        '''
        This should do something that has a relationship with the class,
         but not something that muys be unique per instance
        '''
    

    @classmethod
    def instantiate_from_something(cls):
        '''
        this should  also do something that has a relationship
        with the class, but usually, thosae are used to manupulate different
        structures of data to instantiate object, like we have done with CSV
        '''

# However, those could be also called from instances.

item1 = Item()
item1.is_integer(5)
item1.instantiate_from_something()
