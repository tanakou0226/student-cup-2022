import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--train_path", default="../data/train.csv")
# train parameter
parser.add_argument("--lr", default=2e-5)
parser.add_argument("--batch_size", type=int, default=16)
args = parser.parse_args()


def train():
    print("train")


def main():
    train()


if __name__ == "__main__":
    main()
