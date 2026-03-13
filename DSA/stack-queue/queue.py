class queue:
    def __init__(self):
        self.queue = []
        
def enqueue(q,data):
    q.queue.append(data)
    
def dequeue(q):
    if len(q.queue) == 0:
        return None
    return q.queue.pop(0)


def front(q):
    if len(q.queue) == 0:
        return None
    return q.queue[0]

def is_empty(q):
    return len(q.queue) == 0

def print_queue(q):
    print(q.queue)

q = queue()

enqueue(q,10)
enqueue(q,20)
enqueue(q,30)
print_queue(q)

dequeue(q)
print_queue(q)
