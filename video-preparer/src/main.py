from components import myComponent
import ffmpeg


def flip_horizontally(input_file):  
    """Output path same as file_path"""
    ffmpeg.input(input_file).hflip().output('HF' + input_file).run()

