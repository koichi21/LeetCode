#!/usr/local/bin/python

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # store number of bricks for each column
        d = {}
        for r in wall:
            sum = 0
            for b in r[:-1]:
                sum += b
                if sum not in d:
                    d[sum] = 1
                else:
                    d[sum] += 1

        # 
        if d:
            return len(wall) - max(d.values())
        else:
            return len(wall)

# test
a = [[1,2,2,1],
     [3,1,2],
     [1,3,2],
     [2,4],
     [3,1,2],
     [1,3,1,1]]

sol = Solution()
print sol.leastBricks(a)
