import hashlib, json, time

def bhash (timestamp, details, prev_hash):
 token = json.dumps([timestamp, details, prev_hash])
 return hashlib.sha1(token.encode()).hexdigest()

class Blockchain(object):
    def __init__(self, details='new-chain'):
        self.blocks = [(time.time(), details, "")]

    def record(self, details, timestamp = None):
        timestamp = timestamp or time.time()
        prev_hash = self.blocks[-1] [2]
        new_hash = bhash(timestamp, details, prev_hash)
        self.blocks.append((timestamp, details, new_hash))

    def verify(self):
        prev = self.blocks[0]
        for block in self.blocks[1:]:
            new_hash = bhash(block[0], block[1], prev[2])
            if block[2] != new_hash: return False
            prev = block
        return True

bc = Blockchain('A found 10 dollars')
bc.record('A gives 10 dollars to B')
bc.record('B gives 10 dollars to C')
bc.record('C gives 10 dollars to D')

for t, details, h in bc.blocks:
    print(f"------------------------------------")
    print(f"Timestamp: {t}")
    print(f"Details:   {details}")
    print(f"Hash:      {h}")
    print(f"Is the chain valid? {bc.verify()}")
    print(f"------------------------------------")