import boto3

from PIL import Image
import io

def image_to_bytes(image_path, format='JPEG'):
    """
    Converts an image to bytes.

    Args:
        image_path (str): Path to the image file.
        format (str, optional): Image format for encoding. Defaults to 'JPEG'.

    Returns:
        bytes: Byte representation of the image.
    """
    try:
        # Open the image using Pillow library
        img = Image.open(image_path)

        # Create a BytesIO object to hold the image data in memory
        img_bytes = io.BytesIO()

        # Save the image to BytesIO object in the specified format
        img.save(img_bytes, format=format)

        # Get the byte data from BytesIO object
        byte_data = img_bytes.getvalue()
        return byte_data

    except FileNotFoundError:
        print(f"Error: Image file not found at '{image_path}'")
        return None
    except Exception as e:
         print(f"An error occurred: {e}")
         return None

image_path_cur = 'image.jpg'
image_path_root = 'rekognition/image.jpg'
image_bytes = image_to_bytes(image_path_cur)

if not image_bytes:
    image_bytes = image_to_bytes(image_path_root)

if image_bytes:
    rekognition = boto3.client('rekognition')

    response = rekognition.detect_labels(
        Image={'Bytes': image_bytes}
    )

    print(response)

else:
    print("Image conversion failed.")