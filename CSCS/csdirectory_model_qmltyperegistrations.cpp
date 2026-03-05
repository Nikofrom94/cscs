/****************************************************************************
** Generated QML type registration code
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include <QtQml/qqml.h>
#include <QtQml/qqmlmoduleregistration.h>

#if __has_include(</home/niko/Github/cscs/CSCS/csdirectory_model.py>)
#  include </home/niko/Github/cscs/CSCS/csdirectory_model.py>
#endif


#if !defined(QT_STATIC)
#define Q_QMLTYPE_EXPORT Q_DECL_EXPORT
#else
#define Q_QMLTYPE_EXPORT
#endif
Q_QMLTYPE_EXPORT void qml_register_types_CSCS()
{
    QT_WARNING_PUSH QT_WARNING_DISABLE_DEPRECATED
    qmlRegisterTypesAndRevisions<CSDirectoryModel>("CSCS", 1);
    QT_WARNING_POP
    qmlRegisterModule("CSCS", 1, 0);
}

static const QQmlModuleRegistration cSCSRegistration("CSCS", qml_register_types_CSCS);
