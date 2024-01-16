import spotify_extractor.listings_adapter as adapter
from prefect import flow, task


@task
def get_playlist_tracks(playlist_id):
    return adapter.get_playlist_tracks(playlist_id)

@task
def extract_tracks_info(tracks, playlist_id):
    pass

@task
def write_to_csv(tracks):
    pass

@flow
def extract_and_write():
    playlist_id = "37i9dQZEVXbLRQDuF5jeBp"
    playlist_tracks = get_playlist_tracks(playlist_id)
    # fill in remainder of flow here
    

extract_and_write()