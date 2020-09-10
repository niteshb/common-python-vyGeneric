"""
import importlib
import vyGenericObjectRepr
importlib.reload(vyGenericObjectRepr)
"""
import types
functions = (types.BuiltinFunctionType, types.BuiltinMethodType, types.FunctionType)

def vyGenericObjectRepr(obj):
    dataAttributes = []
    maxLen = 0
    for attributeName in dir(obj):
        # get rid of builtin names: __str__, __repr__,... 
        if attributeName.startswith("__"):
            continue
        # get rid of functions ??
        if isinstance(getattr(obj, attributeName), functions):
            continue
        # get rid of methods
        if callable(getattr(obj, attributeName)):
            continue
        dataAttributes.append(attributeName)
        maxLen = max(maxLen, len(attributeName))
    formatStr = '%' + str(maxLen + 5) + 's :: %s'
    retString = ''
    for attr in dataAttributes:
        valStr = str(getattr(obj, attr))
        valArr = valStr.split('\n')
        l = len(valArr)
        if l == 1:
            valStr1 = valStr
        else:
            while valArr[-1] == '':
                del(valArr[-1])
            for vali in valArr:
                valStr1 += '\n' + ' ' * maxLen + vali
        retString += formatStr % (attr, valStr1) + '\n'
    return retString


