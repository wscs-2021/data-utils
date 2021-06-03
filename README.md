# data-utils

[![example workflow](https://github.com/wscs-2021/data-utils/actions/workflows/test.yml/badge.svg)](https://github.com/wscs-2021/data-utils/actions/workflows/test.yml)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4889447.svg)](https://doi.org/10.5281/zenodo.4889447)

A data utility package for Brane.

## Features

Currently, we only have a single feature:

-  Downcast data files, which makes sure that their data types per column are using the most efficient data type memory-wise.

## Installation

Import directly from GitHub:

```sh
brane import wscs-2021/data-utils
```

## Requirements

- pandas
- numpy
- parquet engine, e.g. fastparquet/pyarrow

### Dev requirements

- pytest

## Usage

Function **downcast**:

`downcast(input_path, output_dir)`

```sh
> import data-utils;
> downcast("path/to/input.csv", "path/to/output_dir/")

Wrote optimised file to a 'parquet' file.
    Disk Usage: 2.88k KB -> 2.43 KB (-15.57%)
    Memory Usage: 5.25 KB -> 1.73 KB (-67.07%)
```

## Test

Run unit tests with `pytest`:

```sh
pytest
```

Test whether the API is executable:

```sh
make test_executable
```

Test in Brane:

```sh
$ brane --debug test -d . downcast

✔ The function the execute · downcast

Please provide input for the chosen function:

[2021-05-26T10:28:13Z DEBUG] {}
✔ inputpath (string) · /data/downcast/test/sample.csv
[2021-05-26T10:28:23Z DEBUG] {}
✔ outputpath (string) · /data/downcast/test/output.parquet
```

You should now see `output.parquet` in `./downcast/test/output.parquet`.

## Schema (optional) 

For more advanced use cases, users may provide additional context to the package for each variable through the use of a schema. For example, the schema can be used to specify the downcast data type, the categories for nominal variables and their order for ordinal ones.

As Brane is currently still in development, dictionnary type variables cannot be passed to Brane functions. Therefore, the schema is implented using nested arrays. The first element of each nested array specifies the variable type (currently supports `integer`, `float` and `categorical`). The second element specifies the downcast type for numerical variables (eg.: `int32`, `uint8`, `float32`, etc.) or categorical type for categorical variables (currently supports `nominal` and `ordinal`). The third element is an array of the variable names as present in the dataset. Categorical types expect a fourth element specifying the categories. It is optional for nominal variables and mandatory for ordinal variables (as it is used to derive the ordering).


Below we provide some example schemas for different data types.

```
# Pass downcast data type (single)
schema = [['integer', 'int32', ['population']]]

# Pass downcast data type (multiple, same )
schema = [['integer', 'int8', ['temperature', 'height']]]

# Pass downcast data type (multiple, different)
schema = [
            ['integer', 'int32', ['population']],
            ['float', 'float32', ['surface']]
         ]
         
# Pass categorical data type
schema = [
            ['categorical', 'nominal', ['country', 'region']],
            ['categorical', 'ordinal', ['pressure'], ['low', 'medium', 'high']]
         ]
```

The schema can simply be passed to the function as follows: 

```
> downcast("path/to/input.csv", "path/to/output_dir/", schema)
```
