from vyGeneric import vyGenericObjectRepr, vyGeneric
stars80 = '*' * 80
# Testing for non-vyGeneric classes
class NotVyGeneric:
    pass

obj = NotVyGeneric()
obj.l1 = NotVyGeneric()
obj.l1.string1 = 'l1.string1'
obj.l1.obj = NotVyGeneric()
obj.l1.obj.integer1000 = 1000

obj.integer5000 = 5000
obj.integer500000 = 500000
obj.string1_ITTIA = 'I think therefore I am'
obj.string2_Stronger = 'That which doesn\'t kill you, \nmakes you stronger'

obj.l2 = NotVyGeneric()
obj.l2.string1_Hello = 'l2.string1 Hello!!'
obj.l2.string2_World = 'l2.string2 World!!'
obj.l2.string3_Multiline = 'Hello\nWorld!!'
obj.l2.objGenericLongAttributeName = NotVyGeneric()
obj.l2.obj = obj.l2.objGenericLongAttributeName
obj.l2.obj2 = obj.l2.obj
obj.l2.obj.integer10000 = 10000
obj.l2.obj.integer123456 = 123456
obj.l2.obj.integer1234567890 = 1234567890
del obj.l2.obj

print(stars80)
print('Testing for non-vyGeneric classes')
print(stars80)
print('The secret version')
print(obj)
print(stars80)
print('The all-revealing version')
print(vyGenericObjectRepr(obj))
print(stars80)

# Testing for vyGeneric classes
obj = vyGeneric()
obj.l1 = vyGeneric()
obj.l1.string1 = 'l1.string1'
obj.l1.obj = vyGeneric()
obj.l1.obj.integer1000 = 1000

obj.integer5000 = 5000
obj.integer500000 = 500000
obj.string1_ITTIA = 'I think therefore I am'
obj.string2_Stronger = 'That which doesn\'t kill you, \nmakes you stronger'

obj.l2 = vyGeneric()
obj.l2.string1_Hello = 'l2.string1 Hello!!'
obj.l2.string2_World = 'l2.string2 World!!'
obj.l2.string3_Multiline = 'Hello\nWorld!!'
obj.l2.objGenericLongAttributeName = vyGeneric()
obj.l2.obj = obj.l2.objGenericLongAttributeName
obj.l2.obj2 = obj.l2.obj
obj.l2.obj.integer10000 = 10000
obj.l2.obj.integer123456 = 123456
obj.l2.obj.integer1234567890 = 1234567890
del obj.l2.obj

print(stars80)
print('Testing for vyGeneric classes')
print(stars80)
print(obj)
print(stars80)
