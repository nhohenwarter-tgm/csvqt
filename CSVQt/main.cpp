#include "csvqt.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    CSVQt w;
    w.show();

    return a.exec();
}
