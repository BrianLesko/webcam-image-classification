
# Real Time Image Classifier

This code classifies the webcam feed into 1000 different categories mostly consisting of animals, vehicles, furniture, and tools.

I was able to run this code at ~ 11.5 fps on my macbook pro webcam.

&nbsp;

<div align="center"><img src="docs/preview.png" width="800"></div>

&nbsp;

## Dependencies

`Streamlit` - for the web interface
`pytorch` - to download the Machine learning model and run it
`opencv` - to fetch the camera feed from your device
`pillow` - python image library for converting from opencv to torchvision format

To run, use the following commands in your terminal:
```
python3 -m venv my_env
source my_env/bin/activate # or on windows: source my_env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

to stop the app, go back to the terminal and press control C

This will start the local Streamlit server, and you can access the chatbot by opening a web browser and navigating to `http://localhost:8501`.

&nbsp;

<hr>

&nbsp;

<div align="center">



╭━━╮╭━━━┳━━┳━━━┳━╮╱╭╮        ╭╮╱╱╭━━━┳━━━┳╮╭━┳━━━╮
┃╭╮┃┃╭━╮┣┫┣┫╭━╮┃┃╰╮┃┃        ┃┃╱╱┃╭━━┫╭━╮┃┃┃╭┫╭━╮┃
┃╰╯╰┫╰━╯┃┃┃┃┃╱┃┃╭╮╰╯┃        ┃┃╱╱┃╰━━┫╰━━┫╰╯╯┃┃╱┃┃
┃╭━╮┃╭╮╭╯┃┃┃╰━╯┃┃╰╮┃┃        ┃┃╱╭┫╭━━┻━━╮┃╭╮┃┃┃╱┃┃
┃╰━╯┃┃┃╰┳┫┣┫╭━╮┃┃╱┃┃┃        ┃╰━╯┃╰━━┫╰━╯┃┃┃╰┫╰━╯┃
╰━━━┻╯╰━┻━━┻╯╱╰┻╯╱╰━╯        ╰━━━┻━━━┻━━━┻╯╰━┻━━━╯
  


&nbsp;


<a href="https://x.com/TheBrianLesko/status/1124018912268554240">Brian Lesko's X Post<img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/main/.socials/svg-grey/x.svg" width="30" alt="Brian Lesko's X Logo"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://github.com/BrianLesko">Brian Lesko's GitHub<img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/main/.socials/svg-grey/github.svg" width="30" alt="Brian Lesko's GitHub Logo"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://www.linkedin.com/in/brianlesko/">Brian Lesko's LinkedIn<img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/main/.socials/svg-grey/linkedin.svg" width="30" alt="Brian Lesko's LinkedIn Logo"></a>

follow all of these for a cookie :)

</div>


&nbsp;


