ID = 0
class one:
    def __init__(self, a):
        global ID
        self.a = a
        self.ID = ID
        ID += 1

class two:
    def __init__(self, a):
        global ID
        self.a = a
        self.ID = ID
        ID += 1

a = one(1)
b = one(2)
c = one(3)
d = two(1)
e = two(2)
f = two(3)
print(f'''{a.a} {type(a)} {a.ID}
{b.a} {type(b)} {b.ID}
{c.a} {type(c)} {c.ID}
{d.a} {type(d)} {d.ID}
{e.a} {type(e)} {e.ID}
{f.a} {type(f)} {f.ID}''')