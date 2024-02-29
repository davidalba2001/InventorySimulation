from typing import Dict
from request import Request


class Store:
    def __init__(self, storage: Dict[str, int] = {}, reorder_level: Dict[str, int] = {}, target_level: Dict[str, int] = {}, item_prices: Dict[str, float] = {}, budget: float = 0) -> None:
        self.storage: Dict[str, int] = storage
        self.reorder_level: Dict[str, int] = reorder_level
        self.target_level: Dict[str, int] = target_level
        self.items_prices: Dict[str, float] = item_prices
        self.budget = budget
        self.pending_request: Dict[str, bool] = {
            product: False for product in storage.keys()}
        self.financial_losses: Dict[str, int] = {
            product: 0 for product in storage.keys()}

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
            self.item_prices[item] = cost
            self.financial_losses[item] = 0
            self.pending_order[item] = False
        else:
            print("Product already exists in the inventory")

    def add_item(self, item: str, amount: int, cost: float):
        if item not in self.storage:
            raise ValueError(
                f"Product '{item}' does not exist in the inventory. Please add the product type first.")
        else:
            _amount = self.storage[item]
            _cost = self.items_prices[item]
            self.storage[item] = (_amount + amount, max(cost, _cost))

    def update_storage(self, request: Request):
        for item in request.items.keys():
            if item in self.storage.keys():
                _amount = self.storage[item]
                cost = request.get_item_cost(item)
                _cost = self.items_prices[item]
                self.add_item(item, _amount, max(cost, _cost))
            print(f"not type item:({item}) found in storage")

    def items_pending_request(self)-> list(str):
        return [item for item in self.storage.keys() if self.pending_request[item] and self.reorder_level[item] > self.storage[item]]

    def manage_requests(self)-> (bool,Request):  
        items = self.items_pending_request()
        request = Request()
        pendig_request = False
        for item in items:
            pendig_request = True
            amount_needed = self.target_level[item] - self.storage[item]
            cost = self.items_prices[item]       
            request.add_item(item,amount_needed,cost)
            self.pending_request[item] = True
        return pendig_request,Request

   
