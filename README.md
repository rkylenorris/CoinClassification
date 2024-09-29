# Coin Classification
### Author: R. Kyle Norris


A capstone project for https://learn.365datascience.com/ Python Bootcamp course
using OpenCV to determine coin values from a picture

Picture coins.png supplied for project

## Description from site:
>Capstone Project - Computer Vision
> 
> Working through problems in Python could also be quite a challenging task. 
> However, Python allows us to work on very complicated computational problems 
> even with a limited programming knowledge. In this capstone project we simulate 
> a real-world situation where we are asked to solve an extremely challenging problem, 
> in order to build our research skills.

## Summary of video giving project problem:
>Use library OpenCV to determine the value of the circular coins in the picture
> provided

## My Approach
- Follow along OpenCV tutorial for finding circles using the Hough Circles algorithm
- use a class based structure for the coins
- Feed the data from circles found with OpenCV into the Coin class constructor
- Use the methods found in Coin to determine coin value and type
- write this information back to the original image using OpenCV