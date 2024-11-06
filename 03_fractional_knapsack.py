class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight
        
def fractional_knapsack(w, arr):
    arr.sort(key = lambda x: x.profit/x.weight, reverse = True)
    final_value = 0.0
    
    for item in arr:
        if w >= item.weight:
            final_value += item.profit
            w -= item.weight
            
        else:
            final_value += (item.profit / item.weight) * w
            break
        
    return final_value

if __name__ == "__main__":
    n = int(input("Enter number of items-\n"))
    arr = [Item(*map(int, input(f"Enter profit and weight of item {i + 1} (space-seperated): ").split())) for i in range(n)]
    w = int(input("Enter capacity of knapsack-\n"))
    print("Maximum value in knapsack: ", fractional_knapsack(w, arr))