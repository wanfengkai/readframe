import os
import subprocess
import argparse


# add argparse for controlling .

parser = argparse.ArgumentParser()
parser.add_argument("--origin", help=' the path of your original video',
                    type=str, default='./try.mp4')


args = parser.parse_args()


# start from here
# origin videos' path
origin = args.origin

# create folder to save all the result

# change the folder name if you want
temp_movie = './temp'
vis_path = './vis_folder'


def create_if_no_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


create_if_no_folder(temp_movie)
create_if_no_folder(vis_path)


# create temp avi movie, it's the best way to save it in avi for high accuracy
# Don't change here, if it's not necessary
movie_name = origin.split('/')[-1].split('.')[0]
source_movie = os.path.join(temp_movie, movie_name + '.avi')


# preprocess data
# #if you want any resolution
# feel free to change the scale value, you can use it to whatever you like, just keep in mind smaller means
# less accuracy but faster speed
if not os.path.exists(source_movie):

    pre_proc = subprocess.Popen(
        ['ffmpeg', '-i', origin, '-vf', 'scale=320:240', source_movie])
    pre_proc.wait()

# create png images by frame number:


def get_img_by_frame(frame_num, source_movie):
    '''
    frame_num: frame index: eg: 16, 100, start with non_zero

    '''
    save_path = os.path.join(vis_path, 'img_{}.png'.format(frame_num))
    select_frame = 'select=gte(n\,{})'.format(frame_num)
    pre_proc = subprocess.Popen(
        ['ffmpeg', '-i', source_movie, '-vf', select_frame, '-vframes', '1', save_path])
    pre_proc.wait()


# example use

get_img_by_frame(62,source_movie)

