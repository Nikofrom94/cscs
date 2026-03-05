//
//

import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material

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
