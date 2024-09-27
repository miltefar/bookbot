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
    my_dict = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lc_dict = {}

    for char in my_string:
      if char in my_dict.i == True and lc_dict.i > 0:
          lc_dict.i += 1
      elif i in my_dict.i == True and lc_dict.i == 0:
          lc_dict.i = 1

    return lc_dict

def sorted_on(lc_dict):
    sorted_dict = dict(sorted(lc_dict.items(), key =lambda item: item[1], reverse = True))
    return sorted_dict

def main():
  #print("--- Begin report of books/frankenstein.txt ---")
  #for key, value in lc_dict.items()
  #  print(f"The '{key}' character was found {value} times.")
  get_book()
  print(sorted_on(counting_letters(get_book())))
main()