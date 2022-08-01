import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--download_train_path", default="../data/train.csv")
parser.add_argument("--download_test_path", default="../data/test.csv")
parser.add_argument("--pre1", action="store_true")
parser.add_argument("--pre2", action="store_true")
parser.add_argument("--output_dir", default="../data")
# preprocess1の引数
parser.add_argument("--pre1_arg", type=int, default=3)
# preprocess2の引数
parser.add_argument("--pre2_arg", type=int, default=2)
args = parser.parse_args()


def preprocess1(num):
    print(f"preprocess1: arg {num}")


def preprocess2(num):
    print(f"preprocess2:{num}")


def main():
    if args.pre1:
        preprocess1(args.pre1_arg)

    if args.pre2:
        preprocess2(args.pre2_arg)


if __name__ == "__main__":
    main()
