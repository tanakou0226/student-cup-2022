# Setup
## EDAを行う場合

EDAを行うためのツールをclone

```bash
mkdir tools_external
cd tools_external
git clone https://github.com/jasonwei20/eda_nlp.git
```

### Install NLTK

nltkをインストール
```bash
pip install -U nltk
```

WordNetをダウンロード
```bash
python
>>> import nltk; nltk.download('wordnet')
```