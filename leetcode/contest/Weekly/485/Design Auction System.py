import heapq

class AuctionSystem:
    def __init__(self):
        self.d = {}
        self.p = {}

    def addBid(self, u, i, a):
        if i not in self.d:
            self.d[i] = {}
            self.p[i] = []

        if u in self.d[i]:
            self.d[i][u] = a
        else:
            self.d[i][u] = a

            
        heapq.heappush(self.p[i], (-a, -u))

    def updateBid(self, u, i, a):
        if i in self.d:
            if u in self.d[i]:
                self.d[i][u] = a
            else:
                self.d[i][u] = a
            heapq.heappush(self.p[i], (-a, -u))

    def removeBid(self, u, i):
        if i in self.d:
            if u in self.d[i]:
                del self.d[i][u]

    def getHighestBidder(self, i):
        if i not in self.d:
            return -1

        if not self.d[i]:
            return -1

        h = self.p[i]

        while h:
            v = h[0][0]
            k = h[0][1]

            if -k in self.d[i]:
                if self.d[i][-k] == -v:
                    return -k

            heapq.heappop(h)

        return -1



# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)