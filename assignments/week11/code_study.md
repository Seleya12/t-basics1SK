# Where did you find the code, and why did you choose it? 

Code link: https://github.com/NolanNicholson/Looper/blob/master/loop.py

I found the code while searching for Python projects related to audio and sound. I checked out a few other projects first, but most of them were either way too short or had no real structure. Then I came across this one. It’s a small tool that lets you record audio and loop it – kind of like a mini version of what musicians use when they layer sounds live. I thought it was interesting because it actually does something useful, and I was curious how audio recording and playback works in Python. Also, it seemed like a manageable file to read through – not too long, not too short.

# What does the program do? What's the general structure of the program?

The program records audio from your microphone and plays it back in a loop. You can also overdub, which means recording more audio on top of the loop. It’s all done through the keyboard – you press ‘r’ to record, ‘p’ to play, and ‘q’ to quit. It runs in the terminal and uses the pyaudio and keyboard libraries.

Everything is written in one file: loop.py. At the top, it defines some basic settings like chunk size, format, and sample rate. Then there are a few functions for recording and playing audio. At the bottom, there’s a main() function that listens for key presses and handles the logic. It’s pretty linear and easy to follow once you get used to how the recording works.

# Function analysis: pick one function and analyze it in detail

I looked at the record(frames, stream, seconds=1) function because it's the part that actually captures audio.

What does this function do?

It records audio for a certain number of seconds and stores it in the frames list. Each frame is a small chunk of audio data.

What are the inputs and outputs?

Input:

frames: a list where the recorded audio will be saved
stream: the audio input stream from the mic
seconds: how long to record (default is 1 second)
Output:

It doesn’t return anything. It just updates the frames list.
How does it work (step by step)?

First, it calculates how many chunks it needs to record based on the sample rate and chunk size. Then it loops through that number and reads each chunk from the microphone. Each chunk is added to the frames list. So basically, it grabs small pieces of audio until the full recording time is reached, and then you can use that list to play it back later.

Takeaways: are there anything you can learn from the code?

Yeah, a few things. First, it showed me how audio recording actually works behind the scenes – you don’t just call “record()” and magically get a file. You’re working with streams and small chunks of data. Also, I liked how simple the structure was. It reminded me that even slightly more complex ideas (like a looper) can be broken down into simple steps if you write your code clearly. And the way it handles user input with key presses in real time was something I didn’t know was possible in Python without a GUI.

# What parts of the code were confusing or difficult to understand?

At the beginning, I wasn’t sure what all the constants like CHUNK, FORMAT, and RATE meant or how they affect the audio. I had to look that up. Also, I didn’t fully get how pyaudio streams work at first – especially the idea of reading raw data in chunks and storing them in a list.

# Were you able to understand what it is doing after your own research?

Yes. After looking up a few examples and checking how audio streaming works in Python, it started to make sense. It’s actually a pretty clever way to do a basic looper without needing any complicated GUI or frameworks.

# Extra notes

I chose this code because I really want to do something related to music as my final project. Unfortunately, I only realized afterwards that the code was older than 5 years... I hope it's still okay :) 
