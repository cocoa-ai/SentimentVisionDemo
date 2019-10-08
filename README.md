# Sentiment Vision Demo

A Demo application using `Vision` and `CoreML` frameworks to detect the most
likely sentiment of the given image.

<div align="center">
<img src="https://github.com/cocoa-ai/SentimentVisionDemo/blob/master/Screenshot.png" alt="SentimentVisionDemo" width="300" height="416" />
</div>

## Model

This demo is based on the "Fine-tuning CNNs for Visual Sentiment Prediction"
neural network classifier, which was converted from original [Caffe model](https://github.com/imatge-upc/sentiment-2017-imavis)
to [CoreML model](https://drive.google.com/file/d/1nt_Sp85Orplcbyyc7AAyCUjEfss8Pw87/view?usp=sharing)
using [coremltools](https://pypi.python.org/pypi/coremltools) python package.

## Requirements

- Xcode 9
- iOS 11

## Installation

```sh
git clone https://github.com/cocoa-ml/SentimentVisionDemo.git
cd SentimentVisionDemo
pod install
open SentimentVision.xcworkspace/
```

Download the [CoreMl model](https://drive.google.com/open?id=0B1ghKa_MYL6mZ0dITW5uZlgyNTg)
and drag the file into your project.

Build the project and run it on a simulator or a device with iOS 11.

## Conversion

```sh
cd Convert
./download.sh
python convert.py
```

## Author

Vadym Markov, markov.vadym@gmail.com

## Credits

[From Pixels to Sentiment: Fine-tuning CNNs for Visual Sentiment Prediction](https://github.com/imatge-upc/sentiment-2017-imavis)

## References
- [Caffe](http://caffe.berkeleyvision.org)
- [Apple Machine Learning](https://developer.apple.com/machine-learning/)
- [Vision Framework](https://developer.apple.com/documentation/vision)
- [CoreML Framework](https://developer.apple.com/documentation/coreml)
- [coremltools](https://pypi.python.org/pypi/coremltools)
