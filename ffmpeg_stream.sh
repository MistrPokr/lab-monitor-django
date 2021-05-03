ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video0    \
        -b:v 2000k -r 15 -f flv rtmp://localhost/live/py