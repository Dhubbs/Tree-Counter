# Tree-Counter
Counts trees by analysing 1.5 Meter by 1.5 Meter grids in a planted forest.
Uses deep neural networks to classify high quality drone imagery to achive this.

Uses Sklearn MlpClassifier for neural network and Python Imaging Library to interpert photos

This same code should work for any image classifacation task all that is required to change is the size of the pictures that it is trained on and the amount of pictures in the trianing data

To run your self
1. Configure the program and locations
2. Place pictures of trees that are 25*25 pixels in the "Good" directory
3. Place pictures of things that are 25*25 pixels and not trees in the "Bad" directory
4. Place all images to be queued and processed in the ready directory


![1](1.png)


