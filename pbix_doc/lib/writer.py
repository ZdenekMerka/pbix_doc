import abc
# formal readers interface  
class reader(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_metadata(self):
        pass