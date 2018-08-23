FPVSum  Dataset
=======
First-Person Video Summarization (FPVSum) dataset proposed in our ECCV 2018 paper "**First-Person Video Summarization From Third Person's Point of Views.**"

## Description

First-Person Video Summarization (FPVSum) dataset is a benchmark to evaluate video summarization algorithms especially for first-person videos. FPVSum contains 14 categories of first-person videos captured by head- or body-mounted devices alongside their corrosponding human-annotated frame-level importance scores. The ground-truth scores are used for both training and evalutaion in this paper.

The files of FPVSum are listed as below. We provide lists and scripts to obtain selected first-person videos from YouTube. Both frame-level importance scores and the UI for annotation are also provided for public use.

```
fpvsum/
 ⊢ crawler/        # scripts to obtain video data
 ⊢ annotation/     # ground-truth scores of videos
 ⊢ UI/             # user interface for labeling
```


## Videos

<img src="https://github.com/azuxmioy/fpvsum/blob/master/images/thumbnail.png" height="350">

FPVSum consists of 14 categories of videos from YouTube, resulting in a total number of 98 first-person videos. During the collection of the first-person videos, we found that a large number of such videos on YouTube are not raw videos but edited ones, consisting of obvious frame discontinuity, transitions of point-of-view, and unrelated contents. Thus, we carefully selected continuous first-person videos only (i.e., no transition within or between points of views), and exluded those with unrelated contents.

### How to get the videos

**Prerequisites**  
* [youtube-dl](https://github.com/rg3/youtube-dl/)

**Run the scripts**  
To download the videos in the list, you may simply run the following commands:
```
mkdir video_dir

chmod +x fetch_fpvsum_videos.sh

./fetch_fpvsum_videos.sh video_dir FPVSum_videolist.csv
```


## Ground-Truth Scores

We invite more than 15 volunteers to perform video annotation. Given each video, annotators are asked to produce a summary that contains most of its important content and highlight segments using our designed human interface. We observe that most annotators would lose concentration on assigning scores for very long videos. Thus, for each video category we select about 35% of the video sequences to be annotated with ground-truth scores, while the remaining are viewed as the unlabeled ones.  

The details of our annotation process are shown as follows:

* The annotators require to select highlight/non-highlight segments in each video. They need to finish watching each video once, then they start the labeling process.
* The annotators are asked to select the video parts which they consider interesting or important (i.e., mark the parts to red color using the interface). We note that an interesting part being marked may vary in any length.
* The annotators are encouraged to produce the summary which accounts for 10% to 20% of the full video length.
* Each frame would get an importance score which indicates how many annotators mark on this frame. We finally select frames ranked in the top 15% of all video frames as the highlight ones.

## User Interface for Human Annotation

<img src="https://github.com/azuxmioy/fpvsum/blob/master/images/UI.png" height="350">

We provide a user interface (written in MATLAB language) for labeling video sequences. The interface shows each video excluding its audio track, ensuring annotators select highlight based on visual content only. Annotators are able to use the interface for moving forward and backward and modify their annotations at any time.

## References

Hsuan-I Ho, Wei-Chen Chiu, and Yu-Chiang Frank Wang: Summarizing First-Person Videos from Third Persons’ Points of Views. In: Proceedings of the European Conference on Computer Vision (ECCV) (2018)
