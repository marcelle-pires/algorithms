import logging
import fire
from src.binary_search import binary_search
from src.selection_sort import selection_sort

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.INFO)

def binary_search_algorithm(list, valor):
  result = binary_search(list, valor)
  if (result is None):
    logging.info("value not found")
  else: 
    logging.info("value found - index: " + str(result)) 

def selection_sort_algorithm(list):
  result = selection_sort(list)
  logging.info("sorted list: " + str(result))

if __name__ == '__main__':
  fire.Fire()
