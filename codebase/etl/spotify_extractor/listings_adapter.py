import os
from datetime import date

import pandas as pd


def get_playlist_tracks(playlist_id):
    pass

def extract_tracks_info(tracks, playlist_id):
    pass

def write_to_csv(tracks):
    folder_path = "./data/"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    tracks_df = pd.DataFrame(tracks)
    data_path = "./data/track_listings.csv"
    tracks_df.to_csv(data_path)