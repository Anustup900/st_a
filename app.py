import streamlit as st
import os
from PIL import Image


def get_image_groups(main_folder):
    image_groups = {}
    subfolders = [f for f in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, f))]

    for subfolder in subfolders:
        subfolder_path = os.path.join(main_folder, subfolder)
        for file in os.listdir(subfolder_path):
            if file.endswith(('png', 'jpg', 'jpeg')):
                base_name = os.path.splitext(file)[0]  # Extract name without extension
                if base_name not in image_groups:
                    image_groups[base_name] = []
                image_groups[base_name].append((subfolder, os.path.join(subfolder_path, file)))

    return image_groups


def main():
    st.title("Image Comparator")
    main_folder = "pinterest_style_dataset"  # Fixed folder path

    if os.path.exists(main_folder):
        image_groups = get_image_groups(main_folder)

        for base_name, images in image_groups.items():
            st.subheader(base_name)
            col_count = len(images)
            cols = st.columns(col_count)

            for i, (experiment, image_path) in enumerate(images):
                with cols[i]:
                    st.text(experiment)
                    img = Image.open(image_path)
                    st.image(img, caption=base_name, use_container_width=True)
    else:
        st.error("Folder does not exist. Please check the folder path.")


if __name__ == "__main__":
    main()