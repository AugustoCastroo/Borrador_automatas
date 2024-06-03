from dataclasses import dataclass

GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

@dataclass
class SongDto:
    index: int
    artist: str
    url_spotify: str
    track: str
    album: str
    album_type: str
    uri: str
    danceability: float
    energy: float
    key: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration: float
    url_youtube: str
    youtube_video_title: str
    youtube_channel: str
    youtube_views: float
    youtube_likes: float
    comments:  float
    licensed: bool
    official_video: bool
    stream: float