import QtQuick 2.15
import QtQuick.Layouts 1.15

RowLayout {
    id: abilityLayout
    anchors:{
        fill: parent
        margins: 8
    }
    spacing: 1
    Rectangle{
        GridLayout{
            id: ab_textform
            anchors.fill: parent
            columns: 2
            Text { text: "Name"; font.bold: true; }
            TextEdit { id:ab_name; text: ""; }
            Text { text: "Stat"; font.bold: true; }
            TextEdit { id:ab_stat; text: ""; }
            Text { text: "Tier"; font.bold: true; }
            TextEdit { id:ab_tier; text: ""; }
            Text { text: "CS Page"; font.bold: true; }
            TextEdit { id:ab_cs_page; text: ""; }
        }
    }

}
