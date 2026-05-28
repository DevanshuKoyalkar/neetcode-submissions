class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        # target is a, b, c
        # points are (x,y,z)

        # first set is x = a
        # second set is x <=a, y = b
        # third set is x <=a, y<=b, z = c

        a, b, c = target
        found1, found2, found3 = False, False, False

        for triplet in triplets:
            x, y, z = triplet

            if x == a and y <= b and z <= c:
                found1 = True
            
            if x <= a and y == b and z <=c:
                found2 = True
            
            if x <= a and y <= b and z == c:
                found3 = True
        
        return found1 and found2 and found3