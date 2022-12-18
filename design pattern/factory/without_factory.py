"""Basic video exporting"""

import pathlib
from abc import ABC, abstractmethod

class VideoExporter(ABC):
    """Basic representation of video exporting"""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder"""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting"""

    def prepare_export(self, video_data):
        print("Preparing video data for lossless export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}.")


class H264BPVideoExporter(VideoExporter):
    """Lossless video exporting"""

    def prepare_export(self, video_data):
        print("Preparing video data for H264BP export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H264BP format to {folder}.")


class H264i422VideoExporter(VideoExporter):
    """Lossless video exporting"""

    def prepare_export(self, video_data):
        print("Preparing video data for H264i422 export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H264i422 format to {folder}.")


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""


class AACAudioExporter(AudioExporter):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}.")


class WAVAudioExporter(AudioExporter):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}.")

"""
You can see main fucntion got too many responsibilities
It's responsible for
    - asking the user with the export quality
    - mapping that desired quality to actual objects
    - doing the export
"""
def main() -> None:
    """Main Function"""
    
    export_quality: str
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break
        print("Unknown")

    video_exporter: VideoExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
    elif export_quality == "high":
        video_exporter = H264i422VideoExporter()
    else:
        video_exporter = LosslessVideoExporter()
    
    video_exporter.prepare_export("video_data")
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)


if __name__ == '__main__':
    main()
