# ECommerce-Python-SQL

<h2>About-Target Platform/Website 🛍️: </h2>
<b>Target is a globally recognized brand and a leading retailer 🛒 in the United States, known for offering exceptional value, inspiration, innovation, and a unique shopping experience.</b>
<h2>Project Goal 🎯: </h2> 
<b>Analyzing this dataset offers valuable insights into Target's Brazilian operations, revealing details about Customer Demographics and Behavior, Sales and Order Performance, Product and Seller Performance, Business Growth and Health, High-Value Customers, pricing strategies, payment and shipping efficiency and customer satisfaction. This comprehensive dataset is a valuable resource for understanding various business aspects and enhancing strategic decision-making.<br>
☑️Analysis is done using SQL by computing Queries in python to showcase SQL knowledge and integration of SQL in python.Matplotlib is used for visualization.</b>
<h2>Tech Stack 👩‍💻: </h2>
<b>
💻Python<br>
📂SQL<br>
📊Matplotlib<br>
🐼Pandas<br></b>

<h2>File Format 📁: </h2>
<b>Main.py </b>:It is the main code file containing all sql queries to fetch from database and present them using pandas and matplotlib.<br>
<b>CSV_to_Database.py </b>: The code in this file create mysql database schema,create appropriate tables, clean columns and naming in data using pandas and save the data into database.<br>
<b>Main.ipynb </b>: same as Main file but as jupyter notebook to see output without running the code, just download it and run in jupyter environment.<br>

<h2>Data Overview ✔️:</h2>
<b>The data focuses on Target's operations in Brazil, covering 1,00,000 orders placed between 2016 and 2018. It includes detailed information on order status, pricing, payment and shipping performance, customer locations, product attributes, and customer reviews.<br>
The data is available in 7 csv files:<br></b>
<b>1. customers.csv</b><br>
<b>2. sellers.csv</b><br>
<b>3. order_items.csv</b><br>
<b>4. geolocation.csv</b><br>
<b>5. payments.csv</b><br>
<b>6. orders.csv</b><br>
<b>7. products.csv</b><br>
<br>

<img alt="CSV_File_Structure" src="https://github.com/tanmay-changade/ECommerce-Python-SQL/blob/main/CSV%20File%20Structure.png"/>

The <b>customers.csv</b> contain following features:<br>
<i>customer_id</i>: ID of the consumer who made the purchase.<br>
<i>customer_unique_id</i>: Unique ID of the consumer.<br>
<i>customer_zip_code_prefix</i>: Zip Code of consumer’s location.<br>
<i>customer_city</i>: Name of the City from where order is made.<br>
<i>customer_state</i>: State Code from where order is made (Eg. são paulo - SP).<br>

The <b>geolocations.csv</b> contain following columns:<br>
<i>geolocation_zip_code_prefix</i>: First 5 digits of Zip Code.<br>
<i>geolocation_lat</i>: Latitude.<br>
<i>geolocation_lng</i>: Longitude.<br>
<i>geolocation_city</i>: City.<br>
<i>geolocation_state</i>: State.<br>

The <b>order_items.csv</b> contain following columns:<br>
<i>order_id</i>: A Unique ID of order made by the consumers.<br>
<i>order_item_id</i>: A Unique ID given to each item ordered in the order.<br>
<i>product_id</i>: A Unique ID given to each product available on the site.<br>
<i>seller_id</i>: Unique ID of the seller registered in Target.<br>
<i>shipping_limit_date</i>: The date before which the ordered product must be shipped.<br>
<i>price</i>: Actual price of the products ordered.<br>
<i>freight_value</i>: Price rate at which a product is delivered from one point to another.<br>

The <b>orders.csv</b> contain following columns:<br>
<i>order_id</i>: A Unique ID of order made by the consumers.<br>
<i>customer_id</i>: ID of the consumer who made the purchase.<br>
<i>order_status</i>: Status of the order made i.e. delivered, shipped, etc.<br>
<i>order_purchase_timestamp</i>: Timestamp of the purchase.<br>
<i>order_delivered_carrier_date</i>: Delivery date at which carrier made the delivery.<br>
<i>order_delivered_customer_date</i>: Date at which customer got the product.<br>
<i>order_estimated_delivery_date</i>: Estimated delivery date of the products.<br>

The <b>payments.csv</b> contain following columns:<br>
<i>order_id</i>: A Unique ID of order made by the consumers.<br>
<i>payment_sequential</i>: Sequences of the payments made in case of EMI.<br>
<i>payment_type</i>: Mode of payment used (Eg. Credit Card).<br>
<i>payment_installments</i>: Number of installments in case of EMI purchase.<br>
<i>payment_value</i>: Total amount paid for the purchase order.<br>

The <b>products.csv</b> contain following columns:<br>
<i>product_id</i>: A Unique identifier for the proposed project.<br>
<i>product_category_name</i>: Name of the product category.<br>
<i>product_name_lenght</i>: Length of the string which specifies the name given to the products ordered.<br>
<i>product_description_length</i>: Length of the description written for each product ordered on the site.<br>
<i>product_photos_qty</i>: Number of photos of each product ordered available on the shopping portal.<br>
<i>product_weight_g</i>: Weight of the products ordered in gm.<br>
<i>product_length_cm</i>: Length of the products ordered in cm.<br>
<i>product_height_cm</i>: Height of the products ordered in cm.<br>
<i>product_width_cm</i>: Width of the product ordered in cm.<br>

The <b>sellers.csv</b> contains following columns:<br>
<i>seller_id</i>: Unique ID of the seller registered.<br>
<i>seller_zip_code_prefix</i>: Zip Code of the seller’s location.<br>
<i>seller_city</i>: Name of the City of the seller.<br>
<i>seller_state</i>: State Code (Eg. são paulo - SP).<br>

<b>Dataset Link </b> 🔗: https://www.kaggle.com/datasets/devarajv88/target-dataset?select=products.csv

