from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os
from PIL import Image as PILImage
from PIL import GifImagePlugin

app = QApplication(sys.argv)

class MainWindow(QMainWindow): 
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("GIF Frames Extractor")
        self.setWindowIcon(QIcon('easel.ico'))

        windowLayout = QVBoxLayout()
        headerLayout = QHBoxLayout()
        dirSelectLayout = QHBoxLayout()
        outSelectLayout = QHBoxLayout()
        appRunLayout = QVBoxLayout()

        appHeader = QLabel("GIF Frames Extractor")
        selButton = QPushButton("Input directory")
        selButton.setFixedSize(QSize(100,20))
        outButton = QPushButton("Output directory")
        outButton.setFixedSize(QSize(100,20))
        runButton = QPushButton("Run")
        progBar = QProgressBar(self)
        progBar.setAlignment(Qt.AlignCenter)
        dirLine = QLineEdit("")
        outLine = QLineEdit("")

        def input_directory():
            fileDial = QFileDialog.getExistingDirectory(self, 'Select directory')
            global dirUrl
            dirUrl = fileDial
            dirLine.insert(dirUrl)

        def output_directory():
            fileDial = QFileDialog.getExistingDirectory(self, 'Select directory')
            global outUrl
            outUrl = fileDial
            outLine.insert(outUrl)

        def FrameExtract():
            inputDir = dirUrl
            filesList = os.listdir(inputDir)
            progBar.setMaximum(len(filesList))
            count = 0
            for emoticon in filesList:
                fileName = emoticon[:-4]
                fileExt = emoticon[-4:]
                if fileExt == ".gif":
                    inputGIF = PILImage.open(inputDir + "/" + fileName + fileExt)
                    GIFlength = inputGIF.n_frames

                    if not os.path.exists(outUrl + "/" + fileName):
                        os.mkdir(outUrl + "/" + fileName)

                    for frame in range(0,GIFlength):
                        inputGIF.seek(frame)
                        inputGIF.save(outUrl + "/" + fileName + "/" + fileName + '{:04d}'.format(frame) + ".png")
                else:
                    next
                count += 1
                progBar.setValue(count)
                print(count)

                if count == len(filesList):
                    progBar.setValue(0)
                    msg = QMessageBox()
                    msg.setText("GIF frames extracted")
                    msg.exec_()

        selButton.clicked.connect(input_directory)
        outButton.clicked.connect(output_directory)
        runButton.clicked.connect(FrameExtract)

        headerLayout.addWidget(appHeader)
        headerLayout.setAlignment(Qt.AlignCenter)

        dirSelectLayout.addWidget(selButton)
        dirSelectLayout.addWidget(dirLine)

        outSelectLayout.addWidget(outButton)
        outSelectLayout.addWidget(outLine)

        appRunLayout.addWidget(runButton)
        appRunLayout.addWidget(progBar)

        windowLayout.addLayout(headerLayout)
        windowLayout.addLayout(dirSelectLayout)
        windowLayout.addLayout(outSelectLayout)
        windowLayout.addLayout(appRunLayout)

        widget = QWidget()
        widget.setLayout(windowLayout)
        self.setCentralWidget(widget)

window = MainWindow()
window.setFixedSize(400,150)
window.show()

app.exec_()