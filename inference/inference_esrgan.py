# https://github.com/XPixelGroup/BasicSR/tree/master

import argparse
import glob
import os
import sys
import warnings

import cv2
import numpy as np
import torch
from basicsr.archs.rrdbnet_arch import RRDBNet

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(ROOT_DIR)
sys.path.append(REPO_DIR)

from realesrgan import RealESRGANer

warnings.filterwarnings("ignore")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--model_name",
        type=str,
        default="RealESRGAN_x4plus",
    )
    parser.add_argument(
        "-i", "--input", type=str, default="test_img", help="input test image folder"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="results", help="output folder"
    )

    args = parser.parse_args()

    model_path = os.path.join("weights", args.model_name + ".pth")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # set up model
    model = RRDBNet(
        num_in_ch=3,
        num_out_ch=3,
        num_feat=64,
        num_block=23,
        num_grow_ch=32,
        scale=4,
    )

    # params in upsampling
    scale = 4
    # restorer
    upsampler = RealESRGANer(
        scale=scale,
        model_path=model_path,
        model=model,
    )

    os.makedirs(args.output, exist_ok=True)
    for idx, path in enumerate(sorted(glob.glob(os.path.join(args.input, "*")))):
        img_name = os.path.splitext(os.path.basename(path))[0]
        print("Testing", idx, img_name)
        # read image
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        # inference
        try:
            output, _ = upsampler.enhance(img, outscale=scale)
        except Exception as error:
            print("Error", error, img_name)
        else:
            # save image
            cv2.imwrite(os.path.join(args.output, f"{img_name}_ESRGAN.png"), output)


if __name__ == "__main__":
    # because you call it from repo root
    os.chdir(ROOT_DIR)
    main()
