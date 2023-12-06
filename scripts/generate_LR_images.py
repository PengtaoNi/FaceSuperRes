import os
import argparse
from PIL import Image


def main(args):
    img_paths = sorted(os.listdir(args.input))
    for img_path in img_paths:
        # TODO:
        # Implement Blur (Gaussian, 2D sinc, etc.),
        #           Downsample (Bicubic, Bilinear, etc.)
        #           Noise (Gaussian, Poisson, etc.)
        #           Compression (JPEG)

        img = Image.open(os.path.join(args.input, img_path))
        hr = img.crop((0, 0, img.size[0] // 4 * 4, img.size[1] // 4 * 4))
        hr = hr.resize((hr.size[0] * 4, hr.size[1] * 4), Image.BICUBIC)
        lr = hr.resize((hr.size[0] // 4, hr.size[1] // 4), Image.BICUBIC)
        hr.save(os.path.join(args.input, img_path))
        lr.save(os.path.join(args.output, img_path))


if __name__ == "__main__":
    """
    Generate LR (degraded) images from HR images.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        nargs="+",
        default="dataset/celeba/celeba_aligned_HR",
        help="Input folder",
    )
    parser.add_argument(
        "--output",
        nargs="+",
        default="dataset/celeba/celeba_aligned_LR",
        help="Output folder",
    )
    args = parser.parse_args()

    main(args)
