def function_with_uncommon_error(a, b):
    if a == 0:
        return "Division by zero error"  #Handle the case where a is zero
    return b / a

result = function_with_uncommon_error(0, 10)
print(result)
result2 = function_with_uncommon_error(2,10)
print(result2)