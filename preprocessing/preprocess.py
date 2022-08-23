import argparse
import re

import pandas as pd

from eda_func import gen_eda

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--download_train_path", default="../data/train.csv")
parser.add_argument("--download_test_path", default="../data/test.csv")
parser.add_argument("--output_train_path", default="../data/train_preprocessed.csv")
parser.add_argument("--output_test_path", default="../data/test_preprocessed.csv")
# EDA parameter
parser.add_argument("--num_aug", default=8, help="number of augmented sentences per original sentence")
parser.add_argument("--alpha_sr", default=0.05, help="percent of words in each sentence to be replaced by synonyms")
parser.add_argument("--alpha_ri", default=0.05, help="percent of words in each sentence to be inserted")
parser.add_argument("--alpha_rs", default=0.05, help="percent of words in each sentence to be swapped")
parser.add_argument("--alpha_rd", default=0.05, help="percent of words in each sentence to be deleted")
args = parser.parse_args()

# HTMLタグ除去
def rm_tag(text):
    p = re.compile(r"<[^>]*?>")
    return p.sub("", text)


def cleaning(texts):
    clean_texts = []
    for text in texts:
        # htmlタグを削除
        text = rm_tag(text)

        # edaでの処理
        text = text.replace("’", "")
        text = text.replace("'", "")
        text = text.replace("-", " ")  # replace hyphens with spaces
        text = text.replace("\t", " ")
        text = text.replace("\n", " ")
        text = text.lower()
        text = re.sub(r"[^a-z]", " ", text)
        text = re.sub(" +", " ", text)  # delete extra spaces
        if text[0] == " ":
            text = text[1:]

        clean_texts.append(text)
    return clean_texts


def main():
    train_df = pd.read_csv(args.download_train_path)
    test_df = pd.read_csv(args.download_test_path)

    train_df["description"] = cleaning(train_df["description"])
    test_df["description"] = cleaning(test_df["description"])

    train_df = gen_eda(train_df, args.alpha_sr, args.alpha_ri, args.alpha_rs, args.alpha_rd, args.num_aug)

    train_df.to_csv(args.output_train_path, index=False)
    test_df.to_csv(args.output_test_path, index=False)


if __name__ == "__main__":
    main()
