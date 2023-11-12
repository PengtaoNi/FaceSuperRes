#!/bin/bash

URL="https://drive.google.com/file/d/0B7EVK8r0v71pZjFTYXZWM3FlRnM/view?usp=drive_link&resourcekey=0-dYn9z10tMJOBAkviAcfdyQ"
DOWNLOAD_PATH="data/celeba.zip"
EXTRACTED_PATH="data/celeba/"

mkdir -p $(dirname $DOWNLOAD_PATH)

echo "Downloading CelebA dataset..."
gdown --id $FILE_ID -O $DOWNLOAD_PATH

echo "Unzipping CelebA dataset..."
unzip $DOWNLOAD_PATH -d $EXTRACTED_PATH

echo "Download and extraction complete."