#tqdm means taqaddum in urdu which is nothing but progress
#desc is Prefix fot the progress bar
#ncols the width of entire output message
#ASCII if we dont specified uses unicode to fill the meter
from tqdm import tqdm
import time

for i in tqdm (range(101), desc="loading",ascii=False,ncols=75):
    time.sleep(0.01)

print("Complete")