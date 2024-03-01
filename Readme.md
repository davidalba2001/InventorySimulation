# Proyecto: Simulación de Eventos Discretos

Este proyecto se centra en la simulación de eventos discretos para analizar y mejorar la gestión del inventario en un entorno de comercio minorista. La simulación tiene como objetivo modelar el comportamiento del inventario y evaluar diferentes políticas de reordenamiento para minimizar la pérdida de clientes y optimizar la eficiencia operativa.

## Detalles de Implementación

Para implementar la simulación, se desarrollaron varias clases y métodos en Python para representar los componentes clave del sistema, como clientes, tiendas, proveedores y solicitudes de productos. A continuación se describen los principales aspectos de la implementación:

1. **Clase Customers:**
   Esta clase simula el comportamiento de los clientes, generando eventos de llegada, creando pedidos aleatorios y determinando el tiempo de espera de los clientes.
   - Métodos:
     - `generate_next_arrivals_time`: Genera tiempos de llegada de clientes basados en una distribución exponencial.
     - `generate_order`: Genera pedidos aleatorios para los clientes, seleccionando productos de manera probabilística.
     - `generate_wait_time`: Genera tiempos de espera aleatorios para los clientes antes de ser atendidos.

2. **Clase Request:**
   Esta clase representa las solicitudes de productos realizadas por los clientes, incluidos los productos solicitados y sus cantidades.
   - Métodos:
     - `get_total_cost`: Calcula el costo total de una solicitud de productos.
     - `add_item`: Agrega un nuevo artículo a la solicitud.
     - `get_item_cost`: Obtiene el costo de un artículo específico en la solicitud.

3. **Clase Store:**
   Esta clase modela la tienda minorista, incluyendo su inventario, niveles de reorden, precios de productos y presupuesto.
   - Métodos:
     - `add_type`: Agrega un nuevo tipo de producto al inventario de la tienda.
     - `add_item`: Agrega una cierta cantidad de un artículo al inventario existente.
     - `update_storage`: Actualiza el inventario de la tienda después de recibir un pedido del proveedor.
     - `charge_storage_fee`: Aplica una tarifa de almacenamiento al inventario de la tienda.
     - `manage_requests`: Gestiona las solicitudes de productos pendientes y decide si realizar pedidos adicionales al proveedor.
     - `attend_customers`: Atiende a los clientes, actualizando el inventario y calculando los ingresos obtenidos.

4. **Clase Suppliers:**
   Esta clase representa a los proveedores de la tienda, que son responsables de suministrar productos y generar facturas.
   - Métodos:
     - `generate_invoice`: Genera una factura para un pedido de productos.
     - `generate_delivery_time`: Genera tiempos de entrega aleatorios para los pedidos.

**Otros Componentes:**
- Se implementó una cola de prioridad para gestionar los eventos de manera eficiente durante la simulación.
- Se utilizaron algoritmos de distribución exponencial y aleatoria para modelar la llegada de clientes y los tiempos de entrega de pedidos.

## Clase SimulateInventory_Model

Esta clase se encarga de simular el comportamiento del inventario y las interacciones entre los clientes, la tienda y los proveedores. Aquí se modelan los eventos discretos, como la llegada de clientes, la gestión de pedidos y la entrega de productos. Algunas características importantes de esta clase incluyen:

- Métodos para simular eventos específicos, como la llegada de clientes (`event_arrival`) y la gestión de pedidos (`manage_requests`).
- Utiliza una cola de prioridad para planificar y ejecutar los eventos en el momento adecuado.
- Gestiona el tiempo de simulación y controla el flujo de eventos hasta que se alcance el final de la simulación.
- Interactúa con la clase Store y Suppliers para realizar operaciones de inventario y gestión de pedidos.

## Clase GeneticAlgorithm

Esta clase se encarga de optimizar los parámetros del modelo de simulación utilizando un algoritmo genético. Aquí se busca encontrar los valores óptimos para los niveles de reordenamiento que minimizan el número de clientes no atendidos. Algunas características importantes de esta clase incluyen:

- Definición de la función de aptitud (fitness) que evalúa qué tan bien funcionan los diferentes conjuntos de niveles de reordenamiento.
- Implementación de operadores genéticos, como la selección, el cruce y la mutación, para evolucionar y mejorar las soluciones candidatas.
- Evaluación de múltiples generaciones de soluciones y seguimiento del progreso para encontrar la mejor solución posible.
- Interacción con la simulación de inventario para ejecutar cada evaluación de aptitud y obtener los resultados necesarios.

## Resultados y Experimentos

En la sección de Resultados y Experimentos, nuestro objetivo fue optimizar un vector que contiene los niveles de reordenamiento utilizando un algoritmo genético para minimizar la pérdida de clientes. Durante el proceso, encontramos que el algoritmo genético presentaba lentitud debido a la necesidad de simular el comportamiento del inventario para poder calcular el fitness de cada vector de niveles de reordenamiento. Calculamos el fitness como el inverso de la cantidad de clientes no atendidos para evaluar la efectividad de cada vector en minimizar esta pérdida.

Las limitaciones en tiempo y recursos computacionales nos impidieron realizar simulaciones más extensas, lo que significa que solo pudimos simular el comportamiento del inventario durante un día y ejecutar la simulacion una vez para determinar el fitness de un vector. Esto puede haber afectado la representatividad de nuestros resultados, ya que se basan en una única ejecución de la simulación y un conjunto limitado de datos.

Además, no consideramos la variabilidad en la demanda de los clientes, en la vida real los hay ciertos productos mas vendidos que otros, es no lo tiene en cuenta el proyecto actualmente, simplemente generamos órdenes de compra aleatorias. Esta simplificación puede haber afectado la precisión de nuestros resultados y provocar variaciones cada vez que se ejecuta el algoritmo de optimización.

En conclusión, aunque logramos encontrar un vector que minimizaba la pérdida de clientes utilizando un algoritmo genético, nuestras limitaciones en recursos y enfoque de simulación podrían haber impactado la precisión y aplicabilidad de nuestros resultados. Para futuras investigaciones, recomendamos considerar estrategias más sofisticadas para la generación de órdenes de compra y realizar múltiples ejecuciones de la simulación para obtener una evaluación más robusta de los vectores de niveles de reordenamiento óptimos.





