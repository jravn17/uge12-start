from data_manipulator import get_sales_by_category_data,get_TotalPrice_OrderID, get_sales_by_employee_data, average_order_value_per_customer
import matplotlib.pyplot as plt

def create_sales_plot():
    try:
        # Prepare data
        df= get_TotalPrice_OrderID()

        if df is not None:
            # Group data by country and calculate total sales
            sales_by_country = df.groupby('ShipCountry')['TotalPrice'].sum().reset_index()

            # Plot sales by country
            plt.figure(figsize=(10, 6))
            plt.bar(sales_by_country['ShipCountry'], sales_by_country['TotalPrice'])
            plt.xlabel('Country')
            plt.ylabel('Total Sales')
            plt.title('Total Sales by Country')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Save the plot as a file in the 'plots' folder with the desired name
            plt.savefig('plots/sales_plot.png')
            
            # Show the plot
            plt.show()

    except Exception as e:
        print(f"Error creating sales plot: {e}")

def create_sales_by_category_plot():  # Removed the argument from here
    try:
        # Get the data for sales distribution by category
        df = get_sales_by_category_data()

        if df is not None:
            # Create bar plot
            plt.figure(figsize=(10, 6))
            plt.bar(df['CategoryName'], df['TotalSales'])
            plt.xlabel('Category')
            plt.ylabel('Total Sales')
            plt.title('Total Sales by Category')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Save the plot as a file in the 'plots' folder with the desired name
            plt.savefig('plots/category_plot.png')

            # Show the plot
            plt.show()

    except Exception as e:
        print(f"Error creating sales by category plot: {e}")

def create_sales_by_employee_plot():
    try:
        # Get the data for sales by employee
        df = get_sales_by_employee_data()

        if df is not None:
            # Create bar plot
            plt.figure(figsize=(10, 6))
            plt.bar(df['EmployeeName'], df['TotalSales'])
            plt.xlabel('Employee')
            plt.ylabel('Total Sales')
            plt.title('Total Sales by Employee')
            plt.xticks(rotation=45)
            plt.tight_layout()
            
            # Save the plot as a file in the 'plots' folder with the desired name
            plt.savefig('plots/employee_sales_plot.png')

            # Show the plot
            plt.show()

    except Exception as e:
        print(f"Error creating sales by employee plot: {e}")
        


def create_avg_order_value_per_customer_plot(top_n_customers=10):
    try:
        # Hent data om den gennemsnitlige ordreværdi pr. kunde
        data = average_order_value_per_customer()

        # Check om data er tilgængelig
        if data is not None and not data.empty:
            # Sorter data efter gennemsnitlig ordreværdi i faldende rækkefølge
            data_sorted = data.sort_values(by='AvgOrderValue', ascending=False)

            # Begræns data til de øverste N kunder
            data_top_n = data_sorted.head(top_n_customers)

            # Plot søjlediagram
            plt.figure(figsize=(10, 6))
            plt.bar(data_top_n['CustomerName'], data_top_n['AvgOrderValue'])
            plt.xlabel('Customer Name')
            plt.ylabel('Average Order Value')
            plt.title('Top {} Customers by Average Order Value'.format(top_n_customers))
            plt.xticks(rotation=45)
            plt.tight_layout()

            plt.savefig('plots/avg_customer_order_plot.png')
            
            # Vis plottet
            plt.show()
        else:
            print("No data available to create plot.")

    except Exception as e:
        print(f"Error creating average order value per customer plot: {e}")

