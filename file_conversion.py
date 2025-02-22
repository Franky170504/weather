import xarray as xr
import os

ds_temp = xr.open_dataset("weather-nc\_temperature.nc")
ds_vol_soil_water_l1 = xr.open_dataset("weather-nc\_volumetric_soil_water_layer_1.nc")
ds_preci = xr.open_dataset("weather-nc\precipitation.nc")
ds_sea_surface_temp = xr.open_dataset("weather-nc\sea_surface_temperature.nc")
ds_soil_temp_l1 = xr.open_dataset("weather-nc\soil_temperature_level_1.nc")
ds_soil_type = xr.open_dataset("weather-nc\soil_type.nc")
ds_surface_pressure = xr.open_dataset("weather-nc\surface_pressure.nc")

# Convert to Pandas DataFrame
df_temp = ds_temp.to_dataframe().reset_index()
df_vol_soil_water_l1 = ds_vol_soil_water_l1.to_dataframe().reset_index()
df_preci = ds_preci.to_dataframe().reset_index()
df_sea_surface_temp = ds_sea_surface_temp.to_dataframe().reset_index()
df_soil_temp_l1 = ds_soil_temp_l1.to_dataframe().reset_index()
df_soil_type = ds_soil_type.to_dataframe().reset_index()
df_surface_pressure = ds_surface_pressure.to_dataframe().reset_index()


# Save as CSV
if os.path.exists("notebook\data\_temperature.csv"):
    print("Tempreture File already exists")
else:
    df_temp.to_csv("notebook\data\_temperature.csv", index= False)
    print("Tempreture File created")

if os.path.exists("notebook\data\_volumetric_soil_water_layer_1.csv"):
    print("Soil Water Layer 1 File already exists")
else:
    df_vol_soil_water_l1.to_csv("notebook\data\_volumetric_soil_water_layer_1.csv", index= False)
    print("Soil Water Layer 1 File created")

if os.path.exists("notebook\data\precipitation.csv"):
    print("Precipitation File already exists")
else:
    df_preci.to_csv("notebook\data\precipitation.csv", index=False)
    print("Precipitation File created")

if os.path.exists("notebook\data\sea_surface_temperature.csv"):
    print("Sea Surface Temperature File already exists")
else:
    df_sea_surface_temp.to_csv("notebook\data\sea_surface_temperature.csv", index=False)
    print("Sea Surface Temperature File created")

if os.path.exists("notebook\data\soil_temperature_level_1.csv"):
    print("Soil Temperature Level 1 File already exists")
else:
    df_soil_temp_l1.to_csv("notebook\data\soil_temperature_level_1.csv", index=False)
    print("Soil Temperature Level 1 File created")

if os.path.exists("notebook\data\soil_type.csv"):
    print("Soil Type File already exists")
else:
    df_soil_type.to_csv("notebook\data\soil_type.csv", index=False)
    print("Soil Type File created")

if os.path.exists("notebook\data\surface_pressure.csv"):
    print("Surface Pressure File already exists")
else:
    df_surface_pressure.to_csv("notebook\data\surface_pressure.csv", index=False)
    print("Surface Pressure File created")

