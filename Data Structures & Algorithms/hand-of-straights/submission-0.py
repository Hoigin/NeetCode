class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        store = defaultdict(int)
        for num in hand:
            store[num] += 1
        for i in range(n // groupSize):
            min_key = min(store)
            for j in range(groupSize):
                store[min_key+j] -= 1
                if store[min_key+j] == 0:
                    del store[min_key+j]
                elif store[min_key+j] < 0:
                    return False
        return True