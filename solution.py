#хотим узнать, может ли увеличиться конверсия, то есть
#H0: a0 = a1, значит, алтернатива:
#H1: a0 < a1, где a0 - конверсия историческая (контроль), a1 - на тесте, то есть мы хотим отклонить гипотезу
#‘larger’

import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 728846853 # Ваш chat ID, не меняйте название переменной


def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
 
p = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='smaller')[1] 
if p < 0.08:
  return True
else:
  return False
