from bs4 import BeautifulSoup


with open("final_output.txt", "w", encoding="utf-8") as output_file:
    
    for page_number in range(1, 21):
        
        file_path = f"output_{page_number}.html"
        with open(file_path, "r", encoding="utf-8") as file:
            html_content = file.read()

        
        soup = BeautifulSoup(html_content, 'html.parser')

       
        div_elements = soup.find_all('div', class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right')

        output_file.write(f"Processed elements from page{page_number}\n")
        for div in div_elements:
            
            product_name = div.find('span', class_='a-size-medium a-color-base a-text-normal').get_text(strip=True)
            product_url = div.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href']
            full_product_url = f"https://www.amazon.in{product_url}"  
            
            
            price_element = div.find('span', class_='a-price-whole')
            price = price_element.get_text(strip=True) if price_element else "Price information not available"
            
            
            ratings_element = div.find('span', class_='a-icon-alt')
            ratings = ratings_element.get_text(strip=True) if ratings_element else "Ratings information not available"
            
            
            reviews_element = div.find('span', class_='a-size-base')
            reviews = reviews_element.get_text(strip=True) if reviews_element else "Reviews information not available"
            
           
            output_file.write("Product Name: {}\n".format(product_name))
            output_file.write("Product URL: {}\n".format(full_product_url))
            output_file.write("Price: {}\n".format(price))
            output_file.write("Ratings: {}\n".format(ratings))
            output_file.write("Number of Reviews: {}\n".format(reviews))
            output_file.write("\n")

        output_file.write("\n")
