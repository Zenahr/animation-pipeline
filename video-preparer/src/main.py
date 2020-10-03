from components import myComponent
import ffmpeg

TEST_FILE="D:/Open-Source/Animation Pipeline/video-preparer/data/i.mp4"

def flip_horizontally(input_file):  
    """Output path same as file_path"""
    ffmpeg.input(input_file).hflip().output('HF' + "-" + 'output.mp4').run()
# flip_horizontally(TEST_FILE)

def change_frame_rate(input_file, target_frame_rate=12):
    (
    ffmpeg
    .input(input_file)
    .filter('fps', fps=target_frame_rate, round='up')
    .output(filename="output.mp4")
    .overwrite_output()
    .run(capture_stdout=0)
    )

change_frame_rate(TEST_FILE)
