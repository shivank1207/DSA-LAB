# Given entry/exit logs of customers and a cyber cafe's capacity,
# find the total number of customers who could not get any computer
def process(sequence, capacity):
    if not sequence:
        return 0
    allocated = set()
    visited = set()
    unattended = 0
    for i in sequence:
        if i not in visited:
            # mark customer as visited
            visited.add(i)
            # if a computer is available, allocate it to the customer
            if len(allocated) < capacity:
                allocated.add(i)
            # if no computer is available, increment the unattended customer's count
            else:
                unattended += 1
        # if a customer is leaving the cyber cafe, mark the customer as unvisited
        # and deallocate the computer
        else:
            visited.remove(i)
            if i in allocated:
                allocated.remove(i)
    return unattended
 
 
if __name__ == '__main__':
    sequence = 'WECEABCDDFFEBGAG'
    capacity = 3
    print(process(sequence, capacity))