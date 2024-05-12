# helmetDetection (will update project)
 Final term project for CpE EL1 (Artificial Intelligence)

## Introduction: 
This project aims to detect helmets worn by individuals in images or video frames using [Ultralytics](https://github.com/ultralytics/ultralytics). Whether you're concerned with enforcing safety regulations on the road, analyzing footage for research purposes, or any other application where helmet detection is vital, this solution provides an efficient and accurate mechanism.

## Features:
<ul>
    <li> <b>Helmet Detection:</b> Identify motorcycle or bike helmets in images or video streams.
    <li> <b>Real-time Processing:</b> Apply the model to real-time data from webcam source.
    <li> <b> Customizable:</b> The model is adaptable and can be fine-tuned for specific motorcycle or bike helmet types, colors, or environmental conditions.
</li>
</ul>

## Getting Started
To setup this project, follow these steps:
1. Clone the repository using git clone: <br>
`git clone https://github.com/yourusername/motorcycle-helmet-detection.git`
2. Install dependencies: <br>
`pip install -r requirements.txt`

## Usage
To utilize the motorcycle/bike helmet detection system, follow these steps:
1. <b>Live Webcam:</b> Open PyCharm (this is optional but I used it to create the project) and run `main.py`. This will open a window that uses your webcam to detect the helmet. 

2. <b>Image Detection in Folder:</b> Change the folder path of `folder_path = r"C:\Users\Admin\Downloads\helmetDetection\images"` to your desired image folder in `image.py` and run it. (I recommend like 4 images max per use)

3. <b>Video Detection:</b> Change the folder path of `video_path = r"C:\Users\Admin\Downloads\helmetDetection\video\video_0.mp4"` to your desired video folder in `video.py` and run it. (Use only 1 video)

## Sample Output
Here is a sample output of the application using `main.py`: <br>
[Link](https://youtu.be/sE0ksb10GTI)

## Contributing
Contributions are encouraged! Whether it's bug fixes, new features, or improvements, your input is valuable. Here's how you can contribute:

- <b>Bug Reports:</b> Report any bugs or issues encountered.
- <b>Feature Requests:</b> Suggest new features or enhancements.
- <b>Code Contributions:</b> Submit patches, improvements, or new features.

## License
This software is licensed under the MIT license. See [LICENSE]() file for more details