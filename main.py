import sys
#from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
#import main_window
from main_window import Ui_MainWindow

class ExampleApp(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(ExampleApp,self).__init__(parent)
        #super().__init__()
        self.setupUi(self)
        www = self.centralwidget.getContentsMargins()
        print(www)
        self.setWindowTitle('LARK')
        self.ledText = QLineEdit('просто текст',self)
        self.ledText.setGeometry(QtCore.QRect(100,200,200,400))
        #self.ledText.move(100,100)
        self.pushButton.clicked.connect(self.action_push)
        self.label.setText("Заголовок-1")

    def action_push(self):
        a=10
        #print('action push')
        #result = QMessageBox.question(self,'Disk Full ','LARK information')
        #result = QInputDialog.getText(self,'','Ну',text='введите')
        result = QFileDialog.getOpenFileName(self,'','d:/SHARE/dt/','image File (*.jpg)')
        print(result)
def main():
        app=QApplication(sys.argv)
        window = ExampleApp()
        window.show()
        app.exec_()
if __name__ =='__main__':
    main()