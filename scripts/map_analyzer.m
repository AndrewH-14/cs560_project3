%pixels = imread('small_run1.pgm');
%pixels = imread('small_run2.pgm');
%pixels = imread('small_run3.pgm');
%pixels = imread('maze_run1.pgm');
%pixels = imread('maze_run2.pgm');
%pixels = imread('maze_run3.pgm');

%imshow(pixels);
histogram(pixels);

max_pixel = max(max(pixels));

num_discovered_pixels = size(find(pixels==254),1);

square_meters_discovered = num_discovered_pixels * 0.0025
