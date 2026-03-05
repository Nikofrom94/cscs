// Copyright (C) 2024 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material
import CSCS

ApplicationWindow {
    id: window
    Material.theme: Material.Dark
    Material.accent: Material.Gray
    width: Screen.width * 0.3
    height: Screen.height * 0.5
    visible: true
    title: qsTr("Cypher System Character Sheet")
    //property var csDirectoryModel
    property var session



    // Add a toolbar for the application, only visible on mobile
    header: ToolBar {
        Material.primary: "#5c8540"
        visible: Qt.platform.os === "android"
        RowLayout {
            anchors.fill: parent
            Label {
                text: qsTr("Cypher System Character Sheet")
                font.pixelSize: 20
                Layout.alignment: Qt.AlignCenter
            }
        }
    }


    CSDirectoryModel{
        id: csDirectoryModel
    }

    SplitView {
        anchors.fill: parent

        // directory of all CS items in a treeview
        TreeView {
            SplitView.preferredWidth: 150
            model: csDirectoryModel
            delegate: CSDirectoryTreeDelegate {}
        }

        // display of clicked item in the directory
        ColumnLayout {
            anchors.fill: parent

            TabBar {
                id: tabBar
                Layout.fillWidth: true

                // TabButton {
                //     text: qsTr("Expenses")
                //     font.pixelSize: Qt.platform.os == "android" ?
                //         Math.min(window.width, window.height) * 0.04 :
                //         Math.min(window.width, window.height) * 0.02
                //     onClicked: stackView.currentIndex = 0
                // }

                // TabButton {
                //     text: qsTr("Charts")
                //     font.pixelSize: Qt.platform.os == "android" ?
                //         Math.min(window.width, window.height) * 0.04 :
                //         Math.min(window.width, window.height) * 0.02
                //     onClicked: stackView.currentIndex = 1
                // }
            }

            StackLayout {
                id: stackView
                Layout.fillWidth: true
                Layout.fillHeight: true

                // Item {
                //     id: expensesView
                //     Layout.fillWidth: true
                //     Layout.fillHeight: true

                //     FinanceView {
                //         id: financeView
                //         anchors.fill: parent
                //         financeModel: finance_model
                //     }
                // }

                // Item {
                //     id: chartsView
                //     Layout.fillWidth: true
                //     Layout.fillHeight: true

                //     FinancePieChart {
                //         id: financePieChart
                //         anchors.fill: parent
                //         Component.onCompleted: {
                //             var categoryData = finance_model.getCategoryData()
                //             updateChart(categoryData)
                //         }
                //     }
                // }
            }
        }


    }


    // Model to store the CS directory
    // CSDirectoryModel {
    //     id: csdirectory_model
    // }

}