class Stack:
    def __init__(self,container):
        if isinstance(container,list,maxsize=None):
            self._basecontiner = container
            self.maxsize = None
        else:
            raise TypeError("Stack need a list datatype")

    def append(self, elem):
        if self.maxsize is None:
            self._basecontiner.append(elem)
        elif len(self._basecontiner) < self.maxsize:
            self._basecontiner.append(elem)

    def top(self):
        if len(self._basecontiner) > 0:
            return self._basecontiner[-1]
        else:
            raise Exception("stack is empty")

    def isempty(self):
        return len(self._basecontiner)

    def pop(self):
        if len(self._basecontiner) > 0:
            self._basecontiner.pop(-1)
        else:
            raise Exception("stack is empty")



