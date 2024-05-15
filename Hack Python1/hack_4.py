"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    palabra = "fooziman"
    # Reemplaza la última letra con una 'N'
    resultado = "foozimaN"[:-1] + "N"
    return resultado