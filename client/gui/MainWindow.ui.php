<?php
	echo '<?xml version="1.0" encoding="UTF-8"?>';
?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>JDMD Online Judge</string>
  </property>
  <widget class="QWidget" name="centralwidget">
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>25</height>
    </rect>
   </property>
   <widget class="QMenu" name="menu_Home_page">
    <property name="title">
     <string>&amp;Home page</string>
    </property>
    <addaction name="action_Home_page"/>
   </widget>
   <widget class="QMenu" name="menu_Practice">
    <property name="title">
     <string>&amp;Practice</string>
    </property>
    <addaction name="action_Show_problem"/>
   </widget>
   <addaction name="menu_Home_page"/>
   <addaction name="menu_Practice"/>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <action name="action_Home_page">
   <property name="text">
    <string>&amp;Home page</string>
   </property>
  </action>
  <action name="action_Show_problem">
   <property name="text">
    <string>&amp;Show problem</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
