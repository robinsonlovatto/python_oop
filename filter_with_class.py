import pandas as pd
from typing import TypeAlias

ListStr: TypeAlias = list[str]

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtered = None

    def load_csv(self):
        self.df = pd.read_csv(self.file_path)
        return self.df  # Return the DataFrame after loading

    #
    def filter_by(self, columns: ListStr, values: ListStr) -> pd.DataFrame:
        if len(columns) != len(values):
            raise ValueError("It doesn't have the same amount of columns and values.")
        
        if len(columns) == 0:
            return self.df
        
        current_column = columns[0]
        current_value = values[0]
        
        if self.df_filtered is None:
            self.df_filtered = self.df[self.df[current_column] == current_value]
        else:
            self.df_filtered = self.df_filtered[self.df_filtered[current_column] == current_value]

        if len(columns) == 1:
            return self.df_filtered
        else:
            # recursion
            return self.filter_by(columns[1:], values[1:])

if __name__ == "__main__":
    df = CsvProcessor("data/pokemon.csv")
    df.load_csv()
    
    df_filtered = df.filter_by(["Type 1","Type 2"],["Grass","Flying"])

    print(df_filtered)
