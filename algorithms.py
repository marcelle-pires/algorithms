import fire
import logging

from src.binary_search import binary_search

logging.basicConfig(format='[%(levelname)s] %(message)s', level=logging.DEBUG)

def binary_search_algorithm(list, valor):
  result = binary_search(list, valor)
  if (result is None):
    logging.info("value not found")
  else: 
    logging.info("value found - index: " + str(result)) 

if __name__ == '__main__':
  fire.Fire()
