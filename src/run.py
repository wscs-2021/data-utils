#!/usr/bin/env python3

import os
import sys

import yaml

from optimiser import Optimiser


def downcast(input_path, output_dir, schema=None):
  optimiser = Optimiser(
      input_path=input_path,
      output_dir=output_dir,
      schema=schema,
  )
  saved_space: str = optimiser.downcast_df()
  return saved_space


if __name__ == "__main__":
  # Branified
  command = sys.argv[1]
  input_path = os.environ["INPUTPATH"]
  output_dir = os.environ["OUTPUTDIR"]

  # Non-Brane
  # command = "downcast"
  # input_path = '../data/penguins.csv'
  # output_dir = '../data/'

  # Example schema
  schema = [
    ['categorical', 'nominal', ['species', 'island', 'sex'], [
        ['Adelie', 'Chinstrap', 'Gentoo'], ['Biscoe', 'Dream', 'Torgersen'], ['MALE', 'FEMALE']]
     ]
  ]

  functions = {
    "downcast": downcast,
  }
  output = functions[command](input_path, output_dir, schema)
  print(yaml.dump({"output": output}))
