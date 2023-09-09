# Mid Level Question

# Problem Statement:
# Write a function that, given an integer n, returns all possible valid combinations of n pairs of parentheses
# A valid combination is one where every open parenthesis has a corresponding close parenthesis and vice versa
# The function should use a recursive approach to generate these combinations
# Provide an explanation of the logic behind your solution and analyze its space and time complexities

# The generateParentheses() function below generates all possible valid combinations of its input n pairs of parentheses using a recursive approach, explanation with space and time complexity below

def generateParentheses(n):
    def backtrack(current_combination, open_parentheses, close_parentheses):
        if len(current_combination) == 2 * n:
            ans.append(current_combination)
            return
        if open_parentheses < n:
            backtrack(current_combination +
                      '(', open_parentheses+1, close_parentheses)
        if close_parentheses < open_parentheses:
            backtrack(current_combination+')',
                      open_parentheses, close_parentheses+1)

    ans = []
    backtrack('', 0, 0)
    return ans


n = 3
print(generateParentheses(n))
# Expected Output: ["((()))","(()())","(())()","()(())","()()()"]

# Explanation:
# If the length of current_combination is equal to 2*n, we have a valid combination, so we append current_combination to the list of answers and return
# backtrack() is a recursive function that takes the current combination of parentheses current_combination, the count of open parentheses (open_parentheses), and the count of close parentheses (close_parentheses)
# If open_parentheses is less than n, we can add an open parenthesis and recursively call backtrack() with open_parentheses+1
# If close_parentheses is less than open_parentheses, we can add a close parenthesis and recursively call backtrack with close_parentheses+1

# Space Complexity: O(2^n/n^0.5) or O(2^n/n^(1/2))
# The space complexity of the generateParentheses() function is O(2^n/n^0.5) or O(2^n/n^(1/2)) as it generates all combinations of well-formed parentheses for the given n

# Time Complexity: O(2^n/n^0.5) or O(2^n/n^(1/2))
# The time complexity of the generateParentheses() function is O(2^n/n^0.5) or O(2^n/n^(1/2)) as it generates all combinations of well-formed parentheses for the given n
