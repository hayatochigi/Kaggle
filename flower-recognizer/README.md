# Overview
[tf.dataを使って画像をロードする](https://www.tensorflow.org/tutorials/load_data/images?hl=ja) から取得した花の画像をCNNで分類したい

## 1st Try
データの前処理までは検証して、いざネットワークを構築する段階でメモリオーバーフロー...クラウドで試します。

Tensorは基本immutableなので、Pillowを用いて取得した3次元配列を、どのように4次元にバッチかすればよいのか。。。
```
# 学習データを格納するため、pandasのDataFrameを作成
image_size = 3
# 列はpixelサイズの2乗
columns_name = [str(n) for n in list(range(image_size**2))]
# それにラベル列をプラス
columns_name.append('label')
df = pd.DataFrame(columns = columns_name)

storage_file = open('csv_storage.csv', 'w')
writer = csv.writer(storage_file)
writer.writerow(columns_name)
from PIL import Image
count = 0
for folder_path in flower_folders:
    for file_path in folder_path.iterdir():
        if os.path.splitext(file_path)[-1] == '.jpg':
            image = Image.open(file_path)
            # 画像データをリサイズし、ndarrayへ変換
            X = np.asarray(image.resize((image_size, image_size), Image.NEAREST))
            image.close()
            
            # 1次元に変換
            X = X.reshape(-1)
            # 末尾に(label列に)ディクショナリからの値を追加
            X = np.append(X,label_dictionary[os.path.basename(os.path.dirname(file_path))])
            
            # storage用のcsvファイルへ保存
            writer.writerow(X)
            count += 1
            if count > 2:
                break
storage_file.close()
```
一旦ストレージにためておいて、後でpd.read_csvを使って読もうとした。考えとしてはありなのでは？と思ったが、1行で3次元の表現がうまくできずいったん保留。

とりあえず、cnn.fitにXとyを渡して訓練ができるところまでは完了。次のチャレンジでレイヤーの構築を行っていく。