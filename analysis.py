import pandas as pd
import folium
from Util import load_restaurants
from graph import histogram_plot, line_plot
import pandas as pd
import matplotlib.pyplot as plt

# 1. Top 10 regions
def plot_top_regions(restaurants):
    df = pd.DataFrame([r.__dict__ for r in restaurants])
    region_counts = df['region'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    region_counts.plot(kind='bar')
    plt.title("Top 10 Regions with Most Michelin Restaurants")
    plt.xlabel("Region")
    plt.ylabel("Count")

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


# 2. By Nordic country
def plot_nordic_histogram(restaurants):
    nordic = ['Sweden','Norway','Iceland','Denmark','Finland']
    regs = [r.region for r in restaurants if r.region in nordic]
    histogram_plot(
        x_data=regs,
        bins=len(nordic),
        title="Michelin Restaurants in Nordic Countries",
        x_label="Country",
        y_label="Count"
    )

# 3. Star distribution in Sweden
def plot_swedish_stars(restaurants):
    df = pd.DataFrame([r.__dict__ for r in restaurants])
    df = df[df['region'] == 'Sweden']
    stars_counts = df['stars'].value_counts().sort_index()

    plt.figure(figsize=(6, 4))
    ax = stars_counts.plot(kind='bar')
    plt.title("Sweden: Michelin Stars Distribution")
    plt.xlabel("Stars")
    plt.ylabel("Number of Restaurants")

    ax.set_xticklabels(['1', '2', '3'])
    plt.tight_layout()
    plt.show()

# 4. Cuisine distribution in Sweden
def plot_swedish_cuisine(restaurants):
    import pandas as pd
    df = pd.DataFrame([r.__dict__ for r in restaurants])
    df = df[df['region']=='Sweden']
    histogram_plot(
        x_data=df['cuisine'],
        bins=10,
        title="Cuisine Types in Sweden",
        x_label="Cuisine",
        y_label="Count"
    )

# 5. Global cuisine distribution
def plot_global_cuisine(restaurants):
    df = pd.DataFrame([r.__dict__ for r in restaurants])
    cuisine_counts = df['cuisine'].value_counts().head(20)

    plt.figure(figsize=(12, 6))
    cuisine_counts.plot(kind='bar')
    plt.title("Top 20 Cuisines Worldwide")
    plt.xlabel("Cuisine")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# 6. Map all restaurants
def plot_map(restaurants):
    m = folium.Map(location=[59, 20], zoom_start=4)
    for r in restaurants:
        folium.CircleMarker(
            location=[r.location.latitude, r.location.longitude],
            radius=5 + r.stars,
            popup=f"{r.name} ({r.stars}⭐)",
            color='blue',
            fill=True
        ).add_to(m)
    return m

# 7. Price category line chart

def plot_price_category(restaurants):
    df = pd.DataFrame([r.__dict__ for r in restaurants])
    def categorize_price(p):
        if p in ["$", "$$"]:
            return "Plus"
        if p in ["$$$", "$$$$"]:
            return "Premium"
        if p == "$$$$$":
            return "Premium Plus"
        return "Unknown"
    df['category'] = df['price'].apply(categorize_price)
    grouped = df.groupby(['category', 'stars']).size().unstack(fill_value=0)
    if grouped.empty:
        print("⚠️ No data to plot price categories.")
        return
    line_plot(
        df=grouped,
        title="Michelin Restaurants per Price Category by Star",
        x_label="Price Category",
        y_label="Number of Restaurants"
    )
