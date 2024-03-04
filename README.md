Rock Paper Scissors repository from AI CORE

# Table of Contents
1. How to Install
2. Project Description
3. Instructions of Use
4. File Structure
5. License
6. How to Install
7. Clone the repository using the following command in Linux:


Copy code
git clone "https://github.com/your-username/rockpaperscissorsrepository.git"
Project Description

This is a project I completed in my AI Core course where I was able to tie in:
1. Advanced Python coding
2. Visual machine learning algorithms
3. Command line
4. Error handling

# Instructions of Use
Use this project to play the Rock Paper Scissors game.

File Structure

rockpaperscissorsrepository/
├── README.md
├── rockpaperscissors.py
├── camera_rps.py
├── keras_model.h5
└── ...
License
Copyright (c) 2023 Waqar M Shah

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Update 1:

Improved the game code for better flow and functionality.
Added a while loop to allow multiple rounds of play.
Implemented score tracking and display after each round.
Handled invalid user input more gracefully.
Updated the README file with a table of contents and additional information.

Update 2:

Created a prediction model using Keras (keras_model.h5) for hand gesture recognition.
Integrated the prediction model with the game code to allow the camera to capture hand movements and predict the user's choice.
Added error handling to handle cases where the camera fails to open or capture frames, ensuring a smoother user experience.