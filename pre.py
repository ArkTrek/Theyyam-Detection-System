from PIL import Image
import os
import shutil
import subprocess
#import pyheif 

def convert_heic_to_jpg(heic_file, jpg_file):
    subprocess.run(["sips", "-s", "format", "jpeg", heic_file, "--out", jpg_file], check=True)

def convert_webp_to_jpg(webp_file, jpg_file):
    subprocess.run(["dwebp", webp_file, "-o", jpg_file], check=True)

def convert_to_jpg(directory):
    # Get list of files in directory
    files = os.listdir(directory)

    # Iterate through files
    for filename in files:
        # Check if file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.heic')):
            try:
                # Construct new filename with .jpg extension
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_filepath = os.path.join(directory, new_filename)

                # For HEIC files, convert to JPG using pyheif
                if filename.lower().endswith('.heic'):
                    convert_heic_to_jpg(os.path.join(directory, filename), new_filepath)
                # For WebP files, convert to JPG using webptools
                elif filename.lower().endswith('.webp'):
                    convert_webp_to_jpg(os.path.join(directory, filename), new_filepath)
                # For other image formats, simply copy to new file with .jpg extension
                else:
                    shutil.copyfile(os.path.join(directory, filename), new_filepath)

                # Remove original image file
                os.remove(os.path.join(directory, filename))
            except Exception as e:
                print(f"Error converting {filename}: {e}")
                continue

def resize_images_in_folder(input_folder, output_folder, target_size=(176, 176)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is an image (you can add more image extensions if needed)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image file
            image_path = os.path.join(input_folder, filename)
            image = Image.open(image_path)
            
            # Resize the image
            resized_image = image.resize(target_size)
            
            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            resized_image.save(output_path)

def rename_and_convert_files(directory, prefix):
    # Get list of files in directory
    files = os.listdir(directory)
    
    # Iterate through files
    for index, filename in enumerate(files):
        # Check if file is HEIC or WebP
       # if filename.lower().endswith('.heic'):
            # Convert HEIC to JPG
       #     heif_file = pyheif.read(os.path.join(directory, filename))
       #     image = Image.frombytes(
        #        heif_file.mode, 
        #        heif_file.size, 
        #        heif_file.data,
       #         "raw",
        #        heif_file.mode,
       #         heif_file.stride,
      #      )
       #     new_filename = f"{prefix}_{index + 1}.jpg"
       #     image.save(os.path.join(directory, new_filename))
       #     os.remove(os.path.join(directory, filename))  # Remove the original HEIC file
       # elif filename.lower().endswith('.webp'):
            # Convert WebP to JPG
       #     image = Image.open(os.path.join(directory, filename)).convert("RGB")
       #     new_filename = f"{prefix}_{index + 1}.jpg"
       #     image.save(os.path.join(directory, new_filename))
        #    os.remove(os.path.join(directory, filename))  # Remove the original WebP file
        #else:
            # Construct new filename
        new_filename = f"{prefix}_{index + 1}{os.path.splitext(filename)[1]}"
        
        # Rename file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))


if __name__ == "__main__":
    
    directory = "dataset\dataset\Train"
    
    #convert_to_jpg(directory)
    resize_images_in_folder(directory, directory)
    prefix = "IMG"
    rename_and_convert_files(directory, prefix)