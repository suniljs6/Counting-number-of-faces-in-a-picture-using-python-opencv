# Counting-number-of-faces-in-a-picture-using-python-opencv

Introduction

The objective of this project is to demonstrate how to detect and count faces in an image, using OpenCV and Python. In this simple example, we will use a Haar feature-based cascade classifier.

The module I have used is the python's computer vision module to do that type
"import cv2".

I have used four functions they are:-
--> cv2.CascadeClassifier()
--> cv2.imread()
--> cv2.cvtColor()
--> detectMultiScale()

So, let's talk in depth about these functions.
firstly,

cv2.CascadeClassifier():-
--                    
          The word “cascade” in the classifier name means that the resultant classifier consists of several simpler classifiers (stages) that are applied subsequently to a region of interest until at some stage the candidate is rejected or all the stages are passed. The word “boosted” means that the classifiers at every stage of the cascade are complex themselves and they are built out of basic classifiers using one of four different boosting techniques (weighted voting). Currently Discrete Adaboost, Real Adaboost, Gentle Adaboost and Logitboost are supported. The basic classifiers are decision-tree classifiers with at least 2 leaves. Haar-like features are the input to the basic classifiers, and are calculated as described below. The current algorithm uses the following Haar-like features:
                    -> Edge features
                    -> Line features
                    -> Center-surrond features
         OpenCV comes with a trainer as well as detector. If you want to train your own classifier for any object like car, planes etc. you can use OpenCV to create one. Its full details are given here: Cascade Classifier Training.

    Here we will deal with detection. OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc. Those XML files are stored in the opencv/data/haarcascades/ folder. Let's create a face and eye detector with OpenCV.

    First we need to load the required XML classifiers. Then load our input image (or video) in grayscale mode. 


cv2.imread():-
--
        The function imread loads an image from the specified file and returns it. If the image cannot be read (because of missing file, improper permissions, unsupported or invalid format), the function returns an empty matrix 
        Currently, the following file formats are supported:
              -> Windows bitmaps - *.bmp, *.dib 
              -> JPEG files - *.jpeg, *.jpg, *.jpe 
              -> JPEG 2000 files - *.jp2
              -> Portable Network Graphics - *.png
              -> WebP - *.webp
              -> Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm
              -> Sun rasters - *.sr, *.ras
              -> TIFF files - *.tiff, *.tif 
              -> OpenEXR Image files - *.exr 
              -> Radiance HDR - *.hdr, *.pic 
              -> Raster and Vector geospatial data supported by Gdal
              
cv2.cvtColor():-
--
         Converts an image from one color space to another.

    The function converts an input image from one color space to another. In case of a transformation to-from RGB color space, the order of the channels should be specified explicitly (RGB or BGR). Note that the default color format in OpenCV is often referred to as RGB but it is actually BGR (the bytes are reversed). So the first byte in a standard (24-bit) color image will be an 8-bit Blue component, the second byte will be Green, and the third byte will be Red. The fourth, fifth, and sixth bytes would then be the second pixel (Blue, then Green, then Red), and so on.

    The conventional ranges for R, G, and B channel values are:

        0 to 255 for CV_8U images
        0 to 65535 for CV_16U images
        0 to 1 for CV_32F images

    In case of linear transformations, the range does not matter. But in case of a non-linear transformation, an input RGB image should be normalized to the proper value range to get the correct results, for example, for RGB → L*u*v* transformation. For example, if you have a 32-bit floating-point image directly converted from an 8-bit image without any scaling, then it will have the 0..255 value range instead of 0..1 assumed by the function. So, before calling cvtColor , you need first to scale the image down:
    img *= 1./255;
    cvtColor(img, img, COLOR_BGR2Luv);

    If you use cvtColor with 8-bit images, the conversion will have some information lost. For many applications, this will not be noticeable but it is recommended to use 32-bit images in applications that need the full range of colors or that convert an image before an operation and then convert back.

    If conversion adds the alpha channel, its value will set to the maximum of corresponding channel range: 255 for CV_8U, 65535 for CV_16U, 1 for CV_32F.

    Parameters
        src	input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision floating-point.
        dst	output image of the same size and depth as src.
        code	color space conversion code (see ColorConversionCodes).
        dstCn	number of channels in the destination image; if the parameter is 0, the number of the channels is derived automatically from src and code.


detectMultiScale():-
--
      We use v2.CascadeClassifier.detectMultiScale() to find faces or eyes, and it is defined like this:

    cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]]) 

    Where the parameters are:

        image : Matrix of the type CV_8U containing an image where objects are detected.
        scaleFactor : Parameter specifying how much the image size is reduced at each image scale. 
