from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

def get_relevant_tags(image_url):
    response_data = app.tag_urls([image_url])

    tag_urls = []

    # loop through JSON-structured concepts and form list of associated tags
    for concept in response_data['outputs'][0]['data']['concepts']:
        tag_urls.append(concept['name'])

    return tag_urls

'''
Demo using picture of my hometown's town square:
print('\n'.join(get_relevant_tags('https://c1.staticflickr.com/5/4063/4713378212_06c871eba9_b.jpg')))
'''
