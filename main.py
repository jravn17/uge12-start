# main.py

import plots

def main():
    # Create sales plot
    plots.create_sales_plot()
    
    # Create sales by category plot
    plots.create_sales_by_category_plot()
    
    #Create sales by employee plot
    plots.create_sales_by_employee_plot()
    
    # Create average order value per customer plot
    plots.create_avg_order_value_per_customer_plot()
    
    
    

if __name__ == "__main__":
    main()
