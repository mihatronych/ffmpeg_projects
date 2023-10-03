import ffmpeg
from pprint import pprint
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir


# Класс, который нужен для создания окна пользовательского интерфейса
class Ui_MediaDataApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MediaDataApp, self).__init__()
        self.setWindowTitle('Media Data Application')
        self.setGeometry(300, 250, 450, 420)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.createFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.createFileButton.setGeometry(QtCore.QRect(120, 350, 191,
                                                       41))
        self.createFileButton.setObjectName("createFileButton")
        self.createFileButton.clicked.connect(self.createFile)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 330, 401, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.getInforamtionBtn = QtWidgets.QPushButton(self.centralwidget)
        self.getInforamtionBtn.setGeometry(QtCore.QRect(120, 300, 191, 28))
        self.getInforamtionBtn.setObjectName("getInforamtionBtn")
        self.getInforamtionBtn.clicked.connect(self.getInformationFunc)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(200, 140, 20, 150))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 100, 71, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 400, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(17, 120, 391, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.sizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.sizeLabel.setGeometry(QtCore.QRect(20, 140, 181, 20))
        self.inputPath = QtWidgets.QLabel(self.centralwidget)
        self.inputPath.setGeometry(QtCore.QRect(10, 40, 500, 31))
        self.inputPath.setObjectName("inputPath")
        self.inputPath.setFont(font)
        self.inputPath.setText("Input path: ")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.sizeLabel.setFont(font)
        self.sizeLabel.setText("")
        self.sizeLabel.setObjectName("sizeLabel")
        self.resolutionLabel = QtWidgets.QLabel(self.centralwidget)
        self.resolutionLabel.setGeometry(QtCore.QRect(20, 160, 140, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.resolutionLabel.setFont(font)
        self.resolutionLabel.setText("")
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.durationLable = QtWidgets.QLabel(self.centralwidget)
        self.durationLable.setGeometry(QtCore.QRect(20, 180, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.durationLable.setFont(font)
        self.durationLable.setText("")
        self.durationLable.setObjectName("durationLable")
        self.ratioLable = QtWidgets.QLabel(self.centralwidget)
        self.ratioLable.setGeometry(QtCore.QRect(20, 200, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ratioLable.setFont(font)
        self.ratioLable.setText("")
        self.ratioLable.setObjectName("ratioLable")
        self.videoBitRateLabel = QtWidgets.QLabel(self.centralwidget)
        self.videoBitRateLabel.setGeometry(QtCore.QRect(20, 220, 121,
                                                        16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.videoBitRateLabel.setFont(font)
        self.videoBitRateLabel.setText("")
        self.videoBitRateLabel.setObjectName("videoBitRateLabel")
        self.audioSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.audioSizeLabel.setGeometry(QtCore.QRect(230, 140, 141, 16))
        # Опорные координаты
        font = QtGui.QFont()
        font.setPointSize(9)
        self.audioSizeLabel.setFont(font)
        self.audioSizeLabel.setText("")
        self.audioSizeLabel.setObjectName("audioSizeLabel")
        self.audioDurLabel = QtWidgets.QLabel(self.centralwidget)
        self.audioDurLabel.setGeometry(QtCore.QRect(230, 160, 150, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.audioDurLabel.setFont(font)
        self.audioDurLabel.setText("")
        self.audioDurLabel.setObjectName("audioDurLabel")
        self.channelsLabel = QtWidgets.QLabel(self.centralwidget)
        self.channelsLabel.setGeometry(QtCore.QRect(230, 180, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.channelsLabel.setFont(font)
        self.channelsLabel.setText("")
        self.channelsLabel.setObjectName("channelsLabel")
        self.chLayOutLabel = QtWidgets.QLabel(self.centralwidget)
        self.chLayOutLabel.setGeometry(QtCore.QRect(340, 270, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.chLayOutLabel.setFont(font)
        self.chLayOutLabel.setText("")
        self.chLayOutLabel.setObjectName("chLayOutLabel")
        self.codecLabel = QtWidgets.QLabel(self.centralwidget)
        self.codecLabel.setGeometry(QtCore.QRect(230, 200, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.codecLabel.setFont(font)
        self.codecLabel.setText("")
        self.codecLabel.setObjectName("codecLabel")
        self.audioBitRateLabel = QtWidgets.QLabel(self.centralwidget)
        self.audioBitRateLabel.setGeometry(QtCore.QRect(230, 220, 200,
                                                        16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.audioBitRateLabel.setFont(font)
        self.audioBitRateLabel.setText("")
        self.audioBitRateLabel.setObjectName("audioBitRateLabel")
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MediaDataApp):
        _translate = QtCore.QCoreApplication.translate
        MediaDataApp.setWindowTitle(_translate("MediaDataApp", "MediaDataApplication"))
        self.createFileButton.setText(_translate("MediaDataApp", "Create .txt file properties"))
        self.getInforamtionBtn.setText(_translate("MediaDataApp", "Get information"))
        self.label_3.setText(_translate("MediaDataApp", "Instructions: Press 'Get Information' button to choose "
                                                        "file"))
        self.label.setText(_translate("MediaDataApp", "Video:"))
        self.label_2.setText(_translate("MediaDataApp", "Audio:"))

    # Функция привязанная к кнопке создания txt файла
    def createFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())
        probeFile = ffmpeg.probe(str(fileName))
        newInfoFile = open(r"~\\MediaData.txt", "w")
        sys.stdout = newInfoFile
        pprint(probeFile)
        newInfoFile.close()

    # Функция, привязанная к кнопке GetInformation
    def getInformationFunc(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())
        probeFile = ffmpeg.probe(str(fileName))
        self.inputPath.setText("Input path: " +
                               str(ffmpeg.probe(fileName)['format']['filename']))
        for stream in probeFile['streams']:
            if stream['codec_type'] == 'video':
                self.sizeLabel.setText("Size: " + probeFile['format']['size'])
                self.resolutionLabel.setText("Resolution: " + str(stream['width']) + "x"
                                             + str(stream['height']))
                self.durationLable.setText("Duration: " + str(stream['duration']))
                self.ratioLable.setText("Ratio: " + str(stream['display_aspect_ratio']))
                self.videoBitRateLabel.setText("Bit Rate: " + str(stream['bit_rate']))
                audio = next((stream for stream in probeFile['streams'] if
                              stream['codec_type'] == 'audio'), None)
                self.audioSizeLabel.setText("Channels: " + str(audio['channels']))
                self.audioDurLabel.setText("Duration: " + str(audio['duration']))
                self.channelsLabel.setText("Channels layout: " +
                                           str(audio['channel_layout']))
                self.codecLabel.setText("Codec: " + str(audio['codec_name']))
                self.audioBitRateLabel.setText("Bit Rate: " + str(audio['sample_rate']))
            elif stream['codec_type'] == 'audio':
                audio = next((stream for stream in probeFile['streams'] if
                              stream['codec_type'] == 'audio'), None)
                self.audioSizeLabel.setText("Channels: " + str(audio['channels']))
                self.audioDurLabel.setText("Duration: " + str(audio['duration']))
                self.channelsLabel.setText("Channels layout: " +
                                           str(audio['channel_layout']))
                self.codecLabel.setText("Codec: " + str(audio['codec_name']))
                self.audioBitRateLabel.setText("Bit Rate: " + str(audio['sample_rate']))


def application():
    app = QApplication(sys.argv)
    window = Ui_MediaDataApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
