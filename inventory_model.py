from customer import Customers
from request import Request
from store import Store
from priority_queue import PriorityQueue
from suppliers import Suppliers
from enum import Enum
import sys
import numpy as np

"""
Si en evento es un recive customer la cola tendra dentro 
(event,n_event,wait),time
Si en evento es un anttend customer la cola tendra dentro 
(event,n_event,wait),time
Si en evento es un manage request la cola tendra dentro 
(event,n_event,request),time

"""

class TypeEvent(Enum):
    ReciveCustomer = 1
    ManageRequest = 2

class SimulateInventory_Model:
   
    def __init__(self,simulator_store:Store,simulator_suppliers:Suppliers,end_time = 1) -> None:
        self.customers = Customers()
        self.store = simulator_store
        self.suppliers = simulator_suppliers
        self.queue = PriorityQueue() 
        self.end_time = end_time*24*60
        self.current_time = 0

    

    def simulate_events_store(self):
        stdout_original = sys.stdout
    
        with open('output.txt', 'w') as f:
            sys.stdout = f
            while(self.store.isOpen):

                if(self.current_time % (24 * 60) == 0):
                    self.store.charge_storage_fee()

                pending_request,request = self.store.manage_requests()

                # Recive customer if store is open and queue is empty 
                if(self.current_time < self.end_time and self.queue.counter == 0):
                    arrival_time,wait_time = self.customers.event_arrival()
                    self.queue.add_item((TypeEvent.ReciveCustomer,self.customers.count_arrivals,wait_time),self.current_time,arrival_time)
                # Close store and repose items
                elif(self.queue.counter == 0):
                     self.store.isOpen = False
                     if(pending_request):
                        self.store.update_storage(request=request)
                     break
                 
                #Create event for repose storage 
                if(pending_request):
                    
                    #Count the number of requests
                    self.suppliers.countRequest +=1
                    #Create event ManageRequest
                    delivery_time = self.suppliers.generate_delivery_time()
                    self.queue.add_item((TypeEvent.ManageRequest,self.suppliers.countRequest,request),self.current_time,delivery_time) 

                # Extract event in top the queue
                start_time_event,(type_event,n_event,wait_time_or_request)= self.queue.get_next_item()


                if(TypeEvent.ReciveCustomer == type_event):
                    # if the type event is ReciveCustomer then wait_time_or_request is wait_time not a request
                    wait_time =  wait_time_or_request
                    # generate a random time that simulates how long it takes to serve a customer
                    spend_attend_time = self.store.spend_attend_time()
                    # If the current time is before the time of the new event, move the time to the time of the new event.
                    self.current_time = max(self.current_time ,start_time_event)
                    
                    
                    attend_event_time  = self.current_time + spend_attend_time

                    if(attend_event_time - start_time_event <= wait_time_or_request):
                        
                        order = self.customers.generate_order(self.store.storage.keys())
                        request = Request(order,self.store.items_prices)

                        self.current_time = attend_event_time

                        self.store.attend_customers(request,1.10)
                        
                        # If the simulation time has not ended, you will receive a new client
                        if(self.current_time < self.end_time):
                            arrival_time,wait_time = self.customers.event_arrival()
                            self.queue.add_item((TypeEvent.ReciveCustomer,self.customers.count_arrivals,wait_time),self.current_time,arrival_time)                        
                    else:
                        # unattended increases if a customer cannot be attended to on time
                        self.store.unattended +=1
                        
                if(TypeEvent.ManageRequest == type_event):
                    # move in time line  
                    self.current_time = start_time_event
                    # if the type event is ManageRequest then wait_time_or_request is wait_time not a request
                    request = wait_time_or_request
                    # update state store 
                    self.store.update_storage(request=request)

            sys.stdout = stdout_original

   