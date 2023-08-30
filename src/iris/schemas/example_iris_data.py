import pandera as pa
from pandera.typing import Series

class ExampleIrisDataSchema(pa.DataFrameModel):
    sepal_length: Series[float] = pa.Field(gt=2000)

