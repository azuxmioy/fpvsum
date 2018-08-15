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

FPVSum consists of 14 categories of videos from YouTube, resulting in a total number of 98 first-person videos. We carefully selected continuous first-person videos only (i.e., no transition within or between points of views), and exluded those with unrelated contents.

### How to get the videos


 



## Ground-Truth Scores

## User Interface for Human Annotation

## References

