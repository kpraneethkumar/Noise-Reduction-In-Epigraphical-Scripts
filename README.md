# Epigraphy_Project
Noise reduction using Nested Run Length Count

# Run Length Encoding
Run-length encoding (RLE) is a very simple form of lossless data compression. sequences in which the same data value occurs in many consecutive data elements are stored as a single data value and count, rather than as the original run. This is most useful on data that contains many such runs. for example - WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW can be compressed to 12W1B12W3B24W1B14W. where W represents White pixel and B represents Black pixel

Note- we have to convert the image in binary image.

# Implementation of RLE in this project
insted of taking the count of pixels in a row , take the count of pixels around a pixel . for example if there is a 33 matrix. then the we are counting the RLE for the pixel which is located at the center of the matrix(note- we only take square odd order matrices, since we get a center pixel only in odd oder matrices). as it is a 33 matrix there is only one loop around the center pixel. we count the number of white and black pixels. basically there are 2 cases( center pixel being white or black). if center pixel is white - then the count of white pixels should be greater than the threshold value for 33 matrix.similarly for 55,77 and 99 matrices(with their respective threshold). As the size of matrix increases there will be increase in the number of loops around the pixel. for example lets take 77 matix, here we have 3 loops around the pixel so we first check for immediate loop around the center pixel,(this is the case of 33 matrix) if the count is less than the threshold we change the center pixel to black, else we go to second loop , if the count in the second loop is less than threshold we change it to black else if it is greater than threshold we go to the last loop(i.e 3rd loop) if the count is greater than threshold we don't change the pixel but if it is less than the threshold we change it to black. threshold in my project is ceil (25% of number of pixels in the matrix). threshold can be changed according to the use. similarly if center pixel is black - then the count of black pixels should be greater than the threshold value for 33 matrix.similarly for 55,77 and 99 matrices(with their respective threshold).

# Comparision
we campare our image with the original image using some quality measures like ssim etc.

# Observation
according to the quality measures if we go beyond the 99 matrix the qua;ity of image is reducing that is the noise is starting to increase again. so we can go from 33 matrix to 9*9 matrix.

# Future work
Try to get a better threshold algorithm. Better algorithm for converting RGB image to binary image.
