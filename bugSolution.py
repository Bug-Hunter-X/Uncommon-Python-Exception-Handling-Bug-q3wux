def function_with_improved_error_handling(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError as e:
        return f"Error: Type error occurred: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage:
print(function_with_improved_error_handling(10, 2))  # Output: 5.0
print(function_with_improved_error_handling(10, 0))  # Output: Error: Division by zero
print(function_with_improved_error_handling(10, "hello")) # Output: Error: Type error occurred: unsupported operand type(s) for /: 'int' and 'str'
print(function_with_improved_error_handling(10, [1,2])) # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'list' 