x = 0
y = 0
z = 0

with open('1.txt', encoding='utf-8') as f:
    lines = f.readlines()
    x = (len(lines))
with open('2.txt', encoding='utf-8') as f:
    lines = f.readlines()
    y = (len(lines))
with open('3.txt', encoding='utf-8') as f:
    lines = f.readlines()
    z = (len(lines))

values = [x, y, z]
max_value = max(values)
min_value = min(values)

if min_value == x and max_value == y:
    
    with open('1.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("1.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(x) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")
        
    with open('3.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("3.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(z) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")

    with open('2.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("2.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(y) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text)

elif min_value == y and max_value == x:

    with open('2.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("2.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(y) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")
        
    with open('3.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("1.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(z) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")

    with open('2.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("3.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(x) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text)

elif min_value == x and max_value == z:

    with open('1.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("1.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(x) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")
        
    with open('2.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("2.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(y) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")

    with open('3.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("3.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(z) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text)

elif min_value == z and max_value == x:

    with open('3.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("3.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(z) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")
        
    with open('2.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("2.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(y) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")

    with open('1.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("1.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(x) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text)

elif min_value == y and max_value == z:

    with open('2.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'w', encoding='utf-8') as output_file:
        output_file.write("2.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(y) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")
        
    with open('1.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("1.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(x) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text + "\n")

    with open('3.txt', 'r', encoding='utf-8') as input_file:
        text = input_file.read()
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write("3.txt\n") 
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(str(z) + "\n")    
    with open('mix.txt', 'a', encoding='utf-8') as output_file:
        output_file.write(text)    


