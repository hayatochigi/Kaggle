# Overview
[Kerasの使い方をざっくりと](http://marupeke296.com/IKDADV_DL_No2_Keras.html) とても分かりやすい。あれっ？ってなったときに読むとこうかはばつぐんだ。
## Tensorflow環境構築
- Anaconda環境  
 +- Jupyter Notebook  
 +- Python 3.6  
 +- Tensorflow 2.1  
 +- numpy  
 +- pandas  
 +- scikit-learn   
パッケージインストールは基本condaコマンドを使用するとスムーズだった。pipとcondaを混在するとギルティ。

## 1st Try, CNN
train_test_splitの"test_size"はちょっと小さいかなと思いつつ"0.1"で設定。
```
Train on 37800 samples
Epoch 1/20
37800/37800 [==============================] - 39s 1ms/sample - loss: 0.1540 - accuracy: 0.9514
Epoch 2/20
37800/37800 [==============================] - 35s 920us/sample - loss: 0.0502 - accuracy: 0.9844
Epoch 3/20
37800/37800 [==============================] - 32s 856us/sample - loss: 0.0338 - accuracy: 0.9887
...
Epoch 48/50
37800/37800 [==============================] - 37s 981us/sample - loss: 0.0021 - accuracy: 0.9996
Epoch 49/50
37800/37800 [==============================] - 35s 933us/sample - loss: 0.0056 - accuracy: 0.9990
Epoch 50/50
37800/37800 [==============================] - 38s 1ms/sample - loss: 3.0079e-04 - accuracy: 0.9999

score = cnn.evaluate(X_test, y_test)
4200/4200 [==============================] - 1s 258us/sample - loss: 0.1736 - accuracy: 0.9898
```


## 2nd Try, CNN
上位の方のNotebookも拝見しながら、トライアンドエラー。[Introduction to CNN Keras - 0.997 (top 6%)](https://www.kaggle.com/yassineghouzam/introduction-to-cnn-keras-0-997-top-6)
ドロップアウトについて理解しておけば、過学習を正しく防ぐことができる。[過学習と学習不足について知る](https://www.tensorflow.org/tutorials/keras/overfit_and_underfit?hl=ja)
```
Epoch 18/20
1680/1680 [==============================] - 62s 37ms/step - loss: 0.0186 - accuracy: 0.9947
Epoch 19/20
1680/1680 [==============================] - 62s 37ms/step - loss: 0.0187 - accuracy: 0.9936
Epoch 20/20
1680/1680 [==============================] - 62s 37ms/step - loss: 0.0168 - accuracy: 0.9947

score = cnn.evaluate(X_test, y_test)
263/263 [==============================] - 4s 13ms/step - loss: 0.0382 - accuracy: 0.9906
```
Kaggleへのsubmissionはこんな感じ。
<p align="center">
  <img width="600" src="https://github.com/hayatochigi/images/blob/master/Kaggle/kaggle_digit_2nd.PNG">
</p>