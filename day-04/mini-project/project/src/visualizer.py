
import matplotlib.pyplot as plt

class Visualizer:
    def plot_monthly_sales(self, monthly_data):
        plt.figure(figsize=(8,4))
        plt.plot(monthly_data.index, monthly_data.values)
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.title("Monthly Sales Trend")
        plt.grid(True)
        plt.show()

    def plot_product_sales(self, product_data):
        plt.figure(figsize=(8,4))
        plt.bar(product_data.index, product_data.values)
        plt.xlabel("Product")
        plt.ylabel("Sales")
        plt.title("Sales by Product")
        plt.grid(True)
        plt.show()