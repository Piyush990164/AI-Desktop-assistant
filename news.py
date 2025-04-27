import requests
from output_module import output
from internet import check_internet_connection

def get_news():
    if check_internet_connection():
        # News API URL for top headlines
        main_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=aa2faf6587664974aa69ccbd4fd654bb"
        
        # Fetch the news
        open_bbc_page = requests.get(main_url).json()
        articles = open_bbc_page["articles"]
        results = []
        
        # Collect news titles
        for ar in articles:
            results.append(ar["title"])

        # Output the top 5 news
        for i in range(len(results)):
            output(f"{i + 1}. {results[i]}")

        return "So these were the top news from today. Hope you liked it."
    
    else:
        return "No internet connection. Please check your connection and try again."
