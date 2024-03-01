from store import Store
from module.csv_loader import load_inventory_data
from inventory_model import SimulateInventory_Model
from suppliers import Suppliers
from request import Request
from inventory_optimizer import InventoryOptimizer
def main():
    # Carga los datos del CSV
    data = load_inventory_data('data/data_inventory.csv')
    suppliers: Suppliers =  Suppliers(data['provider'],data['item_prices'])
    store:Store = Store(storage=data['storage'],reorder_level=data['reorder_level'],
                        target_level=data['target_level'],item_prices=data['item_prices'],budget=0)
    
    model = SimulateInventory_Model(store,suppliers)
    optimizer = InventoryOptimizer(data)


    optimized_levels = optimizer.optimize_reorder_levels()
    model.simulate_events_store()
    print(optimized_levels)
    
    # {'iPhone 13': 66, 'Samsung Galaxy S21': 19, 'Google Pixel 6': 64, 'OnePlus 9 Pro': 40, 
    #  'Sony Xperia 1 III': 52, 'USB-C Charger': 22, 
    #  'Lightning Cable': 46, 'Wireless Earbuds': 50, 'Smartphone Case': 16, 'Screen Protector': 9}

    

if __name__ == "__main__":
    main()


