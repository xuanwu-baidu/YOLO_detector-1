import os

# get a video from video_path and cut all frames and save them under frames_folder_path
def video2frames(video_path, frames_folder_path):
    # 构建命令
    command = 'ffmpeg -i '
    frames_dir_to_save = os.path.join(frames_folder_path,'out-%03d.jpg')

    # 执行命令
    command += video_path + ' ' + frames_dir_to_save
    os.system(command)
    
video2frames('video.mp4','input-frames')