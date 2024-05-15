"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    original_list = [1, 3, 5, 7, 9]
    result = original_list[1:4]  # Obtiene los elementos desde el índice 1 hasta el 3 (excluyendo el 4)
    return result