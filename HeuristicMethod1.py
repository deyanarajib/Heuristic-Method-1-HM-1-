import numpy as np
from Setup import Transportation

class HeuristicMethod1:

    def __init__(self, trans):

        self.trans = trans
        self.table = trans.table.copy()
        self.alloc = []

    def allocation(self, x, y):
        
        mins = min([self.table[x, -1], self.table[-1, y]])
        self.alloc.append([self.table[x, 0], self.table[0, y], mins])
        
        if self.table[x, -1] < self.table[-1, y]:
            #delete row and supply x then change value of demand y
            self.table = np.delete(self.table, x, 0)
            self.table[-1, y] -= mins
            
        elif self.table[x, -1] > self.table[-1, y]:
            #delete column and demand y then change value of supply x
            self.table = np.delete(self.table, y, 1)
            self.table[x, -1] -= mins
            
        else:
            #delete row and supply x, column and demand y
            self.table = np.delete(self.table, x, 0)
            self.table = np.delete(self.table, y, 1)

    def penalty(self, cost):
        gaps = np.zeros(cost.shape[0])
        for i, c in enumerate(cost):
            try:
                x, y = sorted(c)[:2]
                v = abs(x - y)
            except ValueError:
                v = c[0]
            gaps[i] = v
        return gaps
    
    def solve(self, show_iter=False):

        while self.table.shape != (2, 2):

            if show_iter:
                self.trans.print_frame(self.table)

            cost = self.table[1:-1, 1:-1]

            row_P = self.penalty(cost)
            col_P = self.penalty(cost.T)

            row_PT = [p * t for p, t in zip(row_P, cost.sum(1))]
            col_PT = [p * t for p, t in zip(col_P, cost.sum(0))]

            while True:
                if min(row_PT) < min(col_PT):
                    x = np.argmin(row_PT)
                    y = np.argmin(cost[x])
                    if min(cost[x]) == min(cost[:, y]):
                        break
                    else:
                        row_PT[x] = np.inf
                else:
                    y = np.argmin(col_PT)
                    x = np.argmin(cost[:, y])
                    if min(cost[x]) == min(cost[:, y]):
                        break
                    else:
                        col_PT[y] = np.inf

            self.allocation(x + 1, y + 1)
            
        return np.array(self.alloc, dtype=object)


if __name__ == "__main__":

    #example 1 balance problem
    cost = np.array([[19, 30, 50, 10],
                     [70, 30, 40, 60],
                     [40,  8, 70, 20]])
    supply = np.array([7, 9, 18])
    demand = np.array([5, 8, 7, 14])

    #example 2 unbalance problem
    cost = np.array([[ 4,  8,  8],
                     [16, 24, 16],
                     [ 8, 16, 24]])
    supply = np.array([76, 82, 77])
    demand = np.array([72, 102, 41])

    #initialize transportation problem
    trans = Transportation(cost, supply, demand)

    #setup transportation table.
    #minimize=True for minimization problem, change to False for maximization, default=True.
    #ignore this if problem is minimization and already balance
    trans.setup_table(minimize=True)

    #initialize HM1 with table that has been prepared before.
    HM1 = HeuristicMethod1(trans)

    #solve problem and return allocation lists which consist n of (Ri, Cj, v)
    #Ri and Cj is table index where cost is allocated and v it's allocated value.
    #(R0, C1, 3) means 3 cost is allocated at Row 0 and Column 1.
    #show_iter=True will showing table changes per iteration, default=False.
    allocation = HM1.solve(show_iter=True)

    #print out allocation table in the form of pandas DataFrame.
    #(doesn't work well if problem has large dimension).
    trans.print_table(allocation)

#Result from example problem above
'''
example 1 balance problem
           C0    C1     C2     C3 Supply
R0         19    30     50  10(7)      7
R1      70(2)    30  40(7)     60      9
R2      40(3)  8(8)     70  20(7)     18
Demand      5     8      7     14     34

TOTAL COST: 814

example 2 unbalance problem
           C0      C1      C2  Dummy Supply
R0      4(56)       8       8  0(20)     76
R1         16  24(41)  16(41)      0     82
R2      8(16)  16(61)      24      0     77
Demand     72     102      41     20    235

TOTAL COST: 2968
'''
