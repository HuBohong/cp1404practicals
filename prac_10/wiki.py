import wikipedia
from wikipedia import PageError, DisambiguationError


def main():
    """wiki API practice"""
    page_title = input("Enter a page title").strip()
    while page_title:
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(page.content)
        except DisambiguationError as de:
            print("We need a more specific title. Try one of the following:")
            print(de.options[:5])



        page_title = input("Enter a page title").strip()


main()