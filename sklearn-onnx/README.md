# sklearn-onnx with LabVIEW
Train a Scikit-learn model in [Docker](https://www.docker.com/) container and convert it to [ONNX](https://onnx.ai/) format. 
Then, Do prediction in LabVIEW by calling the prediction script with [Python Node](https://zone.ni.com/reference/en-XX/help/371361R-01/glang/python_node/).

<p align="center">
  <img width="600" src="https://github.com/hayatochigi/images/blob/master/Kaggle/sklearn-onnx-in-LabVIEW.png">
</p>

## Installation on Windows
Python Node cannot recognize Anaconda Environment [Integrate Conda Python Environment with LabVIEW](https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z0000015C6tSAE&l=en-US). Required packages are directly installed in Windows.
- Python
- numpy
- onnxruntime

```
C:\xxx>py -3.6-64 -m pip install scikit-learn numpy pandas
Collecting scikit-learn
...
....
.....

Successfully installed joblib-1.0.1 numpy-1.19.5 pandas-1.1.5 python-dateutil-2.8.1 pytz-2021.1 scikit-learn-0.24.1 scipy-1.5.4 six-1.15.0 threadpoolctl-2.1.0
You are using pip version 18.1, however version 21.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

C:\xxx>py -3.6-64 -m pip install onnxruntime
Collecting onnxruntime
...
....
.....

Installing collected packages: protobuf, onnxruntime
  The script onnxruntime_test.exe is installed in 'C:\xxx\Python\Python36\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed onnxruntime-1.6.0 protobuf-3.15.3
You are using pip version 18.1, however version 21.0.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
```

## Prediction Script
```
import onnxruntime as rt
import numpy as np

# Load scikit-learn model and do prediction

def get_prediction(model_path, X):
    # convert list to numpy array
    X = np.array(X)
    # "sees.run" expect 2D array input.

    sess = rt.InferenceSession(model_path)

    input_name = sess.get_inputs()[0].name
    label_name = sess.get_outputs()[0].name

    # Do prediction
    pred_onx = sess.run([label_name], {input_name: X.astype(np.float32)})[0]
    
    # int64 would be returned
    return pred_onx
```