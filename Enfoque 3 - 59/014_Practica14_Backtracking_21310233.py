# -*- coding: utf-8 -*-
"""
@author: Diego Ivan Garcia Monteon
           21310233    6E1
            Inteligencia Artificial
"""

#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

def backtrack_combinations(target, nums, path, result):
    if target == 0:
        result.append(path)
        return
    if target < 0 or not nums:
        return
    for i in range(len(nums)):
        backtrack_combinations(target - nums[i], nums[i+1:], path + [nums[i]], result)

# Ejemplo de uso
target = 7
nums = [2, 3, 6, 7]
result = []
backtrack_combinations(target, nums, [], result)
print("Combinaciones que suman", target, ":", result)