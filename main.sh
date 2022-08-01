cd preprocessing
python preprocess.py --pre1
cd ../

cd learning
python train.py
cd ../

cd predicting
python predict.py

# 結果提出
# signate submit -c 735 <結果ファイルのパス> --note <コメント>