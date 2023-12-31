# Selenium Web Scraping with BeautifulSoup

This is a Python script that demonstrates web scraping using the Selenium and BeautifulSoup libraries. It extracts product information from a specific page on Flipkart and stores it in a CSV file. The script uses the Microsoft Edge WebDriver for automation.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- Python (https://www.python.org/downloads/)
- Selenium (https://selenium-python.readthedocs.io/)
- BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- Microsoft Edge WebDriver (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Installation

You can install the required Python libraries using pip:

```bash
pip install selenium beautifulsoup4 pandas
```

Download and install the Microsoft Edge WebDriver suitable for your system from the provided link.

## Usage

1. Replace the WebDriver path with the path to your Microsoft Edge WebDriver. The code to change is:

   ```python
   driver = webdriver.Edge()  # Replace with your WebDriver path
   ```

2. Change the URL in the `driver.get()` method to the Flipkart page you want to scrape.

3. Run the script using Python:

   ```bash
   python flipkart_scraper.py
   ```

## Output

The script will scrape the product names, prices, and ratings (if available) from the specified Flipkart page. The data will be stored in a CSV file named `product1.csv`. Each row in the CSV file represents a product with columns for Product Name, Price, and Rating.

## Example

Here's an example Flipkart URL you can use for scraping gaming laptops:

```python
driver.get('https://www.flipkart.com/6bo/b5g/~cs-hbtuge4qub/pr?sid=6bo%2Cb5g&collection-tab-name=Gaming&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkdhbWluZyBMYXB0b3BzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=26.productCard.PMU_V2_5')
```

## Example output

| ASUS TUF Gaming F15 Core i5 10th Gen 10200H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA Ge... | "₹58,550"   | 4.4 |
|-----------------------------------------------------------------------------------------------------------|-------------|-----|
| DELL G15 Core i5 12th Gen 12500H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeForce RTX ... | "₹72,990"   | 4.2 |
| Lenovo IdeaPad Gaming 3 Intel Core i5 11th Gen 11320H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics... | "₹53,990"   | 4.3 |
| HP Victus Core i5 12th Gen 12450H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeForce GTX ... | "₹63,990"   | 4.2 |
| Lenovo Ideapad Gaming 3 AMD Ryzen 5 Hexa Core 5600H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/N... | "₹53,990"   | 4.3 |
| Lenovo IdeaPad Gaming 3 Ryzen 7 Octa Core AMD R7-5800H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphi... | "₹75,343"   | 4.3 |
| MSI Core i7 13th Gen 13620H - (16 GB/1 TB SSD/Windows 11 Home/8 GB Graphics/NVIDIA GeForce RTX 4060) K... | "₹1,35,990" | 4.2 |
| Acer Aspire 7 Core i5 10th Gen - (8 GB/512 GB SSD/Windows 10 Home/4 GB Graphics/NVIDIA GeForce GTX 165... | "₹52,500"   | 4.4 |
| DELL Alienware Core i5 12th Gen 12500H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeForc... | "₹1,54,990" | N/A |
| ASUS ROG Strix G15 (2022) with 90Whr Battery Ryzen 7 Octa Core AMD R7-6800H - (16 GB/1 TB SSD/Windows ... | "₹1,14,990" | 4.5 |
| Acer Aspire 7 Core i5 12th Gen 1240P - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeForce R... | "₹65,990"   | 4.2 |
| Lenovo IdeaPad Gaming 3 Intel Core i5 11th Gen 11300H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics... | "₹55,990"   | 4.3 |
| ASUS Vivobook Pro 15 Ryzen 7 Octa Core AMD R7-4800H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/... | "₹63,990"   | 4.4 |
| Lenovo IdeaPad Gaming 3 Intel Core i5 11th Gen 11300H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics... | "₹62,990"   | 4.3 |
| ASUS TUF Gaming A15 Ryzen 5 Hexa Core AMD R5-4600H - (8 GB/1 TB SSD/Windows 11 Home/4 GB Graphics/NVID... | "₹63,000"   | 4.3 |
| MSI Katana GF66 Core i7 11th Gen 11800H - (16 GB/512 GB SSD/Windows 10 Home/6 GB Graphics/NVIDIA GeFor... | "₹85,900"   | 4.4 |
| HP Victus Core i7 12th Gen 12650H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeForce RTX ... | "₹87,599"   | 4.3 |
| Lenovo IdeaPad Gaming 3 Ryzen 7 Octa Core AMD R7-5800H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphic... | "₹71,990"   | 4.5 |
| DELL Ryzen 5 Hexa Core AMD R5-6600H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeForce R... | "₹73,990"   | 4   |
| HP Pavilion Gaming Ryzen 7 Octa Core AMD R7-5800H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NV... | "₹79,800"   | 4.4 |
| Ultimus Lite Celeron Dual Core N4020 - (4 GB/128 GB SSD/Windows 11 Home) NU14U4INC43BN-SG Thin and Lig... | "₹13,990"   | 3.6 |
| ASUS Chromebook Celeron Dual Core N4020 - (4 GB/64 GB EMMC Storage/Chrome OS) CX1101CMA_ID-GJ0002 / CX... | "₹13,990"   | 3.6 |
| Lenovo IdeaPad Gaming 3 Ryzen 5 Hexa Core AMD R5-5600H - (16 GB/512 GB SSD/Windows 11 Home/4 GB Graphi... | "₹68,990"   | 4.3 |
| DELL Core i5 11th Gen 11260H - (8 GB/512 GB SSD/Windows 11 Home/4 GB Graphics/NVIDIA GeForce RTX 3050)... | "₹65,990"   | 4.1 |
