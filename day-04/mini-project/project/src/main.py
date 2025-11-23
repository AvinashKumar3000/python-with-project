from data_loader import DataLoader
from analyzer import Analyzer
from visualizer import Visualizer


def main():
    loader = DataLoader("../data/sales.csv")
    df = loader.load_data()

    if df is None:
        return

    analyzer = Analyzer(df)

    print("Total Sales:", analyzer.total_sales())

    monthly = analyzer.sales_by_month()
    print("\nSales by Month:\n", monthly)

    product = analyzer.sales_by_product()
    print("\nSales by Product:\n", product)

    viz = Visualizer()
    viz.plot_monthly_sales(monthly)
    viz.plot_product_sales(product)


if __name__ == "__main__":
    main()