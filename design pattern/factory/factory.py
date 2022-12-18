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


# it provides us the instances we need to create an object
class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio.
    The factory doesn't maintain any of the instances it creates.
    """

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance"""

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance"""


class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed, lower quality export."""
    def get_video_exporter(self) -> VideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a slower speed, high quality export."""
    def get_video_exporter(self) -> VideoExporter:
        return H264i422VideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing a low speed, master quality export."""
    def get_video_exporter(self) -> VideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preferences"""
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }
    
    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print("Unknown")


def main(fac: ExporterFactory) -> None:
    """Main Function"""

    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    video_exporter.prepare_export("video_data")
    audio_exporter.prepare_export("audio")

    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == '__main__':
    fac = read_exporter()
    main(fac)
