import pickle
import warnings
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)
# Load the pickle file
with open(r'E:\amazon sambhav\mcf omniflux\backend_vania\inventory_lead_time\furniture_inventory_data\Furniture_inventory_data.pkl', 'rb') as file:
    data = pickle.load(file)

# Inspect the content
print(type(data))
print(data)