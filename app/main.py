from typing import Optional
import random
import json

from fastapi import FastAPI, HTTPException

new_songs_file = open('app/data/data_new.json')
popular_songs_file = open('app/data/data_popular.json')
trending_songs_file = open('app/data/data_trending.json')

new_songs = json.load(new_songs_file)
popular_songs = json.load(popular_songs_file)
trending_songs = json.load(trending_songs_file)

all_songs = [*new_songs, *popular_songs, *trending_songs]

app = FastAPI()

MAX_PAGE_COUNT = 10

@app.get("/")
def read_root():
    return "Welcome to Musika-api"


@app.get("/song/{song_id}")
def read_song(song_id: int):
    if song_id >= len(all_songs):
        raise HTTPException(status_code=404, detail="Item not found")
    return all_songs[song_id]


@app.get("/songs/new/{page_number}")
def list_new_songs(page_number: int):
    starting_index = page_number * 10
    ending_index = (page_number + 1) * 10

    if starting_index >= len(new_songs):
        return []

    if ending_index > len(new_songs):
        ending_index = len(new_songs)

    return new_songs[starting_index:ending_index]


@app.get("/songs/popular/{page_number}")
def list_popular_songs(page_number: int):
    starting_index = page_number * 10
    ending_index = (page_number + 1) * 10

    if starting_index >= len(popular_songs):
        return []

    if ending_index > len(popular_songs):
        ending_index = len(popular_songs)

    return popular_songs[starting_index:ending_index]


@app.get("/songs/trending/{page_number}")
def list_trending_songs(page_number: int):
    starting_index = page_number * 10
    ending_index = (page_number + 1) * 10

    if starting_index >= len(trending_songs):
        return []

    if ending_index > len(trending_songs):
        ending_index = len(trending_songs)

    return trending_songs[starting_index:ending_index]

@app.get("/songs/search")
def search_songs(key_word: str):

    word = key_word.lower()

    if key_word is None or key_word == '':
        raise HTTPException(status_code=400, detail="key_word shouldn't be empty")

    results = []

    for song in all_songs:
        if word in song['name'].lower() or word in song['author'].lower() or word in song['type'].lower():
            results.append(song)

    return results