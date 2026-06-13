import os
import qt
import slicer
from slicer.ScriptedLoadableModule import *


class Home(ScriptedLoadableModule):
    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = "Home"
        self.parent.categories = [""]
        self.parent.dependencies = []
        self.parent.contributors = ["Capla Medical"]
        self.parent.helpText = "Capla DBS - Deep Brain Stimulation Planning System"
        self.parent.acknowledgementText = "Capla Medical Pvt Ltd, Bangalore"


class HomeWidget(ScriptedLoadableModuleWidget):
    def setup(self):
        ScriptedLoadableModuleWidget.setup(self)

        # Main layout
        layout = qt.QVBoxLayout()
        self.layout.addLayout(layout)

        # Logo
        logoLabel = qt.QLabel()
        logoPath = os.path.join(os.path.dirname(__file__), "Resources/Icons/Home.png")
        if os.path.exists(logoPath):
            pixmap = qt.QPixmap(logoPath).scaledToWidth(300, qt.Qt.SmoothTransformation)
            logoLabel.setPixmap(pixmap)
        logoLabel.setAlignment(qt.Qt.AlignCenter)
        layout.addWidget(logoLabel)

        # Title
        titleLabel = qt.QLabel("Capla DBS")
        titleLabel.setAlignment(qt.Qt.AlignCenter)
        titleLabel.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #1a73e8;
            margin-top: 10px;
        """)
        layout.addWidget(titleLabel)

        # Subtitle
        subtitleLabel = qt.QLabel("Deep Brain Stimulation Planning System")
        subtitleLabel.setAlignment(qt.Qt.AlignCenter)
        subtitleLabel.setStyleSheet("font-size: 14px; color: #555; margin-bottom: 20px;")
        layout.addWidget(subtitleLabel)

        # Divider
        line = qt.QFrame()
        line.setFrameShape(qt.QFrame.HLine)
        line.setStyleSheet("color: #ddd;")
        layout.addWidget(line)

        # Quick launch buttons
        btnStyle = """
            QPushButton {
                background-color: #1a73e8;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 12px;
                font-size: 13px;
                font-weight: bold;
                margin: 4px;
            }
            QPushButton:hover {
                background-color: #1557b0;
            }
        """

        importBtn = qt.QPushButton("Import Patient Data")
        importBtn.setStyleSheet(btnStyle)
        importBtn.clicked.connect(lambda: slicer.util.selectModule("dataImport"))
        layout.addWidget(importBtn)

        planBtn = qt.QPushButton("Pre-operative Planning")
        planBtn.setStyleSheet(btnStyle)
        planBtn.clicked.connect(lambda: slicer.util.selectModule("preopPlanning"))
        layout.addWidget(planBtn)

        frameBtn = qt.QPushButton("Frame Detection")
        frameBtn.setStyleSheet(btnStyle)
        frameBtn.clicked.connect(lambda: slicer.util.selectModule("frameDetect"))
        layout.addWidget(frameBtn)

        intraBtn = qt.QPushButton("Intra-operative Planning")
        intraBtn.setStyleSheet(btnStyle)
        intraBtn.clicked.connect(lambda: slicer.util.selectModule("intraopPlanning"))
        layout.addWidget(intraBtn)

        postBtn = qt.QPushButton("Post-operative Localization")
        postBtn.setStyleSheet(btnStyle)
        postBtn.clicked.connect(lambda: slicer.util.selectModule("postopLocalization"))
        layout.addWidget(postBtn)

        layout.addStretch()

        # Footer
        footerLabel = qt.QLabel("© 2025 Capla Medical Pvt Ltd, Bangalore")
        footerLabel.setAlignment(qt.Qt.AlignCenter)
        footerLabel.setStyleSheet("font-size: 10px; color: #aaa; margin-top: 10px;")
        layout.addWidget(footerLabel)

        # Set window title
        slicer.util.mainWindow().setWindowTitle("Capla DBS")
