import exifread
import sys
import os
from PIL import Image

def get_decimal_from_dms(dms, ref):
    """
    Converts GPS coordinates from DMS (Degrees, Minutes, Seconds) 
    format to Decimal Degrees.
    """
    try:
        degrees = dms[0].num / dms[0].den
        minutes = dms[1].num / dms[1].den
        seconds = dms[2].num / dms[2].den

        decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)

        if ref in ['S', 'W']:
            decimal = -decimal
            
        return decimal
    except Exception as e:
        return None

def extract_metadata(image_path):
    # Verify file exists
    if not os.path.exists(image_path):
        print(f"Error: The file '{image_path}' was not found.")
        return

    # 1. Open image file for reading (binary mode)
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            
        print(f"\n--- Metadata for: {os.path.basename(image_path)} ---")
        print("-" * 50)

        # 2. Extract Basic Camera Data
        make = tags.get('Image Make', 'Unknown')
        model = tags.get('Image Model', 'Unknown')
        date_time = tags.get('EXIF DateTimeOriginal', tags.get('Image DateTime', 'Unknown'))
        
        print(f"Camera Make:    {make}")
        print(f"Camera Model:   {model}")
        print(f"Date Taken:     {date_time}")

        # 3. Extract Shot Settings
        exposure = tags.get('EXIF ExposureTime', 'Unknown')
        f_number = tags.get('EXIF FNumber', 'Unknown')
        iso = tags.get('EXIF ISOSpeedRatings', 'Unknown')
        
        print(f"Shutter Speed:  {exposure} sec")
        print(f"Aperture:       f/{f_number}")
        print(f"ISO:            {iso}")

        # 4. Extract and Convert GPS Data
        gps_lat = tags.get('GPS GPSLatitude')
        gps_lat_ref = tags.get('GPS GPSLatitudeRef')
        gps_long = tags.get('GPS GPSLongitude')
        gps_long_ref = tags.get('GPS GPSLongitudeRef')

        if gps_lat and gps_long and gps_lat_ref and gps_long_ref:
            lat = get_decimal_from_dms(gps_lat.values, gps_lat_ref.values)
            lon = get_decimal_from_dms(gps_long.values, gps_long_ref.values)

            print("-" * 50)
            print("GPS Coordinates Found:")
            print(f"Latitude:  {lat:.6f}")
            print(f"Longitude: {lon:.6f}")
            print(f"Google Maps Link: https://www.google.com/maps?q={lat},{lon}")
        else:
            print("-" * 50)
            print("No GPS data found in this image.")
            
        print("-" * 50 + "\n")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Metadata_Extractor.py <path_to_image>")
    else:
        image_path = sys.argv[1]
        extract_metadata(image_path)