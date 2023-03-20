import abc
# formal writers interface
class writer(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def write_metadata(self):
        pass
