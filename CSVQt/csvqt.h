#ifndef CSVQT_H
#define CSVQT_H

#include <QMainWindow>

namespace Ui {
class CSVQt;
}

class CSVQt : public QMainWindow
{
    Q_OBJECT

public:
    explicit CSVQt(QWidget *parent = 0);
    ~CSVQt();

private:
    Ui::CSVQt *ui;
};

#endif // CSVQT_H
