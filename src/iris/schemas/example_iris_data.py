import pandera as pa
from pandera.typing import Series

class ExampleIrisDataSchema(pa.DataFrameModel):
    sepal_length: Series[int] = pa.Field(gt=2000)

schema = ExampleIrisDataSchema