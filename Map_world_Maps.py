# import the necessary packages
import matplotlib.pyplot as plt
import geopandas as gpd
import contextily as ctx

# Path to the dataset
url = 'Natural_Earth_quick_start/10m_cultural/ne_10m_admin_0_countries.shp'

# Load the dataset
world = gpd.read_file(url)

# Load the dataset
world = gpd.read_file(url)

# Load the dataset
world = gpd.read_file(url)

# Print the first few rows of the dataset to inspect column names
print(world.head())
print(world.columns)

# Check for the correct column names
if 'CONTINENT' in world.columns:
    continent_col = 'CONTINENT'
elif 'continent' in world.columns:
    continent_col = 'continent'
else:
    raise ValueError("The dataset does not contain a 'continent' or 'CONTINENT' column")

if 'NAME' in world.columns:
    name_col = 'NAME'
elif 'name' in world.columns:
    name_col = 'name'
else:
    raise ValueError("The dataset does not contain a 'name' or 'NAME' column")

# grab all African countries
africa = world[world[continent_col] == "Africa"]

# plot a basic map of Africa with a basemap
fig, ax = plt.subplots(figsize=(20, 10))

# Plot the countries
africa.to_crs(epsg=3857).plot(
    ax=ax,
    cmap="Pastel1",
    edgecolor="black",
    alpha=0.5
)

# Add basemap using contextily
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# turn off axis ticks
ax.set_xticks([])
ax.set_yticks([])

# set the plot title
plt.title("Map of Africa with Basemap and GeoPandas")
plt.show()

# grab all African countries
europe = world[world[continent_col] == "Europe"]

# plot a basic map of Europe with a basemap
fig, ax = plt.subplots(figsize=(20, 10))

# Plot the countries
europe.to_crs(epsg=3857).plot(
    ax=ax,
    cmap="Pastel1",
    edgecolor="black",
    alpha=0.5
)

# Add basemap using contextily
ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

# turn off axis ticks
ax.set_xticks([])
ax.set_yticks([])

# set the plot title
plt.title("Map of Europe with Basemap and GeoPandas")
plt.show()
