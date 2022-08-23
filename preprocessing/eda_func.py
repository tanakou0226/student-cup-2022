import pandas as pd

from tools_external.eda_nlp.code.eda import eda


def gen_eda(train_df, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug):
    aug_df = pd.DataFrame(columns=train_df.columns)
    for i, row in train_df.iterrows():
        id = row["id"]
        label = row["jobflag"]
        sentence = row["description"]
        aug_sentences = eda(
            sentence, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, p_rd=alpha_rd, num_aug=num_aug
        )

        original = pd.DataFrame([[id, sentence, label]], columns=aug_df.columns)
        aug_df = pd.concat([aug_df, original], axis=0)
        for i in range(num_aug):
            tmp = pd.DataFrame([[id, aug_sentences[i], label]], columns=aug_df.columns)
            aug_df = pd.concat([aug_df, tmp], axis=0)

    return aug_df
