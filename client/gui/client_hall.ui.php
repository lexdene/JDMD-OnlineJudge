<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QWidget" name="gridLayoutWidget">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>600</height>
    </rect>
   </property>
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="2" colspan="2">
     <widget class="QLabel" name="lab_most_active_user">
      <property name="text">
       <string>most active user during last 24 hours</string>
      </property>
     </widget>
    </item>
    <item row="0" column="0">
     <widget class="QLabel" name="lab_problem_list">
      <property name="text">
       <string>problem list</string>
      </property>
     </widget>
    </item>
    <item row="2" column="0" rowspan="5">
     <widget class="QListView" name="listView"/>
    </item>
    <?php
    	$arrTable=array(
    		'sub'=>'Submit',
    		'ac'=>'Accept',
    		'wa'=>'Wrong Answer',
    		'pe'=>'Presentation Error',
    		'ce'=>'Compile Error',
    		'tle'=>'Time Limit Exceeded',
    	);
    ?>
    <item row="1" column="2">
     <widget class="QLabel" name="lab_sub">
      <property name="maximumSize">
       <size>
        <width>75</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="text">
       <string>Submit</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="2" column="2">
     <widget class="QLabel" name="lab_ac">
      <property name="maximumSize">
       <size>
        <width>75</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="text">
       <string>Accept</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="3" column="2">
     <widget class="QLabel" name="lab_wa">
      <property name="maximumSize">
       <size>
        <width>75</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="text">
       <string>Wrong Answer</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="4" column="2">
     <widget class="QLabel" name="lab_pe">
      <property name="maximumSize">
       <size>
        <width>75</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="text">
       <string>Presentation Error</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="5" column="2">
     <widget class="QLabel" name="lab_ce">
      <property name="maximumSize">
       <size>
        <width>75</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="text">
       <string>Compile Error</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="6" column="2">
     <widget class="QLabel" name="lab_tle">
      <property name="maximumSize">
       <size>
        <width>75</width>
        <height>16777215</height>
       </size>
      </property>
      <property name="text">
       <string>Time Limit Exceeded</string>
      </property>
      <property name="wordWrap">
       <bool>true</bool>
      </property>
     </widget>
    </item>
    <item row="2" column="3">
     <widget class="QListView" name="listView_ac"/>
    </item>
    <item row="3" column="3">
     <widget class="QListView" name="listView_wa"/>
    </item>
    <item row="4" column="3">
     <widget class="QListView" name="listView_pe"/>
    </item>
    <item row="5" column="3">
     <widget class="QListView" name="listView_ce"/>
    </item>
    <item row="6" column="3">
     <widget class="QListView" name="listView_tle"/>
    </item>
    <item row="0" column="1">
     <widget class="QLabel" name="lab_personal">
      <property name="text">
       <string>personal infomation</string>
      </property>
     </widget>
    </item>
    <item row="4" column="1" rowspan="3">
     <widget class="QListView" name="listView_fresh_news">
      <property name="minimumSize">
       <size>
        <width>450</width>
        <height>0</height>
       </size>
      </property>
     </widget>
    </item>
    <item row="1" column="3">
     <widget class="QListView" name="listView_sub"/>
    </item>
   </layout>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>