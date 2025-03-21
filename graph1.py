import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import pyqtgraph as pg

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)

        self.image_view = pg.ImageView(self.central_widget)
        layout.addWidget(self.image_view)

        # Load an example image (you can replace this with your own image loading logic)
        #example_image = pg.gaussianFilter(pg.np.random.normal(size=(512, 512)), (10, 10))
        pg.gaussianFilter()
        #self.image_view.setImage(example_image)

        self.setWindowTitle("ImageView Example")
        self.setGeometry(100, 100, 800, 600)

        # Get the frame size (dimensions) of the image view
        frame_width = self.image_view.width()
        frame_height = self.image_view.height()
        print("Frame Width:", frame_width)
        print("Frame Height:", frame_height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())