# InventorySimulation

## Características de la simulación

Se tiene una tienda con un stock de productos en el inventario y se desea modelar las siguientes dinámicas:

### El stock se debe reabastecer para mantener un nivel adecuado.

#### Variables importantes:

- Inventario actual: **x** --> Representa la cantidad actual de productos disponibles en el inventario.
- Nivel de reorden: **s** --> Representa el nivel mínimo requerido para realizar un nuevo pedido de suministros a los proveedores.
- Nivel objetivo: **S** --> Representa el nivel máximo de llenado que se desea mantener en el inventario. Este nivel puede depender del tiempo o ser un parámetro fijo.

#### Política de pedido:

- Si el inventario actual es menor que el nivel de reorden y no hay un pedido pendiente, se realiza un pedido al distribuidor para llevar el inventario hasta el nivel objetivo (***x < s ∧ ¬∃p  -> ordenar S-x productos***)

### Existen costos asociados a distintos eventos internos de la tienda 

#### Costos asociados a un pedido:
- **c(n)** --> Es una función específica que determina el costo de realizar un pedido de y unidades del producto.
- **L** --> Unidades de tiempo hasta que se entrega el pedido, con el pago realizado a la entrega.

#### Costo de mantenimiento:
- **h** --> Costo de mantenimiento del inventario dependiente de los artículos y el tiempo.

### En relación con las demandas de los clientes

#### Demanda y ventas:

- Si un cliente solicita más productos de los que están disponibles en el inventario, se vende la cantidad disponible y el resto del pedido se pierde para la tienda.