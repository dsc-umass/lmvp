from rest_framework import renderers
import json
class UserRenderer(renderers.JSONRenderer): #This pre-fixes responses with keywords, this ensures consitent responses in the API
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''

        if 'ErrorDetail' in str(data):
            response= json.dumps({'errors':data})
        else:
            response= json.dumps({'data':data})
        return response