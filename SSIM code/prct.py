import pandas as pd
f = open("C:/Users/kakhi/OneDrive/Desktop/Flask/website/output.json")
cf = f.readlines()
data = [cf]
df = pd.DataFrame(data)
print(df)

