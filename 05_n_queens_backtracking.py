def solve_n_queen(n):
    col = set()
    positive_diagonal = set()
    negative_diagonal = set()
    
    result = []
    board = [["."] * n for i in range(n)]
    
    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
        
        for c in range(n):
            if c in col or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
                continue
                
            col.add(c)
            positive_diagonal.add(r + c)
            negative_diagonal.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            positive_diagonal.remove(r + c)
            negative_diagonal.remove(r - c)
            board[r][c] = "."
            
    backtrack(0)
    return result
    
def display_solutions(solutions):
    for idx, solution in enumerate(solutions, 1):
        print(f"Solution {idx}:\n")
        for row in solution:
            print(" ".join(row))
        print("\n" + "=" * 2 * len(solution) + "\n")
   
if __name__ == "__main__":
    n = int(input("Enter Square Matrix Value: "))
    
    solutions = solve_n_queen(n)
    
    print(f"\nFound {len(solutions)} solutions for {n}-Queens problem:\n")
    display_solutions(solutions)