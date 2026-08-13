# Last updated: 13/08/2026, 22:22:56
1import pandas as pd
2from typing import List
3def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
4    df = pd.DataFrame(student_data, columns=["student_id", "age"])
5    return df
6