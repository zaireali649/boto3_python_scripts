import boto3
from PIL import Image
import io
from typing import Optional

def image_to_bytes(image_path: str, format: str = 'JPEG') -> Optional[bytes]:
    """
    Convert an image file to a byte stream.

    Args:
        image_path (str): The file path to the image.
        format (str, optional): Format to encode the image (e.g., 'JPEG', 'PNG'). Defaults to 'JPEG'.

    Returns:
        Optional[bytes]: The image in byte format if successful, otherwise None.
    """
    try:
        # Open the image using the Pillow library
        img = Image.open(image_path)

        # Create a BytesIO stream to hold the image data in memory
        img_bytes = io.BytesIO()

        # Save the image to the BytesIO stream in the specified format
        img.save(img_bytes, format=format)

        # Return the byte data from the BytesIO stream
        return img_bytes.getvalue()

    except FileNotFoundError:
        # Handle case where the image file does not exist
        print(f"Error: Image file not found at '{image_path}'")
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An error occurred: {e}")
        return None

# Define two image paths: one current directory, one nested
image_path_cur: str = 'image.jpg'
image_path_root: str = 'rekognition/image.jpg'

# Attempt to convert the image to bytes from the current directory
image_bytes: Optional[bytes] = image_to_bytes(image_path_cur)

# Fallback to alternate path if the first conversion fails
if not image_bytes:
    image_bytes = image_to_bytes(image_path_root)

# If image was successfully converted to bytes
if image_bytes:
    # Create a boto3 Rekognition client
    rekognition = boto3.client('rekognition')

    # Call Rekognition API to detect labels in the image
    response = rekognition.detect_labels(
        Image={'Bytes': image_bytes}
    )

    # Output the label detection response
    print(response)

else:
    # Inform the user of failure if neither image path worked
    print("Image conversion failed.")
