import re


replacement = {
    "sqrt": "np.sqrt",
    "^": "**",
    "log10": "np.log10",
    "log2": "np.log2",
    "log": "np.log",
    "exp": "np.exp",
    "sin": "np.sin",
    "cos": "np.cos",
    "tan": "np.tan",
    "asin": "np.arcsin",
    "acos": "np.arccos",
    "atan": "np.arctan",
    "sinh": "np.sinh",
    "cosh": "np.cosh",
    "tanh": "np.tanh",
    "arcsinh": "np.arcsinh",
    "arccosh": "np.arccosh",
    "pi": "np.pi",
    "j": "p"
}

def regexMapper(plotFunction):

    pattern = re.compile('|'.join(re.escape(key) for key in replacement.keys()))

    def replace(match):
        return replacement[match.group(0)]
    
    return pattern.sub(replace, plotFunction)