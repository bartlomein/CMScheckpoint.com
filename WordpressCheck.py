# Checks the metatags of a site for WordPress
import requests
from bs4 import BeautifulSoup
import html5lib


def addHTML(url1):
    if "http" in url1:
        return url1
    else:
        return "http://" + url1


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


def checker(url):
    newurl = addHTML(url)

    try:
        r = requests.get(newurl)

        soup = BeautifulSoup(r.content, "html5lib")
        meta_check = soup.find_all('meta', attrs={'name': 'generator'})
        meta_name = soup.find_all('meta', attrs={'property': 'og:image'})
        whole_html = str(meta_name)
        soup_string = str(meta_check)
        print(meta_check)
        print(soup_string)


        if "WordPress" in soup_string:
            final_content = meta_check[0].attrs['content']
            does_it_have_version = hasNumbers(final_content)
            if does_it_have_version:
                return "Made with " + final_content
            else:
                return "Made with WordPress (unknown version)"
        elif "Drupal" in soup_string:
            return "Made with Drupal"
        elif "Joomla!" in soup_string:
            return "Made with Joomla"
        elif "squarespace" in whole_html:
            return "Made with Squarespace"
        elif "Wix" in soup_string:
            return "Made with Wix"
        else:
            return "Sorry, can't tell the CMS :("
    except requests.exceptions.MissingSchema:
        return "Error, try again"
    except requests.exceptions.ConnectionError:
        return "Error, try again"
    except requests.exceptions.InvalidURL:
        return "Error, try again"
