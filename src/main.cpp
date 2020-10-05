#include <iostream>
#include <map>
#include <filesystem>

#include "DescriptorProcessor.h"
#include "opencv2/xfeatures2d/nonfree.hpp"
#include "opencv2/calib3d.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"


int main() {

    {// First dataset
        DescriptorProcessor processor("../img_first_dataset/object1.jpeg", "../img_first_dataset/");
        size_t size = processor.getSize();
        printf("Total photos to process: %zu.\n", size);
        if (!size) {
            printf("Error: couldn't load images\n");
            return 1;
        }
        processor.setHaussian(400);
        processor.process();
        std::string metricsFilename = "../results_1.csv";
        processor.saveMetricsToFile(metricsFilename);
    }

    {// Second dataset
        DescriptorProcessor processor("../img_second_dataset/object2.jpg", "../img_second_dataset/");
        size_t size = processor.getSize();
        printf("Total photos to process: %zu.\n", size);
        if (!size) {
            printf("Error: couldn't load images\n");
            return 1;
        }
        processor.setHaussian(400);
        processor.process();
        std::string metricsFilename = "../results_2.csv";
        processor.saveMetricsToFile(metricsFilename);
    }
    return 0;
}