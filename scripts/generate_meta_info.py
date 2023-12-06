import argparse
import glob
import os


def main(args):
    txt_file = open(args.meta_info, "w")
    # sca images
    img_paths_gt = sorted(glob.glob(os.path.join(args.input, "*")))

    for img_path_gt in img_paths_gt:
        # get the relative paths
        img_name_gt = os.path.relpath(img_path_gt, args.root)
        txt_file.write(f"{img_name_gt}\n")


if __name__ == "__main__":
    """This script is used to generate meta info (txt file) for paired images."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        nargs="+",
        default="dataset/celeba/celeba_aligned_HR",
        help="Input folder, should be path to gt_folder",
    )
    parser.add_argument("--root", nargs="+", default=None, help="Folder root")
    parser.add_argument(
        "--meta_info",
        type=str,
        default="dataset/celeba/celeba_aligned.txt",
        help="txt path for meta info",
    )
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.meta_info), exist_ok=True)
    if args.input.endswith("/"):
        args.input = args.input[:-1]
    if args.root is None:
        args.root = os.path.dirname(args.input)

    main(args)
