import pandera as pa
import pandas as pd

data = pd.read_csv("../data/01_raw/iris.csv")

schema = pa.infer_schema(data)
print(schema)

schema.to_script()
schema.to_yaml()