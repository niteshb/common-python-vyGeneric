"""
from vyGeneric import vyGenericObjectRepr

* vyGenericObjectRepr(object) will return nice printable 'repr' for your objects

* If you inherit your class, say 'MyClass', from vyGeneric, then any object of 
  MyClass, say 'myObject', prints all its hidden info when you call 
  print(myObject)
"""
import types

functions = (types.BuiltinFunctionType, types.BuiltinMethodType, types.FunctionType)


def vyGenericObjectRepr(obj):
    dataAttributes = []
    maxAttributeNameLen = 0
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
        maxAttributeNameLen = max(maxAttributeNameLen, len(attributeName))
    midAttributeNameValueStr = ' :: '
    formatStr = '%' + str(maxAttributeNameLen) + 's' + midAttributeNameValueStr + '%s'
    childIndent = '\n' + ' ' * (maxAttributeNameLen + len(midAttributeNameValueStr))
    returnStr = ''
    for dataAttribute in dataAttributes:
        val = getattr(obj, dataAttribute)
        valStr = str(val)
        # valStr could be multiline because of a multiline value or a vyGeneric descendant
        # '\n' added to returnStr ensures that. That ensures that you indent your descendant objects.
        # if you got a multiline answer for your attribute, each needs to be indented
        valArr = valStr.split('\n')
        if len(valArr) == 1:
            # if valStr is just one line, that's it
            valStr1 = valStr
        else:
            # if valStr is multiline
            while valArr[-1] == '':
                # remove any blank lines at the end. This could have come from another call to vyGenericRepr call, so trimming it
                del valArr[-1]
            valStr1 = childIndent + childIndent.join(valArr)
        returnStr += formatStr % (dataAttribute, valStr1) + '\n'
    return returnStr
