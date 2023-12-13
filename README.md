# FaceSuperRes

A final project for 11-785 Introduction to Deep Learning, Fall 23.

## Introduction

We explore an enhanced approach in Single Image Super-Resolution (SISR) by integrating textual descriptions into the existing blind SISR framework. Unlike traditional models
that primarily rely on visual data, our approach combines both visual and textual
information, providing a more comprehensive context for image upscaling.

In particular, we fine-tune [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) on 25% of [CelebA](https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html) dataset (5K images) with different text input and losses. More details are explained in our report.

## How to run

1. Clone this repo. 

    ```git clone https://github.com/PengtaoNi/FaceSuperRes.git```

2. Install required modules.
    
    ```pip install -r requirements.txt``` 
3. Run [inference_script.ipynb](/inference/inference_script.ipynb) in [inference](/inference) folder. More details are explained in this jupyter notebook file.
4. The generated (super-resoluted, SRed) results are in [results](/inference/results) folder.
5. Further, run [calculate_niqe.py](/inference/calculate_niqe.py) to create a .csv file containing NIQE scores for SRed images.

## Ablations

Find sample results on exp branch at [inference/results](https://github.com/PengtaoNi/FaceSuperRes/tree/exps/inference/results).

## Members

### Mentor

- Qin Wang

### Authors

- Ashely Chung
- Pengtao Ni
- Wenyi Qian
- Wonjin Wang
