import matplotlib.pyplot as plt
import seaborn as sns

def plot_category_sales(df):
    sales=df.groupby('Category')['Sales'].sum().sort_values()
    sales.plot(kind='bar')
    plt.title('Sales by Category')
    plt.show()
