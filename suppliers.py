import random
from typing import Dict
from request import Request


class Suppliers:
    def __init__(self, name: str, item_cost: Dict[str, float] = None) -> None:
        self.name = name
        if item_cost is None:
            item_cost = {}  # Inicializar el diccionario si no se proporciona
        self.item_cost = item_cost
        self.countRequest = 0
    
    def add_product(self,item, cost):
        if item not in self.item_cost.keys():
            self.item_cost[item] = cost
        else:
            print("change cost product")
            self.item_cost[item] = cost

    def generate_invoice(self, order: Dict[str, int]):
        invoice = Request(order,self.item_cost)
        invoice.generate_request(order)
        return invoice

    def generate_delivery_time(self,lambda_ = 3):
       return  random.expovariate(lambda_)