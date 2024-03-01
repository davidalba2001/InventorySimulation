from typing import Dict, List

import numpy as np
from request import Request


class Store:
    def __init__(self, storage: Dict[str, int] = {}, reorder_level: Dict[str, int] = {}, target_level: Dict[str, int] = {}, item_prices: Dict[str, float] = {}, budget: float = 0) -> None:
        self.storage: Dict[str, int] = storage
        self.reorder_level: Dict[str, int] = reorder_level
        self.target_level: Dict[str, int] = target_level
        self.items_prices: Dict[str, float] = item_prices
        self.budget = budget
        self.isOpen = True
        self.pending_request: Dict[str, bool] = {
            product: False for product in storage.keys()}
        self.financial_losses: Dict[str, int] = {
            product: 0 for product in storage.keys()}
        self.unattended = 0
        self.charges = 0

    # reorder_level es s
    # target_level es S
    # storage es x

    @property
    def total_items(self):
        return sum(self.storage.values())

    def add_type(self, item: str, cost: float, reorder_level: int, target_level: int, amount: int = 0):

        if not (reorder_level < target_level):
            raise ValueError(
                "Parameter error: reorder_level < target_level")
        if item not in self.storage.keys():
            self.storage[item] = amount
            self.reorder_level[item] = reorder_level
            self.target_level[item] = target_level
            self.items_prices[item] = cost
            self.financial_losses[item] = 0
            self.pending_request[item] = False

        else:
            print("Product already exists in the inventory")

    def add_item(self, item: str, amount: int):
        if item not in self.storage:
            raise ValueError(
                f"Product '{item}' does not exist in the inventory. Please add the product type first.")
        else:
            self.storage[item] += amount

    def update_storage(self, request: Request):

        for item in request.items.keys():

            if item in self.storage.keys():

                amount = request.items[item]
                cost = self.items_prices[item]
                self.add_item(item, amount)
                self.budget -= amount * cost
                self.pending_request[item] = False
            else:
                print(f"not type item:({item}) found in storage")

    def charge_storage_fee(self,storage_fee_rate = 0.1):
        for item in self.storage.keys():
            amount = self.storage[item]
            cost = self.items_prices[item]
            self.charges += amount * cost * storage_fee_rate
            self.budget -= amount * cost * storage_fee_rate
            
        

    def items_pending_request(self) -> List[str]:
        items = []
        for item in self.storage.keys():
            need_repose = self.reorder_level[item] >= self.storage[item]
            not_pendingr_equest = not self.pending_request[item]
            if (need_repose and not_pendingr_equest):
                self.check_view(item, need_repose, not_pendingr_equest)
                items.append(item)

        return items

    def check_view(self, item, need_repose =  None, not_pendingr_equest = None):
        print(
            f"item:{item}, need_repose:{need_repose},not_pendingr_equest:{not_pendingr_equest}")
        print(
            f"storage({item}):{self.storage[item]},reorder_level:{self.reorder_level[item]},target_level:{self.target_level}")
       
        if (self.storage[item] > self.target_level[item]):
            print("A L E R T A   E S T O   N O   D E B E R I A   P A S A R")
            print(item, self.storage[item])

    def manage_requests(self) -> (bool, Request):
        items = self.items_pending_request()
        request =  Request({},{})
      
        self.check_(request)
        pendig_request = False
        for item in items:
            pendig_request = True
            amount_needed = self.target_level[item] - self.storage[item]
            cost = self.items_prices[item]
            request.add_item(item, amount_needed, cost)
            self.pending_request[item] = True
        
        
        return pendig_request, request
    
    def check_(self,request:Request):
        _storage = self.storage.copy() 
        for item in _storage.keys():
            if item in request.items.keys():
                _storage[item]+= request.items[item]
                if(self.target_level[item] <  _storage[item]):
                    print("Alert")



    def spend_attend_time(self, lambda_value=2) -> float:
        return np.random.exponential(lambda_value)

    def attend_customers(self, request: Request, take_profit):

        for (item, amount) in request.items.items():
            if item in self.storage.keys():
                if self.storage[item] >= amount:
                    self.storage[item] -= amount
                    cost = self.items_prices[item]
                    profit = amount * cost * take_profit
                    self.budget += profit
                elif (self.storage[item] > 0):
                    amount_losses = amount - self.storage[item]
                    cost = self.items_prices[item]
                    profit = self.storage[item] * cost * take_profit
                    self.budget += profit
                    self.financial_losses[item] += amount_losses
                    self.storage[item] = 0
                else:
                    self.financial_losses[item] += amount



    