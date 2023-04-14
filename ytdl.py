import argparse
from pytube import YouTube

def main():
    # Create command line argument parser
    parser = argparse.ArgumentParser(description="YouTube Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-v", "--version", action="version", version="v1.1", help="display version number")
    args = parser.parse_args()

    # Create a YouTube object
    try:
        yt = YouTube(args.url)
    except:
        print("Invalid YouTube video URL")
        exit()

    # Get the available video resolutions and audio types
    resolutions = [stream.resolution for stream in yt.streams.filter(progressive=True)]
    audio_types = [stream.abr for stream in yt.streams.filter(only_audio=True)]
    
    # Print the available options
    print("Available download options:")
    print("1. Video")
    print("2. Audio/Song")

    # Ask the user to select an option
    option_selected = input("Enter the number corresponding to the download option you want: ")
    try:
        option_selected = int(option_selected)
    except:
        print("Invalid input. Please enter either 1 or 2.")
        exit()

    if option_selected == 1:
        # Video downloads
        # Print the available resolutions
        print("Available resolutions:")
        for i, res in enumerate(resolutions):
            print(str(i+1) + ". " + res)

        # Let the user select a resolution to download
        selected_res_index = input("Enter the number corresponding to the resolution you want to download: ")
        try:
            selected_res_index = int(selected_res_index)
        except:
            print("Invalid input. Please enter the number corresponding to the selected resolution.")
            exit()

        selected_res_index -= 1
        if selected_res_index < 0 or selected_res_index >= len(resolutions):
            print("Invalid input. Please enter the number corresponding to the selected resolution.")
            exit()

        selected_res = resolutions[selected_res_index]

        # Get the selected video stream
        stream = yt.streams.filter(progressive=True, resolution=selected_res).first()

        # Download the video
        file_name = f"{yt.title}.mp4"
        print("Downloading video with name:", file_name)
        stream.download(filename=file_name)
        print("Download finished!")

    elif option_selected == 2:
        # Audio/Song downloads
        # Print the available audio types
        print("Available audio types:")
        for i, audio_type in enumerate(audio_types):
            print(str(i+1) + ". " + audio_type)

        # Let the user select an audio type to download
        selected_audio_index = input("Enter the number corresponding to the audio type you want to download: ")
        try:
            selected_audio_index = int(selected_audio_index)
        except:
            print("Invalid input. Please enter the number corresponding to the selected audio type.")
            exit()

        selected_audio_index -= 1
        if selected_audio_index < 0 or selected_audio_index >= len(audio_types):
            print("Invalid input. Please enter the number corresponding to the selected audio type.")
            exit()

        selected_audio_type = audio_types[selected_audio_index]

        # Get the selected audio stream
        stream = yt.streams.filter(only_audio=True, abr=selected_audio_type).first()

        # Download the audio
        file_name = f"{yt.title}.mp3"
        print("Downloading audio with name:", file_name)
        stream.download(filename=file_name)
        print("Download finished!")

    else:
        # Invalid option
        print("Invalid input. Please enter either 1 or 2.")
        exit()


if __name__ == "__main__":
    main()
