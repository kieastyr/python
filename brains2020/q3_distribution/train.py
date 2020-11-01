from src import model


def main():
    # 機械学習で使用するモデルを宣言
    classifier = model.Classifier()

    # 学習データから学習用のデータを読み込む
    with open('./data/smiles.txt', 'r', encoding='utf-8') as f_data:
        input_smiles = f_data.read().split("\n")
    with open("./data/class.txt", "r", encoding="utf-8") as f_label:
        input_label = f_label.read().split("\n")
    
    classifier.train(input_smiles, input_label)

    # 学習済みモデルを保存する
    model_filename = './src/classifier.pkl'
    classifier.save_model(model_filename)
    print("saved")


if __name__ == "__main__":
    main()
