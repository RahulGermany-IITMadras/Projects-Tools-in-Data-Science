
from bs4 import BeautifulSoup
import pandas as pd

# Define file paths
file_paths = ["C:\Users\Rahul Gupta\Documents\ROE1"
]

# Initialize lists to hold the data
average_scores_math = []
percent_gte_1500 = []

# Function to extract data from HTML
def extract_data_from_html(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        cards = soup.find_all('div', class_='card-body')
        for card in cards:
            avg_score_math_tag = card.find(text="Average Score: Math:")
            percent_1500_tag = card.find(text="Percent >= 1500:")
            
            if avg_score_math_tag and percent_1500_tag:
                avg_score_math = avg_score_math_tag.find_next().text
                percent_1500 = percent_1500_tag.find_next().text.strip('%')

                if avg_score_math != 'null' and percent_1500 != 'null':
                    average_scores_math.append(float(avg_score_math))
                    percent_gte_1500.append(float(percent_1500))

# Extract data from each HTML file
for path in file_paths:
    extract_data_from_html(path)

# Create a DataFrame from the extracted data
data = pd.DataFrame({
    'Average Score: Math': average_scores_math,
    'Percent >= 1500': percent_gte_1500
})

# Calculate the Pearson correlation coefficient
pearson_corr = data.corr().iloc[0, 1]
print(pearson_corr)
from bs4 import BeautifulSoup
import pandas as pd

# Define file paths
file_paths = [
    "score-butte.html",
    "score-colusa.html",
    "score-del-norte.html",
    "score-el-dorado.html"
]

# Initialize lists to hold the data
average_scores_math = []
percent_gte_1500 = []

# Function to extract data from HTML
def extract_data_from_html(file_path):
    with open(file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')
        cards = soup.find_all('div', class_='card-body')
        for card in cards:
            avg_score_math_tag = card.find(text="Average Score: Math:")
            percent_1500_tag = card.find(text="Percent >= 1500:")
            
            if avg_score_math_tag and percent_1500_tag:
                avg_score_math = avg_score_math_tag.find_next().text
                percent_1500 = percent_1500_tag.find_next().text.strip('%')

                if avg_score_math != 'null' and percent_1500 != 'null':
                    average_scores_math.append(float(avg_score_math))
                    percent_gte_1500.append(float(percent_1500))

# Extract data from each HTML file
for path in file_paths:
    extract_data_from_html(path)

# Create a DataFrame from the extracted data
data = pd.DataFrame({
    'Average Score: Math': average_scores_math,
    'Percent >= 1500': percent_gte_1500
})

# Calculate the Pearson correlation coefficient
pearson_corr = data.corr().iloc[0, 1]
print(pearson_corr)

