import pandas as pd
from typing import List
from dataclasses import dataclass

@dataclass
class Coordinate:
    latitude: float
    longitude: float

@dataclass
class Restaurant:
    name: str
    year: int
    city: str
    region: str
    cuisine: str
    price: str
    stars: int
    location: Coordinate

def load_restaurants(filepath: str) -> List[Restaurant]:
    df = pd.read_csv(filepath)

    df = df.dropna(subset=['latitude', 'longitude']).copy()
    df['stars'] = df['stars'].fillna(0).astype(int)
    df['price'] = df['price'].fillna('$')
    df['cuisine'] = df['cuisine'].fillna('Unknown')

    df['year'] = pd.to_numeric(df['year'], errors='coerce').fillna(0).astype(int)
    df['name'] = df['name'].fillna('Unnamed')
    df['city'] = df['city'].fillna('Unknown')

    restaurants = []
    for _, row in df.iterrows():
        coord = Coordinate(latitude=row['latitude'], longitude=row['longitude'])
        r = Restaurant(
            name=row['name'],
            year=row['year'],
            city=row['city'],
            region=row['region'],
            cuisine=row['cuisine'],
            price=row['price'],
            stars=row['stars'],
            location=coord
        )
        restaurants.append(r)
    return restaurants

def restaurants_for_cuisine(restaurants: List[Restaurant], cuisine: str) -> List[Restaurant]:
    return [r for r in restaurants if r.cuisine.lower() == cuisine.lower()]

def restaurants_for_star(restaurants: List[Restaurant], star: int) -> List[Restaurant]:
    return [r for r in restaurants if r.stars == star]

def restaurants_for_city(restaurants: List[Restaurant], city: str) -> List[Restaurant]:
    return [r for r in restaurants if city.lower() in r.city.lower()]

def gothenburg_michelins(restaurants: List[Restaurant]) -> List[Restaurant]:
    return [r for r in restaurants if r.city.lower() == 'gothenburg']
