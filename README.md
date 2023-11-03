# MACHINELEARNING
 # Tensor Calculator

Este proyecto proporciona una clase `TensorCalculator` que te permite realizar diversas operaciones con tensores en PyTorch. La clase `TensorCalculator` incluye métodos para crear tensores de unos, tensores de ceros y tensores aleatorios, así como para realizar operaciones comunes con tensores.

## Uso

Para utilizar la clase `TensorCalculator`, sigue estos pasos:

1. Importa la clase en tu código:

```python
from tensor_calculator import TensorCalculator

x = TensorCalculator()
# Crear un tensor de unos
ones_tensor = x.tensor_ones(3, 4, 5)

# Realizar la suma de un tensor de unos
sum_result = x.tensor_sum(ones_tensor)

# Calcular la media de un tensor de unos
mean_result = x.tensor_mean(ones_tensor)

#Métodos Disponibles
#La clase TensorCalculator proporciona los siguientes métodos:

tensor_ones(dim_x, dim_y, dim_z): #Crea un tensor de unos con las dimensiones especificadas.

tensor_zeros(dim_x, dim_y, dim_z): #Crea un tensor de ceros con las dimensiones especificadas.

tensor_random(dim_x, dim_y, dim_z): #Crea un tensor aleatorio con las dimensiones especificadas.

tensor_sum(tensor): #Calcula la suma de los elementos de un tensor.

tensor_mean(tensor):# Calcula la media de los elementos de un tensor.

tensor_mult(tensor1, tensor2): #Realiza el producto de dos tensores elemento por elemento.

tensor_transpose(tensor): #Realiza la transposición de un tensor.

## Ejemplo
## Puedes encontrar un ejemplo de uso de la clase TensorCalculator en el archivo example.py en este repositorio.
