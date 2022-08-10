import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    @abstractmethod
    def prepare_export(self, video_data):
        """Prepare the export of the video."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Do the export of the video."""


class LowQualityVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing low quality video export")

    def do_export(self, folder: pathlib.Path):
        print("Exporting low quality video to", folder)


class HighQualityVideoExporter(VideoExporter):
    def prepare_export(self, video_data):
        print("Preparing high quality video export")

    def do_export(self, folder: pathlib.Path):
        print("Exporting high quality video to", folder)


class AudioExporter(ABC):
    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepare the export of the audio."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Do the export of the audio."""


class LowQualityAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        print("Preparing low quality audio export")

    def do_export(self, folder: pathlib.Path):
        print("Exporting low quality audio to", folder)


class HighQualityAudioExporter(AudioExporter):
    def prepare_export(self, audio_data):
        print("Preparing high quality audio export")

    def do_export(self, folder: pathlib.Path):
        print("Exporting high quality audio to", folder)


class ExporterFactory(ABC):
    @abstractmethod
    def get_video_exporter(self):
        pass

    @abstractmethod
    def get_audio_exporter(self):
        pass


class LowQualityExporterFactory(ExporterFactory):
    def get_video_exporter(self):
        return LowQualityVideoExporter()

    def get_audio_exporter(self):
        return LowQualityAudioExporter()


class HighQualityExporterFactory(ExporterFactory):
    def get_video_exporter(self):
        return HighQualityVideoExporter()

    def get_audio_exporter(self):
        return HighQualityAudioExporter()


def get_exporter_factory():
    fac = {
        "low": LowQualityExporterFactory(),
        "high": HighQualityExporterFactory()
    }

    while True:
        export_quality = input("Enter export quality (low/high): ")
        if export_quality in fac:
            return fac[export_quality]
        else:
            print("Invalid export quality")


def main(exporter_factory):
    video_exporter = exporter_factory.get_video_exporter()
    audio_exporter = exporter_factory.get_audio_exporter()

    # Prepare the export
    video_exporter.prepare_export("video_data_here")
    audio_exporter.prepare_export("audio_data_here")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    export_factory = get_exporter_factory()
    main(export_factory)
