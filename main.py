import sys
import argparse
from train import train
from test import test

def main(args):
    train(args)
    test(args)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Person Re-Identification Reproduce')
    parser.add_argument('--params-filename', type=str, default='reid.pth.tar', help='filename of model parameters.')
    parser.add_argument('--use-gpu', type=int, default=1, help='set 1 if want to use GPU, otherwise 0. (default 1)')
    parser.add_argument('--world-size', type=int, default=1, help='number of distributed processes. (default 1)')
    parser.add_argument('--dist-url', type=str, default='tcp://127.0.0.1:2222', help='the master-node\'s address and port')
    parser.add_argument('--dist-rank', type=int, default=0, help='rank of distributed process. (default 0)')
    parser.add_argument('--last-conv', type=int, default=1, help='whether contains last convolution layter. (default 1)')
    args = parser.parse_args()
    args.distributed = args.world_size > 1
    main(args)