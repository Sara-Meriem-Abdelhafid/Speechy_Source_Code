'''import picamera
import time

# Set the video resolution and framerate
video_width = 640
video_height = 480
framerate = 30


# Create a Picamera instance
camera = picamera.PiCamera()

# Set the camera resolution and framerate
camera.resolution = (video_width, video_height)
camera.framerate = framerate

# Create a video file to save the recording
video_filename = 'output_video.h264'
camera.start_recording(video_filename)

# Record video for a specified duration (e.g., 10 seconds)
record_duration = 10
camera.wait_recording(record_duration)

# Stop recording and close the camera
camera.stop_recording()
camera.close()

print(f"Video recording saved to {video_filename}")'''
import time
import picamera

def capture_image(output_path='image.jpg'):
    # Initialize the camera
    with picamera.PiCamera() as camera:
        # Give the camera some time to warm up
        time.sleep(2)

        # Capture an image
        camera.capture(output_path)

if __name__ == "__main__":
    # Specify the output path for the image (default: image.jpg)
    output_path = 'image.jpg'

    # Capture an image and save it to the specified output path
    capture_image(output_path)

    print(f"Image captured and saved to {output_path}")

