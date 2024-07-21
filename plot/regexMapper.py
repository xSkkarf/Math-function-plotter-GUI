import re

# Map of the supported operations in the plot function input field
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
    """
    This function takes a string representing a mathematical function and replaces certain 
    operations with their numpy equivalents. The replacements are based on a predefined map.

    Parameters:
    plotFunction (str): A string representing a mathematical function. The supported operations
                        are listed in the 'replacement' map.

    Returns:
    str: The input string with the operations replaced by their numpy equivalents.
    """

    # The function re.compile() builds the pattern to be matched. Example output:
    # 'sqrt|\\^|log10|log2|log|exp|sin|cos|tan|asin|acos|atan|sinh|cosh|tanh|arcsinh|arccosh|pi|j'

    pattern = re.compile('|'.join(re.escape(key) for key in replacement.keys()))
    # print(pattern)

    # This function is called everytime a match is found in the original text
    # It simply replaces the match with the corrisponding value in the replacement map
    def replace(match):
        return replacement[match.group(0)]  # group(0) returns the whole match
    
    # This line uses the re.sub() function to substitute all matches of the pattern in the plotFunction string
    # The replace function is called for each match, replacing the match with the corresponding value from the replacement map
    return pattern.sub(replace, plotFunction)