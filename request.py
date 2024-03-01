from typing import Dict


class Request:
     
    def __init__(self,items:Dict[str,int],items_prices:Dict[str,float]) -> None:
        self.items:Dict[str:int] = items
        self.items_prices:Dict[str:float] = items_prices

    def get_total_cost(self)-> int:
        '''get total cost for all the items'''
        total_cost = 0
        for item,amount in self.items.values():
            total_cost += amount * self.items_prices[item]
        return total_cost
    
    def add_item(self,item:str,amount:int,cost:float):
        '''Add item  into request'''
        if item in self.items.keys():
            self.items[item] += amount
            self.items_prices[item] = cost
        else:
            self.items[item] = amount
            self.items_prices[item] = cost

    def get_item_cost(self,item) -> float:
        '''return the cost of an item'''
        if item in self.items.keys():
            return self.items_prices[item]
        
    def generate_request(self, order: Dict[str, int]):
        for item, amount in order.items():
            if(item in self.items_prices.keys()):
                cost = self.items_prices[item]
                self.add_item(item, amount,cost)
       