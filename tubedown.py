from pytube import Playlist, YouTube
import os

def download_youtube_playlist(playlist_url, download_path='downloads'):
    """
    Downloads all videos from a YouTube playlist to the specified folder.

    :param playlist_url: URL of the YouTube playlist
    :param download_path: Path where videos will be downloaded
    """
    try:
        # Initialize the playlist
        playlist = Playlist(playlist_url)

        # Create the download directory if it doesn't exist
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        print(f"Downloading playlist: {playlist.title}")
        print(f"Number of videos: {len(playlist.video_urls)}")

        for idx, video_url in enumerate(playlist.video_urls, start=1):
            try:
                yt = YouTube(video_url)
                stream = yt.streams.get_highest_resolution()  # Select highest resolution
                print(f"Downloading ({idx}/{len(playlist.video_urls)}): {yt.title}")
                stream.download(output_path=download_path)
                print(f"Downloaded: {yt.title}\n")
            except Exception as e:
                print(f"Failed to download video: {video_url}\nError: {e}\n")
        
        print("Playlist download completed.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_folder = input("Enter the download folder path (default: 'downloads'): ").strip() or 'downloads'
    download_youtube_playlist(playlist_url, download_folder)
