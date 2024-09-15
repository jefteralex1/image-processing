# image processing

## Description

The `image_processing` package is used for image processing and provides functionalities such as:

### Processing

- **Histogram Matching**: Transfer histogram between images.
- **Structural Similarity**: Compare images to measure structural similarity.
- **Resize Image**: Resize images based on a given proportion.

### Utils

- **Read Image**: Function to read images from files.
- **Save Image**: Function to save images to files.
- **Plot Image**: Function to plot images.
- **Plot Result**: Function to plot multiple images and results.
- **Plot Histogram**: Function to plot histograms of images.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `image_processing`:

```bash
pip install image_processing
```

# Usage
## Image Comparison
To compare two images and find their structural similarity:

```python
from image_processing.processing import find_difference
#Load your images (e.g., using image I/O functions)
image1 = ...
image2 = ...
# Compute the difference between images
difference_image = find_difference(image1, image2)
```

## Histogram Matching
To match the histogram of one image to another:
```python
from image_processing.processing import transfer_histogram

#Load your images
image1 = ...
image2 = ...

#Transfer histogram
matched_image = transfer_histogram(image1, image2)
```

## Image Resizing
To resize an image:

```python
from image_processing.transformation import resize_image

#Load your image
image = ...

#Resize image with a proportion
resized_image = resize_image(image, proportion=0.5)
```

## Image I/O
To read and save images:
```python
from image_processing.utils.io import read_image, save_image

#Read an image
image = read_image('path/to/image.jpg', is_gray=False)

#Save an image
save_image(image, 'path/to/output.jpg')
```

## Image Plotting
To visualize images and their histograms:
```python
from image_processing.plot import plot_image, plot_result, plot_histogram

#Plot a single image
plot_image(image)

#Plot multiple images and results
plot_result(image1, image2, difference_image)

#Plot histogram of an image
 plot_histogram(image)
```

# Module Details
## image_processing.processing
* find_difference(image1, image2): Computes the structural similarity between two images and returns a normalized difference image.
* transfer_histogram(image1, image2): Matches the histogram of image1 to image2 and returns the matched image.

## image_processing.transformation
* resize_image(image, proportion): Resizes the input image by the given proportion (between 0 and 1) and returns the resized image.

## image_processing.utils.io
* read_image(path, is_gray=False): Reads an image from the specified path. Optionally reads in grayscale.
* save_image(image, path): Saves the image to the specified path.

## image_processing.plot
* plot_image(image): Plots a single image.
* plot_result(*args): Plots multiple images in a row with titles.
* plot_histogram(image): Plots the histogram of an image, showing separate histograms for each color channel.

## Contributing
Contributions to the image_processing package are welcome! Please submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
This package utilizes functionalities from scikit-image and matplotlib libraries. Special thanks to their contributors for their valuable work.

## Author
Jefter Alexandre

## License
MIT
