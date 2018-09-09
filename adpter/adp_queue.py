class Queue:
    def __init__(self,container,maxsize = None):
        if isinstance(container,list):
            self._basecontainer = container
            self.maxsize = maxsize
        else:
            raise TypeError("Queue needs list type ")

    def append(self,elem):
        if self.maxsize is None:
            self._basecontainer.append(elem)
        elif len(self._basecontainer) < self.maxsize:
            self._basecontainer.append(elem)
        else:
            raise Exception("Queue max limit %s" % self.maxsize)

    def isempty(self):
        return len(self._basecontainer)

    def popfront(self):
        if len(self._basecontainer) > 0:
            res = self._basecontainer[0]
            self._basecontainer.pop(0)
            return res
        else:
            raise Exception("Queue is empty")

