# CLI image processing tool
CLI tool for batch processing images with ability to listen directory for the new files.

Functions:
- change image file format
- threshold
- blur*
- resize*
- grayscale*
- rotate*
- mirroring*
- Image Blending (whater sign)*
- Image Denoising*

*TBD

[TOC]

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

---

## Dependencies
- OpenCV https://opencv.org/
- Watchdog https://pypi.org/project/watchdog
    - pip install opencv-python
    - pip install watchdog


---
pyinstaller tbd