import pandas as pd
import numpy as np

def format_submission(predictions):
	  predictions = np.round([p[1] for p in predictions], 1)
	  test_id = range(0, len(predictions))
	  d = {'test_id': test_id, 'is_female': predictions}
	  df = pd.DataFrame(d)
	  df = df[['test_id', 'is_female']]
	  return df
