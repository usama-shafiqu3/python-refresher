"""                                   Python Refresher-0.1                  """
import os
from DATA import CL_DATA
from Decorator import Header

main_data = CL_DATA
dsply = Header
main_data.welcome_note('self')

os.system('cls')

main_data.dsply_data('self')

dsply.info('self')

dsply.data_time('self')