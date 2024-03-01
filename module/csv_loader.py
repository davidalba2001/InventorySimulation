import csv
from typing import Dict
#-> Dict[str, Dict[str, int]]:
def load_inventory_data(file_path: str):
    """
    Carga los datos de inventario desde un archivo CSV y devuelve los diccionarios necesarios
    para construir una instancia de InventoryManager.

    Parámetros:
    - file_path (str): Ruta del archivo CSV.

    Retorna:
    - Dict[str, Dict[str, int]]: Diccionario con los diccionarios de almacenamiento,
                                 niveles de reorden y niveles objetivo, y precios de los
                                 artículos.
    """
    provider = []
    storage = {}
    reorder_level = {}
    target_level = {}
    item_prices = {}

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
       
        for row in reader:
            prov = row['Provider']
            if(prov not in provider):
                provider.append(prov)
            product = row['Product']
            storage[product] = int(row['Target Level'])
            reorder_level[product] = int(row['Reorder Level'])
            target_level[product] = int(row['Target Level'])
            item_prices[product] = float(row['Cost'])

    return {
        'provider':provider[0],
        'storage': storage,
        'reorder_level': reorder_level,
        'target_level': target_level,
        'item_prices': item_prices
    }

