import stack

string = "gninraeL nldekiL htiw tol a nraeL"
reverse_string = ""
a = stack.Stack()

# my solution
for item in string:
    a.push(item)

while not a.is_empty():
    reverse_string += a.pop()
# my solution

print(reverse_string)