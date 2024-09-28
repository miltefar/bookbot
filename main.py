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

    for char in my_string:

      if char.isalpha():
          
          if char in lc_dict:

            lc_dict[char] += 1
          else:
            lc_dict[char] = 1

    return lc_dict

def sorted_on(lc_dict):
    sorted_dict = dict(sorted(lc_dict.items(), key =lambda item: item[1], reverse = True))
    return sorted_dict

def main():

  get_book()
  dictionary = sorted_on(counting_letters(get_book()))
  print("--- Begin report of books/frankenstein.txt ---")
  for key in dictionary :
    value = dictionary[key]
    print(f"The '{key}' character was found {value} times.")

  print("--- End report ---")

main()