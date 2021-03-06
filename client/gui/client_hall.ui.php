<?php
	echo '<?xml version="1.0" encoding="UTF-8"?>'."\n";
?>
<ui version="4.0">
 <class>client_hall</class>
 <widget class="QWidget" name="client_hall">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Client Hall</string>
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
   <item row="1" column="0" rowspan="7">
    <widget class="QListView" name="listView_problem"/>
   </item>
   <?php
   	$arrTable=array(
   		'sub'=>'Submit',
   		'ac'=>'Accept',
   		'wa'=>'Wrong Answer',
   		'pe'=>'Presentation Error',
   		'ce'=>'Compile Error',
   		'tle'=>'Time Limit Exceeded',
   		'mle'=>'Memory Limit Exceeded',
   	);
   	$iN = 1;
   	foreach($arrTable as $name => $text){
   		$str= <<<STR
   <item row="$iN" column="2">
    <widget class="QLabel" name="lab_$name">
     <property name="maximumSize">
      <size>
       <width>75</width>
       <height>16777215</height>
      </size>
     </property>
     <property name="text">
      <string>$text</string>
     </property>
     <property name="wordWrap">
      <bool>true</bool>
     </property>
    </widget>
   </item>
   <item row="$iN" column="3">
    <widget class="QListView" name="listView_$name"/>
   </item>
STR;
		echo $str;
		$iN ++;
    }
   ?>
   <item row="0" column="1">
    <widget class="QLabel" name="lab_personal">
     <property name="text">
      <string>personal infomation</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
   </item>
   <item row="2" column="1" rowspan="6">
    <widget class="QListView" name="listView_fresh_news">
     <property name="minimumSize">
      <size>
       <width>450</width>
       <height>0</height>
      </size>
     </property>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
