import QtQuick 2.0
import QtQuick.Layouts
import QtQuick.Controls

Item {
    ColumnLayout{
        id: mainLayout
        anchors.fill: parent
        GridLayout{
            id: formLayout
            columns: 2
            Layout.fillWidth: true
            Label {
                text: qsTr("Name:")
                Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
            }
            TextField {
                id: item_name
                focus: true
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
            }
            Label {
                text: qsTr("CS Page:")
                Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
            }
            TextField {
                id: item_cs_page
                focus: true
                Layout.fillWidth: true
                Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
            }
        }
        Label {
            text: qsTr("Abilities:")
            Layout.alignment: Qt.AlignLeft | Qt.AlignBaseline
        }
        ListView{
            id: rankedAbilityView
            anchors.fill: parent
            model: rankedAbilitiesModel
            height: parent.height
            delegate: RankedAbilityDelegate{
                id: delegate
                width: rankedAbilityView.width
            }
        }
    }
}

FlavorView{
    id: flavorView

}
