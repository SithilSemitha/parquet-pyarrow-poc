import string
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from pandas.testing import assert_frame_equal


def create_small_dataset() -> pd.DataFrame:
    data = {
        "course_id": ["001", "002", "003", "004", "005"],
        "course_name": ["Computer Science", "Mathematics", "Physics", "Chemistry", "Biology"],
        "students": [
            ["Alice", "Bob", "Sam"],
            ["Harry", "Ricky"],
            ["George", "Kathy", "Megan"],
            ["Will", "Jhon", "Peter", "Ryan"],
            ["Bill"]
        ]
    }
    return pd.DataFrame(data)


def create_large_dataset() -> pd.DataFrame:
    rows_count = 100000
    max_list_size = 10

    rng = np.random.default_rng()

    def random_int(low, high): return rng.integers(low, high=high, endpoint=True)
    def random_ints_list(size): return rng.integers(0, 100, size=size)
    def random_floats_list(size): return rng.random(size=size)
    def random_booleans_list(size): return rng.choice([True, False], size=size)
    def random_string(length): return "".join(rng.choice(list(string.printable), size=length))
    def random_strings_list(size, str_length=10): return [random_string(str_length) for _ in range(size)]

    data = {
        "row_id": range(0, rows_count),
        "int_col": random_ints_list(rows_count),
        "float_col": random_floats_list(rows_count),
        "bool_col": random_booleans_list(rows_count),
        "str_col": random_strings_list(rows_count),
        "ints_list_col": [random_ints_list(random_int(0, max_list_size)) for _ in range(rows_count)],
        "floats_list_col": [random_floats_list(random_int(0, max_list_size)) for _ in range(rows_count)],
        "bools_list_col": [random_booleans_list(random_int(0, max_list_size)).tolist() for _ in range(rows_count)],
        "strs_list_col": [random_strings_list(random_int(0, max_list_size)) for _ in range(rows_count)],
    }
    return pd.DataFrame(data)


