import os
from random import choice
import shutil


def split(train_ratio,test_ratio,trainPath,valPath,testPath,crsPath):
    # arrays to store file names
    imgs = []
    txt_files = []

    # total count of imgs
    totalImgCount = len(os.listdir(crsPath)) / 2

    # soring files to corresponding arrays
    for (dirname, dirs, files) in os.walk(crsPath):
        for filename in files:
            if filename.endswith('.txt'):
                txt_files.append(filename)
            else:
                imgs.append(filename)

    # counting range for cycles
    countForTrain = int(len(imgs) * train_ratio)
    countForTest = int(len(imgs) * test_ratio)

    # cycle for train dir
    for x in range(countForTrain):
        jpgFile = choice(imgs)  # get name of random image from origin dir
        txtFile = jpgFile[:-4] + '.txt'  # get name of corresponding annotation file

        # move both files into train dir
        shutil.move(os.path.join(crsPath, jpgFile), os.path.join(trainPath, jpgFile))
        if os.path.exists(crsPath + "/" + txtFile):
            shutil.move(os.path.join(crsPath, txtFile), os.path.join(trainPath, txtFile))
            txt_files.remove(txtFile)

        # remove files from arrays
        imgs.remove(jpgFile)

    # cycle for test dir
    for x in range(countForTest):
        jpgFile = choice(imgs)  # get name of random image from origin dir
        txtFile = jpgFile[:-4] + '.txt'  # get name of corresponding annotation file

        # move both files into train dir
        shutil.move(os.path.join(crsPath, jpgFile), os.path.join(testPath, jpgFile))
        if os.path.exists(crsPath + "/" + txtFile):
            shutil.move(os.path.join(crsPath, txtFile), os.path.join(trainPath, txtFile))
            txt_files.remove(txtFile)

        # remove files from arrays
        imgs.remove(jpgFile)

    # rest of files will be validation files, so rename origin dir to val dir
    os.rename(crsPath, valPath)

    # summary information after splitting
    print('Total images: ', totalImgCount)
    print('Images in train dir:', len(os.listdir(trainPath)) / 2)
    print('Images in test dir:', len(os.listdir(testPath)) / 2)
    print('Images in validation dir:', len(os.listdir(valPath)) / 2)


if __name__ == '__main__':
    split(
    # setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
    train_ratio = 0.7,
    test_ratio = 0.2,

    # setup dir names
    trainPath ='',
    valPath ='',
    testPath ='',
    crsPath =''  # dir where images and annotations stored

    )


