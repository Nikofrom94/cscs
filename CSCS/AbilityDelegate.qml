// delegate for Ranked Abilities

import QtQuick
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick.Controls.Material

ItemDelegate {
    id: delegate
    checkable: true
    width: parent.width
    height: Qt.platform.os == "android" ?
        Math.min(window.width, window.height) * 0.15 :
        Math.min(window.width, window.height) * 0.1

    contentItem:
    RowLayout {
        // first item in a row : rank in a SpinBox
        SpinBox {
            id: rankSpinBox
            from: 1
            to: 6
            font.pixelSize: Qt.platform.os == "android" ?
                Math.min(window.width, window.height) * 0.03 :
                Math.min(window.width, window.height) * 0.02
            value: rank
            elide: Text.ElideRight
            Layout.fillWidth: true
            Layout.preferredWidth: 1
            color: Material.primaryTextColor
        }
        // second item in a row : ability name
        Item {
            Layout.fillWidth: true  // This item will take up the remaining space
        }
        Label {
            text: ab_name
            elide: Text.ElideRight
            font.pixelSize: Qt.platform.os == "android" ?
                Math.min(window.width, window.height) * 0.04 :
                Math.min(window.width, window.height) * 0.02
            Layout.fillWidth: true
            ToolTip.delay: 1000
            ToolTip.timeout: 5000
            ToolTip.visible: hovered
            ToolTip.text: description_tooltip
        }

    }
}
