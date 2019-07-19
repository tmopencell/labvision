from clarifai.rest import ClarifaiApp

image_directory = '/home/pi/webcam/cam1/'

app = ClarifaiApp(api_key='40d74b5ce16b47d794ee6b6955f7f930')
model = app.public_models.general_model
##response = model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')
#response = model.predict_by_url('https://gb.gilson.com/pub/media/catalog/product/cache/c687aa7517cf01e65c009f6943c2b1e9/F/1/F123603_MAIN_Pipetman-Classic-Single-Channel-Pipette-P5000_8.jpg')
response = model.predict_by_filename(image_directory+'2019-06-05_140044.jpg')

concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])
