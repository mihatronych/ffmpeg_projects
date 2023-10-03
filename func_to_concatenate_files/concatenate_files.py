# import the necessary packages
import ffmpeg


# "concant_audio_video" function where the videos of different codecs are concatenated
def concat__audio_video():
    # Input videos in different codecs
    in1 = ffmpeg.input(r'video1.mkv') # МОЖнО ЗАМЕНИТЬ НА ДРУГИЕ
    in2 = ffmpeg.input(r'video2.wmv')
    in3 = ffmpeg.input(r'video3.mp4')

    # filter scale, filter setsar, filter fps
    # The scale filter forces the output display aspect ratio to be the same of the input, by changing the output sample aspect ratio.
    # The setsar filter sets the Display Aspect Ratio for the filter output video.
    # the fps filter converts the video to a specified constant frame rate by doubling or dropping frames as needed.
    def filters(i):
        width = 640
        height = 360
        fps = 20
        return i['v'].filter('scale', width, height).filter('setsar', '1/1').filter('fps', fps, round='up')

    # videos files applying the filters
    v1 = filters(in1)
    a1 = in1['a']
    v2 = filters(in2)
    a2 = in2['a']
    v3 = filters(in3)
    a3 = in3['a']
    # Concatenate audio and video streams, joining them together one after the other
    joined = ffmpeg.concat(v1, a1, v2, a2, v3, a3, v=1, a=1).node
    # output file
    ffmpeg.output(joined[0], joined[1], 'out.mp4').run()


concat__audio_video()
