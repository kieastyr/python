import sys
from src import model

def main():
    # 学習済みモデルを読み込む
    classifier = model.Classifier()
    classifier.load_model('./src/classifier.pkl')

    # 標準入力からSMILESを読み込み
    smiles_list = []
    for line in sys.stdin:
        smiles_list.append(line.strip())

    # 予測を行う
    predict_Y = classifier.predict(smiles_list)

    # 予測を出力する
    for output in predict_Y:
        print(output)
    
if __name__ == "__main__":
    main()
