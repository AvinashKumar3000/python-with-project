class Analyzer:
    def __init__(self, df):
        self.df = df

    def total_sales(self):
        return self.df['Sales'].sum()

    def sales_by_month(self):
        return self.df.groupby('Month')['Sales'].sum()

    def sales_by_product(self):
        return self.df.groupby('Product')['Sales'].sum()