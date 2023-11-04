import argparse, os
from export import addFilter

def main():
    parser = argparse.ArgumentParser(description="Process images and labels directories")
    parser.add_argument("--images", required=True, help="Path to the images directory")
    parser.add_argument("--labels", required=True, help="Path to the labels directory")

    args = parser.parse_args()
    
    images_dir = args.images
    labels_dir = args.labels

    if not os.path.exists(images_dir):
        print(f"Error: Images directory '{images_dir}' does not exist.")
        return

    if not os.path.exists(labels_dir):
        print(f"Error: Labels directory '{labels_dir}' does not exist.")
        return
    
    addFilter(images_dir, labels_dir)
    
if __name__ == "__main__":
    main()
