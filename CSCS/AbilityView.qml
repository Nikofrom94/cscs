//
//

import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

Item {
    property Component current_ab_lang:  ab_lang

    QtObject {
        id: internalSettings
        property color color: "green"
    }

    GridLayout {

    }
}

ListView {
    id: listView
    anchors.fill: parent
    height: parent.height
    property var rankedAbilityModel

    delegate: RankedAbilityDelegate {
        id: delegate
        width: listView.width
    }

    model: rankedAbilityModel

    ScrollBar.vertical: ScrollBar { }
}
