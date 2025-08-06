import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df =pd.read_csv(
    r"C:\Users\Gandhi Ji\Downloads\Unemployment_Rate_upto_11_2020.csv",
)


df.columns = df.columns.str.strip()

print("Column names:", df.columns.tolist())

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df = df.dropna(subset=['Date', 'Estimated Unemployment Rate (%)', 'Region'])


plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Estimated Unemployment Rate (%)', data=df, hue='Region')
plt.title('Unemployment Rate Over Time by Region')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()