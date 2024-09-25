__name__

def get_book():
  with open("./books/frankenstein.txt") as f:
    book_content = f.read()
    #print(book_content)
    return book_content

def counting_words(book_content):
    words = book_content.split()
    words_count = (len(words))
    return words_count

def counting_letters(book_content):
    my_string = book_content.lower()
    lc_dict = {}

    for i in my_string:
      if i in lc_dict:
        lc_dict[i] += 1
      else:
        lc_dict[i] = 0

    return lc_dict

def sorted_on(lc_dict):
    return lc_dict["num"]

def main():
  for key, value in lc_dict.items()
    print(f"The '{key}' character was found {value} times.")

main()