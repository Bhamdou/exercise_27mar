import pandas as pd
import matplotlib.pyplot as plt

def read_sales_data(file_path):
    df = pd.read_csv(file_path)
    return df

def analyze_sales_data(df):
    product_summary = df.groupby('Product').agg({'Revenue': ['sum', 'mean']})
    product_summary.columns = ['Total Revenue', 'Average Revenue']
    return product_summary

def visualize_sales_data(df):
    ax = df.plot.bar(y='Revenue', x='Date', rot=45, subplots=True, legend=False)
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.title('Daily Sales Revenue')
    plt.show()

def main():
    sales_data_file = 'sales_data.csv'
    sales_data = read_sales_data(sales_data_file)

    print("Sales Data:")
    print(sales_data)
    print('-' * 40)

    product_summary = analyze_sales_data(sales_data)
    print("Product Summary:")
    print(product_summary)

    visualize_sales_data(sales_data)

if __name__ == "__main__":
    main()
