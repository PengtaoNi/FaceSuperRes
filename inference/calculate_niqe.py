"""
Calculate niqe score for every output image and generate a text file
"""
import argparse
import glob
import os
import warnings

import basicsr.metrics.niqe as niqe
from numpy import asarray
from PIL import Image

warnings.filterwarnings("ignore")


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", type=str, default="results", help="input image folder"
    )
    parser.add_argument(
        "--output", type=str, default="baseline_niqe.csv", help="output text file"
    )
    parser.add_argument(
        "--description",
        type=str,
        default="baseline",
        help="description of the experiment method",
    )
    args = parser.parse_args()

    results_imgs = os.listdir(args.input)
    for i in results_imgs:
        img = Image.open(os.path.join(args.input, i))
        img_array = asarray(img)
        score = niqe.calculate_niqe(img_array, crop_border=0)
        with open(args.output, "a+") as f:
            print(i, score)
            f.write(i)
            f.write(", ")
            f.write(str(score))
            f.write("\n")


if __name__ == "__main__":
    # because you call it from repo root
    os.chdir(ROOT_DIR)
    main()
