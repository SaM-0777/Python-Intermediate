# Strings : oredered, immutable, text representation


s = "Strings - 'Hello World'"
print(s)

s = """hello
world"""
print(s)

s = "Hello World"
char = s[:1]
print(char)

# Slicing
sub = s[1:6]
print(sub)

sub = s[::-1]
print(sub)

sub = s[0:10:2]
print(sub)

if 'e' in s:
    print('Yes')
else:
    print('No')

s = "   Hello World    "
s = s.strip()
# s.strip() not work
print(s)

print(s.lower())
print(s.upper())
print(s.startswith("Hello"))
print(s.endswith("Hello"))
print(s.find("lo"))
print(s.count("l"))
print(s.replace("World", "People"))

# list and Strings
s = "how r u ?"
list = s.split()    # default : " "
print(list)

s = "how, join, link"
list = s.split(", ")
print(list)

new_str = ''.join(s)
print(new_str)

my_list = 'a' * 6
print(my_list)

my_str = ''
for i in my_list:
    my_str += i
print(my_str)

my_str = ''.join(my_list)
print(my_str)

# %, format(), f'strings
var = "Tom"
str = "Ther Var : %s" %var
print(str)

var1 = 3
print("var : %d" %var1)

var2 = 3.15425625622555
print("var : %f" % var2)
print("var : %.2f" % var2)

print(f'Var1 : {var1 ** 2}\nVar2 : {var2 + 50.066}')  # Faster method out of all methods