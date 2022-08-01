import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model_path", default="../output/best_val.pt")
parser.add_argument("--test_path", default="../data/test.csv")
args = parser.parse_args()


def predict():
    print("predict")


def main():
    predict()


if __name__ == "__main__":
    main()
