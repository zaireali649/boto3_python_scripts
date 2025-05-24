import boto3  # Import the AWS SDK for Python to interact with AWS services

# Create a Polly client to interact with the Amazon Polly service
polly = boto3.client('polly')

# Request Polly to synthesize speech using the generative engine
response = polly.synthesize_speech(
    Engine='generative',     # Use the new generative engine for more natural speech
    OutputFormat='mp3',      # Request the audio output in MP3 format
    Text='Hello from Boto3!',# The text that Polly will convert to speech
    VoiceId='Stephen'        # Use the 'Stephen' voice for the synthesized speech
)

# Extract the audio stream from the response
audioStream = response['AudioStream']

# Save the audio stream to a file named 'example.mp3'
with open("example.mp3", "wb") as f:
    f.write(audioStream.read())  # Read and write the binary MP3 content to file
