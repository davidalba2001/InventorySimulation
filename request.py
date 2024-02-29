from typing import Dict


class Request:
    
    def __init__(self,items:Dict[str:int]={},items_prices:Dict[str:float]= {}) -> None:
        self.items:Dict[str:int] = items
        self.items_prices:Dict[str:float] = items_prices
    
    def get_total_cost(self)-> int:
        total_cost = 0
        for item,amount in self.items.values():
            total_cost += amount * self.items_prices[item]
        return total_cost
    
    def add_item(self,item:str,amount:int,cost:float):
        if item in self.items.keys(): 
            _amount,_cost =  self.items[item]
            self.items[item] = (_amount + amount,cost)
        else:
            self.items[item] = (amount,cost)

    def get_item_cost(self,item) -> float:
        if item in self.items.keys():
            return self.items_prices[item]