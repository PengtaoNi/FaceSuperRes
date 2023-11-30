import argparse
import glob
import os


def main(args):
    with open(args.annotation, 'r') as f:
        lines = f.readlines()
        attributes = lines[1].strip().split(' ')
        """
        0: 5_o_Clock_Shadow
        1: Arched_Eyebrows
        2: Attractive (not used)
        3: Bags_Under_Eyes
        4: Bald
        5: Bangs
        6: Big_Lips
        7: Big_Nose
        8: Black_Hair
        9: Blond_Hair
        10: Blurry (not used)
        11: Brown_Hair
        12: Bushy_Eyebrows
        13: Chubby
        14: Double_Chin
        15: Eyeglasses
        16: Goatee
        17: Gray_Hair
        18: Heavy_Makeup
        19: High_Cheekbones
        20: Male
        21: Mouth_Slightly_Open
        22: Mustache
        23: Narrow_Eyes
        24: No_Beard
        25: Oval_Face
        26: Pale_Skin
        27: Pointy_Nose
        28: Receding_Hairline
        29: Rosy_Cheeks
        30: Sideburns
        31: Smiling
        32: Straight_Hair
        33: Wavy_Hair
        34: Wearing_Earrings
        35: Wearing_Hat
        36: Wearing_Lipstick
        37: Wearing_Necklace
        38: Wearing_Necktie
        39: Young
        """
    
    for i in range(len(attributes)):
        attributes[i] = attributes[i].replace('_', ' ')

    texts = []
    for line in lines[2:]:
        vals = line.strip().split()[1:]
        text = ''

        adjectives = [39, 13, 31, 4]
        for i in adjectives:
            if vals[i] == '1':
                text += attributes[i] + ' '
        
        if vals[20] == '1': # Male
            text += 'Man with '
        else:
            text += 'Woman with '
        
        others = [0, 1, 3, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, \
                  25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38]
        for i in others:
            if vals[i] == '1':
                text += attributes[i] + ', '

        texts.append(text[:-2])
    
    with open(args.text, 'w') as f:
        for text in texts:
            f.write(text + '\n')

if __name__ == '__main__':
    """This script is used to generate meta info (txt file) for paired images.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--annotation',
        type=str,
        default='dataset/celeba/annotation.txt',
        help='txt path for annotations'
    )
    parser.add_argument(
        '--text',
        type=str,
        default='dataset/celeba/celeba_aligned_text.txt',
        help='txt path for generated text'
    )
    args = parser.parse_args()

    main(args)
