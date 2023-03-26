import abc
# formal writers interface
class reader(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def read_metadata(self):
        pass
