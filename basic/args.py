# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("--learning-rate", "-lr", type=float, default=0.001, help='your input')

# args = parser.parse_args()

# print(dir(args))


import argparse
import os

cur_dir = os.getcwd()
parser = argparse.ArgumentParser(description="hello")
parser.add_argument('--train-folder', type = str, default = f"{cur_dir}/data/train", help = "path to train dataset")
parser.add_argument('--batch-size', '-bs', type=int, default = 16, help = 'inter ur batch size')
parser.add_argument('-v', type=int, default = 0, choices=[0,1])
args = parser.parse_args()
print(args.train_folder)
# print(args.batch_size)