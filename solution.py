import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest


chat_id = 1019285902 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    x = [1] * int(x_success) + [0] * int(x_cnt - x_success)
    y = [1] * int(y_success) + [0] * int(y_cnt - y_success)
    pvalue = ztest(y, x, alternative="larger")[1]
    ans = True if pvalue < 0.06 else False
    return ans # Ваш ответ, True или False
