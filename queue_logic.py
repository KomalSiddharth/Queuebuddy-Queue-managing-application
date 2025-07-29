queue=[] # it is a simple list 
# adds user to the the queue
def join_queue(name):
    queue.append(name)
    return len(queue)
# returns the full list
def get_queue():
    return queue
# removes the firts user
def next_customer():
    if queue:
        return queue.pop(0)
    return None 