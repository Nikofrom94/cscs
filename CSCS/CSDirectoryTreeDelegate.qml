import QtQuick

Item {
    Text {
        anchors.fill: parent
        color: styleData.textColor
        elide: styleData.elideMode
        text: styleData.value.indentation + ": " + styleData.value.text
    }
}
