import xarray as xr
import os

ds_hr_temp = xr.open_dataset(r"hourly_temp.nc")

df_hr_temp = ds_hr_temp.to_dataframe().reset_index()

if os.path.exists(r"notebook\data\hr_max_temperature.csv"):
    print("Hourly Max Tempreture File already exists")
else:
    df_hr_temp.to_csv(r"notebook\data\hr_max_temperature.csv", index= False)
    print("Hourly Max Tempreture File created")