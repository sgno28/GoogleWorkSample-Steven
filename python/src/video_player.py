"""A video player class."""

from .video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()

    live_video = None
    paused_video = None
    playlist_dict = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")

        for v in sorted(self._video_library.get_all_videos(), key=lambda x: x.title):
            tag = str(v.tags)[1:-1].replace(",", "").replace("'", "")
            print(v.title + " (" + v.video_id + ")" + " [" + tag + "]")
        # use regex

    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        video_id_array = []
        for v in self._video_library.get_all_videos():
            video_id_array.append(v.video_id)

        if video_id not in video_id_array:
            print("Cannot play video: Video does not exist!")
            return

        if self.live_video is not None:
            print("Stopping video:", self.live_video.title)

        self.live_video = self._video_library.get_video(video_id)

        print("Playing video:", self.live_video.title)

        self.paused_video = None

    def stop_video(self):
        """Stops the current video."""

        if self.live_video is None:
            print("Cannot stop video: No video is currently playing")
            return

        print("Stopping video:", self.live_video.title)
        self.live_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        import random

        video_id_array = []

        for v in self._video_library.get_all_videos():
            video_id_array.append(v.video_id)

        random_video_id = random.choice(video_id_array)

        self.play_video(random_video_id)

    def pause_video(self):
        """Pauses the current video."""

        if self.live_video is None:
            print("Cannot pause video: No video is currently playing")
            return

        if self.paused_video is not None:
            print("Video already paused:", self.paused_video.title)
        else:
            self.paused_video = self.live_video
            print("Pausing video:", self.live_video.title)

    def continue_video(self):
        """Resumes playing the current video."""
        if self.live_video is None:
            print("Cannot continue video: No video is currently playing")
            return

        if self.paused_video is None:
            print("Cannot continue video: Video is not paused")
            return

        self.paused_video = self.live_video
        self.paused_video = None
        print("Continuing video:", self.live_video.title)

    def show_playing(self):
        if self.live_video is None:
            print("No video is currently playing")
            return

        v = self.live_video
        tag = str(v.tags)[1:-1].replace(",", "").replace("'", "")

        if self.paused_video is not None:
            print("Currently playing:", v.title + " (" + v.video_id + ")" + " [" + tag + "]" + " - PAUSED")
        else:
            print("Currently playing:", v.title + " (" + v.video_id + ")" + " [" + tag + "]")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        new_playlist = str(playlist_name).lower()

        if new_playlist in [key.lower() for key in self.playlist_dict.keys()]:
            print("Cannot create playlist: A playlist with the same name already exists")
            return

        self.playlist_dict[playlist_name] = []
        print("Successfully created new playlist:", playlist_name)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        add_playlist = str(playlist_name).lower()

        video_id_array = []
        for v in self._video_library.get_all_videos():
            video_id_array.append(v.video_id)

        if add_playlist not in [key.lower() for key in self.playlist_dict.keys()]:
            print("Cannot add video to", playlist_name, ": Playlist does not exist")
            return

        if video_id not in video_id_array:
            print("Cannot add video to", playlist_name, ": Video does not exist")
            return

        if video_id in playlist_name:
            print("Cannot add video to", playlist_name, ": Video already added")
            return

        p_lower = {k.lower(): v for k, v in self.playlist_dict.keys()}
        self.playlist_dict[add_playlist].append(video_id)
        print("Added video to" + playlist_name + ":" + self._video_library.get_video(video_id).title)
        print(self.playlist_dict[add_playlist])

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
