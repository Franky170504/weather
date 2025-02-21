import xarray as xr
import os

ds_temp = xr.open_dataset("weather-nc\pune_temp.nc")
ds_preci = xr.open_dataset("weather-nc\pune_preci.nc")

# Convert to Pandas DataFrame
df_temp = ds_temp.to_dataframe().reset_index()
df_preci = ds_preci.to_dataframe().reset_index()

# Save as CSV
if os.path.exists("notebook\data\pune_weather_temperature.csv"):
    print("File already exists")
else:
    df_temp.to_csv("notebook\data\pune_weather_temperature.csv", index= False)

if os.path.exists("notebook\data\pune_weather_precipitation.csv"):
    print("File already exists")
else:
    df_preci.to_csv("notebook\data\pune_weather_precipitation.csv", index=False)

print(df_temp.head())
print(df_preci.head())
