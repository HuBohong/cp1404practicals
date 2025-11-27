import wikipedia
from wikipedia import PageError, DisambiguationError


def main():
    """wiki API practice"""
    page_title = input("Enter a page title: ").strip()
    while page_title:
        try:
            page = wikipedia.page(page_title, auto_suggest=False)
            print(page.title)
            print(page.summary[:398], end="")
            print(page.url)
        except DisambiguationError as de:
            print("We need a more specific title. Try one of the following:")
            print(de.options[:5])
        except PageError:
            print(f'Page id "{page_title}" does not match any pages. Try another id!')

        page_title = input("Enter a page title: ").strip()

    print("Thank you.")


main()
