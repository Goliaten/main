def count(base):
    orig = []                          #original items
    orig_count = []       #count of items in A A A
    out = ''            #output
    
    for x in base:
        if x in orig:
            index = orig.index(x)
            orig_count[index] += 1
        else:
            orig.append(x)
            orig_count.append(1)
    
    for x, y in zip(orig, orig_count):
        out += f'{x}'
        
        if y != 1:
            out += f'*{y} '
        else:
            out += ' '
    
    return out

if __name__ == '__main__':
    print('main')
    a = count(['a','a','b','c','a','c','g','t','b'])
    print(a)
    
    