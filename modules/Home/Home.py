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

        # Outer scroll area so it works on smaller screens
        scroll = qt.QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(qt.QFrame.NoFrame)
        scroll.setStyleSheet("background-color: #F4F6FA;")
        self.layout.addWidget(scroll)

        container = qt.QWidget()
        scroll.setWidget(container)
        layout = qt.QVBoxLayout(container)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(0)

        # Logo
        logoLabel = qt.QLabel()
        logoPath = os.path.join(os.path.dirname(__file__), "Resources/Icons/Home.png")
        if os.path.exists(logoPath):
            pixmap = qt.QPixmap(logoPath).scaledToWidth(220, qt.Qt.SmoothTransformation)
            logoLabel.setPixmap(pixmap)
        logoLabel.setAlignment(qt.Qt.AlignCenter)
        layout.addWidget(logoLabel)

        # Tagline
        taglineLabel = qt.QLabel("Transforming the future of neurosurgery")
        taglineLabel.setAlignment(qt.Qt.AlignCenter)
        taglineLabel.setStyleSheet(
            "font-size: 12px; font-family: 'Segoe UI'; color: #5A6E8C; margin-top: 4px; margin-bottom: 24px;"
        )
        layout.addWidget(taglineLabel)

        # Divider
        line = qt.QFrame()
        line.setFrameShape(qt.QFrame.HLine)
        line.setStyleSheet("color: #C5D3E8; margin-bottom: 20px;")
        layout.addWidget(line)

        # Section label
        sectionLabel = qt.QLabel("CLINICAL WORKFLOW")
        sectionLabel.setAlignment(qt.Qt.AlignCenter)
        sectionLabel.setStyleSheet(
            "font-size: 10px; font-family: 'Segoe UI'; font-weight: bold; "
            "color: #5A6E8C; letter-spacing: 2px; margin-bottom: 12px;"
        )
        layout.addWidget(sectionLabel)

        # Workflow buttons
        btnStyle = """
            QPushButton {
                background-color: #0066CC;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 14px 20px;
                font-size: 13px;
                font-family: 'Segoe UI';
                font-weight: bold;
                margin: 5px 0px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #004FA3;
            }
            QPushButton:pressed {
                background-color: #0A2A5E;
            }
        """

        buttons = [
            ("  01  |  Import Patient Data",        "dataImport"),
            ("  02  |  Frame Detection",             "frameDetect"),
            ("  03  |  Registration",                "registration"),
            ("  04  |  Anatomical Landmarks",        "anatomicalLandmarks"),
            ("  05  |  Pre-operative Planning",      "preopPlanning"),
            ("  06  |  Intra-operative Planning",    "intraopPlanning"),
            ("  07  |  Post-operative Localization", "postopLocalization"),
            ("  08  |  Post-operative Programming",  "postopProgramming"),
        ]

        for label, module in buttons:
            btn = qt.QPushButton(label)
            btn.setStyleSheet(btnStyle)
            btn.setMinimumHeight(46)
            btn.clicked.connect(lambda _, m=module: slicer.util.selectModule(m))
            layout.addWidget(btn)

        # Data View secondary button
        dataViewStyle = btnStyle.replace("#0066CC", "#29B6F6").replace("#004FA3", "#0066CC").replace("#0A2A5E", "#004FA3")
        dataViewBtn = qt.QPushButton("  Data View")
        dataViewBtn.setStyleSheet(dataViewStyle)
        dataViewBtn.setMinimumHeight(40)
        dataViewBtn.clicked.connect(lambda: slicer.util.selectModule("dataView"))
        layout.addSpacing(8)
        layout.addWidget(dataViewBtn)

        layout.addStretch()

        # Footer
        footerLabel = qt.QLabel("© 2025 Capla Medical Pvt Ltd, Bangalore  |  For clinical investigation use only")
        footerLabel.setAlignment(qt.Qt.AlignCenter)
        footerLabel.setStyleSheet(
            "font-size: 10px; font-family: 'Segoe UI'; color: #5A6E8C; margin-top: 20px;"
        )
        layout.addWidget(footerLabel)

        slicer.util.mainWindow().setWindowTitle("Capla DBS")
