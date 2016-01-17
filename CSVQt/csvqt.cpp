#include "csvqt.h"
#include "ui_csvqt.h"

CSVQt::CSVQt(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::CSVQt)
{
    ui->setupUi(this);
}

CSVQt::~CSVQt()
{
    delete ui;
}
