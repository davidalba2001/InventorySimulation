from typing import List,Dict
import numpy as np


class Customers:
    def __init__(self) -> None:
        self.count_arrivals : int = 0
        
    # generate random time for customer arrival
    def generate_next_arrivals_time(self,lambda_value = 6) ->float:
        return np.random.exponential(lambda_value)

    # generates a random order from a customer
    def generate_order(self,list_items)-> Dict[str,int]:
        order : Dict[str,int] = {} 
        for item in list_items:
            if np.random.choice([True, False], p=[0.5, 0.5]):
                amount = max(1,int(np.random.normal(5,5)))
                order[item] = amount
        return order
    
    # generates a random time for how long the customer is willing to wait
    def generate_wait_time(self,lambda_value = 10) -> float:
        return np.random.exponential(lambda_value)

    # generates an arrival event and counts the number of arrivals
    def event_arrival(self):
        self.count_arrivals += 1
        return (self.generate_next_arrivals_time(),self.generate_wait_time())


        
