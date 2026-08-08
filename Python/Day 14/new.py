import pandas as pd

data = {
    "Name": ["Daksh", "Rahul", "Aman"],
    "Age": [21, 20, 22],
    "Course": ["CSE", "AIML", "CSE"]
}

df = pd.DataFrame(data)

print(df)