class stack:
    def __init__(self):
        self.stack = []
        


def push(stack_obj, data):
    stack_obj.stack.append(data)
    
def pop(stack_obj):
    if len(stack_obj.stack) == 0:
        return None
    return stack_obj.stack.pop()

def peek(stack_obj):
    if len(stack_obj.stack) == 0:
        return None
    return stack_obj.stack[-1]

def print_stack(stack_obj):
    print(stack_obj.stack)



s = stack()

push(s,12)
push(s,15)
push(s,14)
push(s,13)

print_stack(s)

print(pop(s))

print(peek(s))

        