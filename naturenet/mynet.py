class Node:
    def __init__(self, x,y,p=None):
        """
        node的初始化
        :param data: 节点的数据
        """
        self.x =x
        self.y=y
        self.pnext = None
    def add(self,tail):
        p=self
        while p.pnext!=None:
            p=p.pnext
        p.pnext=tail
    def getLength(self):
        p = self
        count=0
        while p.pnext != None:
            count+=1
            p = p.pnext
        return count
    def __repr__(self):
        return str(self.data)


