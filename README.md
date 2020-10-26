# Image Batch Processor
CLI tool for batch processing images with ability to listen directory for the new files.

Functions:
- change image file format
- threshold
- blur
- resize
- rotate
- mirroring
- watermarking

---

- [Install](#install)
- [Run](#run)
    - [Change image file format](#change-image-file-format)
    - [Threshold](#threshold)
    - [Blur](#blur)
    - [Resize](#resize)
    - [Rotate](#rotate)
    - [Mirorring](#mirroring)
    - [Watermarking](#watermarking)
- [Dependencies](#dependencies)

## Install
pip3 install -r requirements.txt

## Run
### Change image file format
**python imgtool.py --extension=jpg**  - convert images to jpg format.

Available formats:
* Windows bitmaps - *.bmp, *.dib (always supported)
* JPEG files - *.jpeg, *.jpg, *.jpe (see the Note section)
* JPEG 2000 files - *.jp2 (see the Note section)
* Portable Network Graphics - *.png (see the Note section)
* WebP - *.webp (see the Note section)
* Portable image format - *.pbm, *.pgm, *.ppm *.pxm, *.pnm (always supported)
* PFM files - *.pfm (see the Note section)
* Sun rasters - *.sr, *.ras (always supported)
* TIFF files - *.tiff, *.tif (see the Note section)
* OpenEXR Image files - *.exr (see the Note section)
* Radiance HDR - *.hdr, *.pic (always supported)
* Raster and Vector geospatial data supported by GDAL (see the Note section)
[Documentation](https://docs.opencv.org/4.2.0/d4/da8/group__imgcodecs.html#gabbc7ef1aa2edfaa87772f1202d67e0ce)

### Threshold
**python imgtool.py --action=threshold**  - threshhold images.
default threshold value is 11, to set another value use flag **--threshold=value should be odd number**
example: **python imgtool.py --action=threshold --threshold=5** 

### Blur
**python imgtool.py --action=blur --blur=11** - default blur value is 5, **--blur=value should be odd number**

### Resize
**python imgtool.py --action=resize --scale=25** - default scale value is 50%

### Rotate
**python imgtool.py --action=rotate --degree=25** - default degree value is 90

### Mirroring
**python imgtool.py --action=mirror** - horizontal mirroring only

### Watermarking
**python imgtool.py --action=watermark --watermarkImage=path to image** - add watermark image to bottom left corner

**python imgtool.py --action=watermark --watermarkText=some text** - add watermark text to bottom left corner

---

## Flags
|  Flag | Description   | Default   | Example  |
| ------------ | ------------ | ------------ | ------------ |
| --path     | Path to images | input  | --path=/folderName|
| --watch   | Observe folder for the new files  | False  | --watch |
| --threshhold | Threshold value | 11 | --threshold=11 (should be odd) |
| --blur | Blur value | 5 | --blur=5 (should be odd) |
| --threshAdaptiveMethod | [Documentation](https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#gaa42a3e6ef26247da787bf34030ed772c) | ADAPTIVE_THRESH_MEAN_C | --threshAdaptiveMethod=ADAPTIVE_THRESH_GAUSSIAN_C |
| --threshType | [Documentation](https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#gaa9e58d2860d4afa658ef70a9b1115576) | THRESH_BINARY | --threshType=THRESH_TOZERO |
| --thresholdConstant | | 2 | --thresholdConstant=2 |
| --extension | extension of the output files | png | --extension=jpg |
| --scale | scale persantage | 50 | --scale=25 |
| --degree | Rotation degree | 90 | --degree=45 |
| --watermarkImage | Path to watermark logo | - | --watermarkImage=path |
| --watermarkText | watermark text | -  | --watermarkText=some text |
| --action | User should chose concrete action  | defult | --action=watermark --watermarkText=some text |

---

## Dependencies
- OpenCV https://opencv.org/
- Watchdog https://pypi.org/project/watchdog
    - pip install opencv-python
    - pip install watchdog


---
pyinstaller tbd
