from argparse import ArgumentParser
import glob
import csv
import os

def get_video_list(video_path, csv_file):
    # Get existing videos
    existing_vids = glob.glob("%s/*.mp4" % video_path)
    for idx, vid in enumerate(existing_vids):
        basename = os.path.basename(vid).split(".mp4")[0]
        if len(basename) != 0:
            existing_vids[idx] = basename
        else:
            raise RuntimeError("Unknown filename format: %s", vid)
    # Read an get video IDs from annotation file

    result = {}

    with open (csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for column, value in row.items():
                result.setdefault(column,[]).append(value)

    all_vids = result['youtube_id']
    all_names = result['video_name']

    non_existing_videos = []
    video_names = []

    for vid, name in zip(all_vids, all_names):
        if name in existing_vids:
            continue
        else:
            non_existing_videos.append(vid)
            video_names.append(name)
    return non_existing_videos, video_names

def main(video_path, csv_file, output_filename):
    non_existing_videos, video_names= get_video_list(video_path, csv_file)
    filename = os.path.join(video_path, "%s.mp4")
    cmd_base = "youtube-dl -f best -f mp4 "
    cmd_base += '"https://www.youtube.com/watch?v=%s" '
    cmd_base += '-o "%s"' % filename
    with open(output_filename, "w") as fobj:
        for vid, name in zip(non_existing_videos, video_names):
            cmd = cmd_base % (vid, name)
            fobj.write("%s\n" % cmd)

if __name__ == "__main__":
    parser = ArgumentParser(description="Script to double check video content.")
    parser.add_argument("video_path", help="Path of the output video folder")
    parser.add_argument("csv_file", help="Location of the csv file (video list)")
    parser.add_argument("output_filename", help="Output script location.")
    args = vars(parser.parse_args())
    main(**args)
