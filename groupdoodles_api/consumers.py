import json
from channels.generic.websocket import WebsocketConsumer

class SignallingSocketConsumer(WebsocketConsumer):
  def connect(self):
    self.accept()
    self.send(text_data=json.dumps({
      'type': 'connection established',
      'message': 'You are now connected!'
    }))
    print('websocket connected')