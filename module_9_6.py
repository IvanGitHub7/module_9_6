def all_variants(text):
    for i in range(len(text)):
        a = text[i]
        yield a
    
    for j in range(len(text) - 1):
        b = text[j] + text[j+1]
        yield b
        
    for g in range(len(text) - 2):
        b = text[g] + text[g+1] + text[g+2]
        yield b
        
a = all_variants("abc")
for i in a:
    print(i)