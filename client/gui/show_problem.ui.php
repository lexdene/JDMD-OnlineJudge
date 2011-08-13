<?php
	echo '<?xml version="1.0" encoding="UTF-8"?>'
?>
<ui version="4.0">
 <class>show_problem</class>
 <widget class="QWidget" name="show_problem">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>show problem</string>
  </property>
  <layout class="QGridLayout" name="gridLayout">
   <item row="1" column="0" rowspan="7">
    <widget class="QTextBrowser" name="textBrowser"/>
   </item>
   <item row="0" column="0">
    <widget class="QLabel" name="lab_problem_title">
     <property name="text">
      <string>problem title</string>
     </property>
    </widget>
   </item>
   <item row="0" column="1">
    <widget class="QLabel" name="lab_record">
     <property name="text">
      <string>record</string>
     </property>
    </widget>
   </item>
<?php
	$arrList=array(
		'least_time'=>'least time',
		'least_memory'=>'least memory',
		'shortest_code'=>'shortest code'
	);
	$iN=0;
	foreach($arrList as $name => $text)
	{
		$row1= $iN * 2 +1;
		$row2=$row1+1;
		$str=<<<STR
   <item row="$row1" column="1">
    <widget class="QLabel" name="lab_$name">
     <property name="text">
      <string>$text</string>
     </property>
    </widget>
   </item>
   <item row="$row2" column="1">
    <widget class="QListView" name="listView_$name"/>
   </item>

STR;
		echo $str;
		$iN++;
	}
?>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
