import numpy as np
branches = ["Branch A","Branch B","Branch C","Branch D"]
transactions = np.array([
  [120,150,130,170,160,180],
  [200,210,190,220,205,215],
  [95,100,90,110,105,115],
  [150,160,155,165,170,175]
])
totals_per_branch = transactions.sum(axis=1)
highest_idx = totals_per_branch.argmax()
overall_avg = transactions.mean()
monthly_avg_across_branches = transactions.mean(axis=0)
reshaped = transactions.reshape(3,8)
