import pandas as pd
from SQLSTUFF.ConnectToDatabase import ConnectToDatabase

def get_TotalPrice_OrderID():
    try:
        # Connect to the database
        database = ConnectToDatabase.connect_to_database()

        # SQL query to join the two tables and select relevant columns
        query = """
            SELECT 
                orders.ShipCountry,
                orderdetails.UnitPrice * orderdetails.Quantity AS TotalPrice
            FROM 
                orders
            INNER JOIN 
                orderdetails ON orders.OrderID = orderdetails.OrderID
        """

        # Execute the query and fetch the results
        df = pd.read_sql(query, database)

        # Close the database connection
        database.close()

        return df

    except Exception as e:
        print(f"Error preparing data: {e}")
        return None

def get_sales_by_category_data():
    try:
        # Opret forbindelse til databasen
        db = ConnectToDatabase.connect_to_database()

        # SQL-forespørgsel for at få salget opdelt efter produktkategorier
        query = """
            SELECT 
                c.CategoryName,
                SUM(od.UnitPrice * od.Quantity) AS TotalSales
            FROM 
                Categories c
            INNER JOIN 
                Products p ON c.CategoryID = p.CategoryID
            INNER JOIN 
                OrderDetails od ON p.ProductID = od.ProductID
            GROUP BY 
                c.CategoryName
        """

        # Udfør forespørgslen og hent dataene
        cursor = db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()

        # Luk cursor
        cursor.close()

        # Konverter dataene til en pandas DataFrame
        df = pd.DataFrame(data, columns=['CategoryName', 'TotalSales'])

        return df

    except Exception as e:
        print(f"Error getting sales by category data: {e}")
        return None
    
def get_sales_by_employee_data():
    try:
        # Connect to the database
        database = ConnectToDatabase.connect_to_database()

        # SQL query to get sales by employee
        query = """
            SELECT 
                CONCAT(e.FirstName, ' ', e.LastName) AS EmployeeName,
                SUM(od.UnitPrice * od.Quantity) AS TotalSales
            FROM 
                Employees e
            INNER JOIN 
                Orders o ON e.EmployeeID = o.EmployeeID
            INNER JOIN 
                OrderDetails od ON o.OrderID = od.OrderID
            GROUP BY 
                EmployeeName
        """

        # Execute the query and fetch the results
        df = pd.read_sql(query, database)

        # Close the database connection
        database.close()

        return df

    except Exception as e:
        print(f"Error getting sales by employee data: {e}")
        return None

def get_order_data():
    try:
        # Connect to the database
        database = ConnectToDatabase.connect_to_database()

        # SQL query to select order status from orders table
        query = """
            SELECT OrderStatus
            FROM Orders
        """

        # Execute the query and fetch the results
        df = pd.read_sql(query, database)

        # Close the database connection
        database.close()

        return df

    except Exception as e:
        print(f"Error getting order data: {e}")
        return None
    
def average_order_value_per_customer():
    try:
        # Opret forbindelse til databasen
        db = ConnectToDatabase.connect_to_database()

        # SQL-forespørgsel for at beregne den gennemsnitlige ordreværdi pr. kunde
        query = """
            SELECT 
                CONCAT(Customers.ContactName, ' (', Customers.CompanyName, ')') AS CustomerName,
                AVG(Orderdetails.UnitPrice * Orderdetails.Quantity) AS AvgOrderValue
            FROM 
                Orders
            INNER JOIN 
                Orderdetails ON Orders.OrderID = Orderdetails.OrderID
            INNER JOIN 
                Customers ON Orders.CustomerID = Customers.CustomerID
            GROUP BY 
                CustomerName
        """

        # Udfør forespørgslen og hent resultaterne
        cursor = db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        
        # Luk cursor
        cursor.close()

        # Luk ikke forbindelsen her

        # Konverter til en pandas DataFrame
        df = pd.DataFrame(data, columns=['CustomerName', 'AvgOrderValue'])

        return df

    except Exception as e:
        print(f"Error calculating average order value per customer: {e}")
        return None

