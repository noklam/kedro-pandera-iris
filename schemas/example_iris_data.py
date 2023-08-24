import pandera as pa

class ExampleIrisDataSchema(pa.DataFrameModel):
    sepal_length: Series[int] = pa.Field(gt=2000)
