import time
import ffmpeg


class VideoStream:
    """
    Wraps a ffmpeg video stream object.
    """

    def __init__(self):
        # default settings
        self.input = "/dev/video2"
        self.output = "rtmp://192.168.0.138/live/py"
        self.process = None

        # Defines the stream's input & output
        self.stream = ffmpeg.input(self.input)
        self.stream = ffmpeg.output(self.stream, self.output, f="flv")

    def start_stream(self):
        """
        Starts streaming
        :return: None
        """
        self.process = ffmpeg.run_async(self.stream, pipe_stdin=True)

    def stop_stream(self):
        """
        Stops streaming.
        Reference: https://github.com/kkroening/ffmpeg-python/issues/162
        :return: None
        """
        # Sends a "q" over stdin to terminate gracefully
        self.process.communicate(str.encode("q"))

        # Ensure the process ends properly
        time.sleep(3)
        self.process.terminate()

    def modify_stream_config(self):
        pass