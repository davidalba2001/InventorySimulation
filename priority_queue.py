import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    
    def add_item(self,item,start_time, duration):
        '''item = (type_event,num_event,wait_time)'''
        '''start_time = current_time'''
        '''duration = ramdom arrive_time'''
        entry = ( start_time + duration, item)
        heapq.heappush(self.queue, entry)
        self.counter += 1

    def get_next_item(self):
        if(self.counter > 0):
            start_time, item = heapq.heappop(self.queue)
            self.counter -= 1
            return start_time,item
        return None
    
    def peek(self):
        if self.counter > 0:
            # Devuelve toda la tupla del elemento superior sin modificar la cola
            return self.queue[0]
        else:
            return None
