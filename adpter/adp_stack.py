
class Stack:
    def __init__(self,container):
        if isinstance(container,list,maxsize=None):
            self._basecontiner = container
            self.maxsize = None
        else:
            raise TypeError("Stack need a list datatype")

    def appen(self,elem):
        if self.maxsize is not None:
        self._basecontiner.append(elem)

