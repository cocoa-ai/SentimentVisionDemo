import coremltools

coreml_model = coremltools.converters.caffe.convert(('twitter_finetuned_test4_iter_180.caffemodel', 'sentiment_deploy.prototxt'), image_input_names = 'data', class_labels='labels.txt')
coreml_model.author = 'Image Processing Group - BarcelonaTECH - UPC'
coreml_model.license = 'MIT'
coreml_model.short_description = 'Fine-tuning CNNs for Visual Sentiment Prediction'
coreml_model.input_description['data'] = 'An image.'
coreml_model.output_description['prob'] = 'The probabilities for each sentiment, for the given input.'
coreml_model.output_description['classLabel'] = 'The most likely sentiment, for the given input.'
coreml_model.save('VisualSentimentCNN.mlmodel')
