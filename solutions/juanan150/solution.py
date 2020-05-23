"""Script que duplica los 0 de una lista sin modificar la longitud de la misma"""
from typing import List

class Solution:
    """Objeto del ejercicio"""
    def duplicate_zeros(self, arr: List[int]):
        """Funcion que duplica los 0s"""
        temp = list(arr)
        j = 0

        for val in temp:
            if j == len(temp):
                break

            if val == 0 and j < len(temp)-1:
                arr[j] = val
                j += 1
                arr[j] = val
            else:
                arr[j] = val
            j += 1
