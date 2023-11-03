import torch
import numpy as np


__all__ = ['TensorCalculator']

class TensorCalculator():

    def __init__(self):

        return None

    def tensor_ones(self,dim_x,
                    dim_y,
                    dim_z):

        ones = torch.ones([dim_x,dim_y,dim_z])

        return ones
    
    def tensor_zeros(self,dim_x,
                    dim_y,
                    dim_z):

        zeros = torch.zeros([dim_x,dim_y,dim_z])

        return zeros
    
    def tensor_random(self,dim_x,
                    dim_y,
                    dim_z):

        random = torch.rand([dim_x,dim_y,dim_z])

        return random
    
    def tensor_sum(self,tensor1):

        return torch.sum(tensor1)
    
    
    def tensor_sqrt(self,tensor1):
        return np.sqrt(tensor1)
    
    def tensor_mean(self, tensor):
        return torch.mean(tensor)

    def tensor_mult(self, tensor1, tensor2):
        return torch.mul(tensor1, tensor2)

    def tensor_transpose(self, tensor):
        return tensor.permute(2, 1, 0)

# Ejemplo de uso
dim_x, dim_y, dim_z = 3, 4, 5
x = TensorCalculator()
ones_tensor = x.tensor_ones(dim_x, dim_y, dim_z)
zeros_tensor = x.tensor_zeros(dim_x, dim_y, dim_z)
random_tensor = x.tensor_random(dim_x, dim_y, dim_z)

sum_result = x.tensor_sum(ones_tensor)
mult_result = x.tensor_mult(ones_tensor, random_tensor)
sqrt_result = x.tensor_sqrt(random_tensor)
mean_result = x.tensor_mean(ones_tensor)
transposed_tensor = x.tensor_transpose(random_tensor)

print("Suma de unos:", sum_result)
print("Multiplicacion de unos y aleatorios:", mult_result)
print("Media de unos:", mean_result)
print("Tensor transpuesto:", transposed_tensor)
