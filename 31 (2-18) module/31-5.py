import requests
import re


if __name__ == '__main__':
    my_request = requests.get('http://www.columbia.edu/~fdc/sample.html')

    date_list = re.findall(r'<h3.*>(.*)</h3>', my_request.text)
    print(date_list)
