# Usage
# python main.py --type "type of aruco marker" --id "id of the Aruco marker" --output "output folder
# of the generated Aruco marker"
# import the necessary packages
import argparse
import cv2 as cv
import numpy as np
import sys

# Construct an argument parser to parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, type=str,
                help="path to output folder containing Aruco generated images")
ap.add_argument("-i", "--id", required=True, type=int, help="ID of Aruco Tag to generate")
ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL", help="type of Aruco card to generate")
args = vars(ap.parse_args())

# define names of each possible aurco tags opencv can support
ARUCO_DICT = {
    "DICT_4X4_50": cv.aruco.DICT_4X4_50,
    "DICT_4X4_100": cv.aruco.DICT_4X4_100,
    "DICT_4X4_250": cv.aruco.DICT_4X4_250,
    "DICT_4X4_1000": cv.aruco.DICT_4X4_1000,
    "DICT_5X5_50": cv.aruco.DICT_5X5_50,
    "DICT_5X5_100": cv.aruco.DICT_5X5_100,
    "DICT_5X5_250": cv.aruco.DICT_5X5_250,
    "DICT_5X5_1000": cv.aruco.DICT_5X5_1000,
    "DICT_6X6_50": cv.aruco.DICT_6X6_50,
    "DICT_6X6_100": cv.aruco.DICT_6X6_100,
    "DICT_6X6_250": cv.aruco.DICT_6X6_250,
    "DICT_6X6_1000": cv.aruco.DICT_6X6_1000,
    "DICT_7X7_50": cv.aruco.DICT_7X7_50,
    "DICT_7X7_100": cv.aruco.DICT_7X7_100,
    "DICT_7X7_250": cv.aruco.DICT_7X7_250,
    "DICT_7X7_1000": cv.aruco.DICT_7X7_1000,
    "DICT_ARUCO_ORIGINAL": cv.aruco.DICT_ARUCO_ORIGINAL,
    "DICT_APRILTAG_16h5": cv.aruco.DICT_APRILTAG_16h5,
    "DICT_APRILTAG_25h9": cv.aruco.DICT_APRILTAG_25h9,
    "DICT_APRILTAG_36h10": cv.aruco.DICT_APRILTAG_36h10,
    "DICT_APRILTAG_36h11": cv.aruco.DICT_APRILTAG_36h11
}

# verify that ur supplied aruco tag exists and supported by opencv
if ARUCO_DICT.get(args["type"], None) is None:
    print("[INFO] Aruco tag of {} is not supported".format(args["type"]))
    sys.exit(0)

# load the Aruco Dictionary
arucoDict = cv.aruco.Dictionary_get(ARUCO_DICT[args["type"]])

# allocate memory for the output ArUCo tag and then draw the ArUCo
# tag on the output image
print("[INFO] generating ArUCo tag type '{}' with ID '{}'".format(args["type"], args["id"]))
tag = np.zeros((300, 300, 1), dtype="uint8")
cv.aruco.drawMarker(arucoDict, args["id"], 300, tag, 1)

# write the generated ArUCo tag to disk and then display it to our
# screen
cv.imwrite(args["output"], tag)
cv.imshow("ArUCo Tag", tag)
cv.waitKey(0)