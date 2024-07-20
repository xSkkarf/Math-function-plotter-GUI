import re


replacement = {
    "sqrt": "np.sqrt",
    "^": "**",
    "log10": "np.log10",
    "log": "np.log",
    "exp": "np.exp"
}

def regexMapper(self, plotFunction):

    pattern = re.compile('|'.join(re.escape(key) for key in replacement.keys()))

    def replace(match):
        return replacement[match.group(0)]
    
    return pattern.sub(replace, plotFunction)