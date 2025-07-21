import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

weather_data={
    "Day":list(range(1,11)),
    "Temperature":[30,31,32,34,33,35,36,37,38,39]
}

df=pd.DataFrame(weather_data)
sns.set(style="whitegrid")
sns.lmplot(x="Day",y="Temperature",data=df,ci=None,order=1,aspect=1.5)
plt.title("Weather Temperature Prediction")
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
weather_data={
    'Name': ["Summer","Winter","Rainy","Authum"],
    'Score': [99, 70, 80, 95]
}
import pandas as pd
df=pd.DataFrame(weather_data)
sns.barplot(x='Name',y='Score',data=df,palette='pastel')
plt.title("Weather in countries")
plt.show()