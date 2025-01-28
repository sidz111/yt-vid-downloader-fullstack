import yt_dlp
import os

def download_video(url, quality='best'):
    # Set options based on selected quality
    ydl_opts = {
        'format': f'{quality}',  # Best, worst, or specific quality
        'outtmpl': '%(title)s.%(ext)s',  # Save file with the video title
        'noplaylist': True,  # Avoid playlist downloads
        'geo_bypass': True,  # Bypass geographic restrictions
        'referer': 'https://www.youtube.com/',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download video and return the file name
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            
            # Move the downloaded file to a proper location if needed
            output_directory = "downloads/"
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            os.rename(filename, os.path.join(output_directory, os.path.basename(filename)))
            filename = os.path.join(output_directory, os.path.basename(filename))
            return filename
    except Exception as e:
        return str(e)


# import yt_dlp

# def download_video(url, quality='best'):
#     # Set options based on selected quality
#     ydl_opts = {
#         'format': f'{quality}',  # Best, worst, or specific quality
#         'outtmpl': '%(title)s.%(ext)s',  # Save file with the video title
#         'noplaylist': True,  # Avoid playlist downloads
#         'geo_bypass': True,  # Bypass geographic restrictions
#         'referer': 'https://www.youtube.com/',
#         'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     }
    
#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             # Download video and return the file name
#             info_dict = ydl.extract_info(url, download=True)
#             filename = ydl.prepare_filename(info_dict)
#             return filename
#     except Exception as e:
#         return str(e)
