# extract text from all the images in a folder 
# storing the text in a single file 
from PIL import Image 
import pytesseract as pt 
import os 

def main(): 
    # get the current working directory
    base_path = os.getcwd()
    
    # path for the folder for getting the raw images 
    images_path = os.path.join(base_path, "")
  
    # link to the file in which output needs to be kept 
    output_file_path = os.path.join(base_path, "output.txt")
    
    # set to store processed image names
    processed_images = set()
    
    # read the output file to find already processed images
    if os.path.exists(output_file_path):
        with open(output_file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.strip() and line.endswith("\n"):
                    processed_images.add(line.strip())

    # iterating the images inside the folder 
    for imageName in os.listdir(images_path): 
        if imageName in processed_images:
            print(f"Skipping already processed image: {imageName}")
            continue
        
        inputPath = os.path.join(images_path, imageName) 
        try:
            img = Image.open(inputPath)
            text = pt.image_to_string(img, lang="eng")
            
            # saving the text for appending it to the output.txt file 
            with open(output_file_path, "a+") as file1:
                # providing the name of the image
                file1.write(imageName + "\n")
                # providing the content in the image
                file1.write(text + "\n")
                # adding a separator between image entries
                file1.write("\n" + "-" * 40 + "\n\n")  # Example separator
                
            # add the processed image name to the set
            processed_images.add(imageName)
        except Exception as e:
            print(f"Error processing {imageName}: {e}")

    # for printing the output file 
    with open(output_file_path, 'r') as file2:
        print(file2.read())

if __name__ == '__main__': 
    main()
