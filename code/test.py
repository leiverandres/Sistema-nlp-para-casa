import re

st = raw_input()

# Referencias: http://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/
# Podemos utilizar la sintaxis especial (?P<nombre>patron) 
# que nos ofrece Python para nombrar estos grupos y que sea mas facil identificarlos.


# (.*) => ((\w*)( )*)*
m = re.compile(r"((\w*)( )*)*(?P<numero1>[0-9]+)( min(utos)?) (?P<numero2>[0-9]+)")
# Formas de usarse:
#s = m.search(st)
s = m.match(st)
minutos1 = (s.group("numero1")) # es de tipo str pero se puede castear a entero
minutos2 = (s.group("numero2"))
print minutos1, minutos2