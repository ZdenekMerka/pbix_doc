import abc
# formal readers interface  
class writer(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def write_metadata(self):
        pass