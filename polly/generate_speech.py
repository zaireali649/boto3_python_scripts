import boto3

polly = boto3.client('polly')

response = polly.synthesize_speech(
    Engine='generative',    
    OutputFormat='mp3',    
    Text='Hello from Boto3!',
    VoiceId='Stephen'
)

audioStream = response['AudioStream']

with open("example.mp3","wb") as f:
  f.write(audioStream.read())