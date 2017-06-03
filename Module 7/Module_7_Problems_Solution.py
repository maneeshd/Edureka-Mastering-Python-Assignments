"""
@author: Maneesh D
@date: 04-Jun-17
@intepreter: Python 3.6
"""
import matplotlib.pyplot as plt
import pandas as pd


def load_dataset():
    df = pd.read_csv("data.csv")
    return df


def add_change_column(df: pd.DataFrame):
    open_series = df.Open
    close_series = df.Close
    change_series = close_series.subtract(open_series)
    df["Change"] = change_series
    print("Dataset loaded into DataFrame and Change column added....")
    print(df.head())
    return df


def get_rolling_average(df):
    ravg = df["Adj Close"].rolling(window=40).mean()
    print("\nLast 10 Moving Average values: ")
    print(ravg[-10:])
    return ravg


def plot_graph(my_df):
    my_df.plot()
    plt.show()


# Load data from CSV
data_frame = load_dataset()

# Add Change column
data_frame = add_change_column(data_frame)

# Calculate "Moving Average" on Adj Close
mavg = get_rolling_average(data_frame)

# Plot Adj Close and mavg on graph.
plot_graph(pd.DataFrame({"Adj_close": data_frame["Adj Close"], "mavg": mavg}))
