#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main() {
    cout << "Hello OpenCV" << CV_VERSION << endl;

    Mat img;
    img = imread("lenna.bmp");

    if (img.empty()) {
        cerr << "image load failed!" << endl;
    }

    namedWindow("image");
    imshow("image", img);

    waitKey();
    return 0;
}