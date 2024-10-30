import requests
# https://www.google.com.ua/?hl=uk
url = "https://www.google.com.ua/?hl=uk" #
response = requests.get(url)
print(response.text)