from typing import Dict
import numpy as np
from genetic_algorithm import GeneticAlgorithm
from inventory_model import SimulateInventory_Model
from store import Store
from suppliers import Suppliers

class InventoryOptimizer:
    def __init__(self,data) -> None:
        self.provider = data['provider']
        self.item_prices = data['item_prices']
        self.storage = data['storage']
        self.initial_levels = data['reorder_level']
        self.target_level = target_level=data['target_level']

    
    def evaluate_reorder_levels(self,reorder_level,avg = 1):
        simulated_levels = {product: reorder_level[i] for i, (product, _) in enumerate(self.storage.items())}
        
        average_unattended = 0
        for _ in range(avg):
            suppliers: Suppliers =  Suppliers(self.provider,self.item_prices)
            store:Store = Store(self.storage,simulated_levels,self.target_level,self.item_prices,0)
            model = SimulateInventory_Model(store,suppliers)
            model.simulate_events_store()
            average_unattended += model.store.unattended

        average_unattended  = average_unattended / avg
        
        return 1/average_unattended

        
        

    
    def optimize_reorder_levels(self) -> Dict[str, int]:
        
        gene_limits = [(0,level) for level in self.target_level.values()]

        ga = GeneticAlgorithm(population_size=20, chromosome_length=len(self.initial_levels.values()), gene_limits=gene_limits)
        best_solution = ga.run(self.evaluate_reorder_levels, max_generations=10)

        best_levels = {product: best_solution[i] for i, (product, _) in enumerate(self.initial_levels.items())}
        return best_levels

