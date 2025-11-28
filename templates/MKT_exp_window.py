MKT_exp_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>700</width>
    <height>500</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>700</width>
    <height>500</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>10000</width>
    <height>10000</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Эксперимент</string>
  </property>
  <layout class="QGridLayout" name="gridLayout_2">
   <item row="0" column="0">
    <layout class="QGridLayout" name="gridLayout" columnstretch="2,0">
     <property name="leftMargin">
      <number>10</number>
     </property>
     <property name="topMargin">
      <number>10</number>
     </property>
     <property name="rightMargin">
      <number>10</number>
     </property>
     <property name="bottomMargin">
      <number>10</number>
     </property>
     <item row="1" column="0" colspan="2">
      <widget class="QLabel" name="status">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QTabWidget" name="tabWidget">
       <property name="currentIndex">
        <number>0</number>
       </property>
       <widget class="QWidget" name="tab_3">
        <attribute name="title">
         <string>Главное</string>
        </attribute>
        <layout class="QGridLayout" name="gridLayout_6">
         <item row="0" column="0">
          <layout class="QGridLayout" name="gridLayout_5" rowstretch="1,1,1,1,1,1,1,1,0" columnstretch="0,0,0,0,0">
           <item row="6" column="3" colspan="2">
            <widget class="QLabel" name="label_3">
             <property name="maximumSize">
              <size>
               <width>16777215</width>
               <height>25</height>
              </size>
             </property>
             <property name="text">
              <string>Комментарии:</string>
             </property>
            </widget>
           </item>
           <item row="0" column="3" colspan="2">
            <widget class="QLabel" name="figure_label">
             <property name="text">
              <string>Тело:</string>
             </property>
            </widget>
           </item>
           <item row="2" column="4">
            <widget class="QSpinBox" name="m_spinBox">
             <property name="maximum">
              <number>999999999</number>
             </property>
            </widget>
           </item>
           <item row="1" column="4">
            <widget class="QSpinBox" name="Mr_spinBox">
             <property name="maximum">
              <number>999999999</number>
             </property>
            </widget>
           </item>
           <item row="0" column="2" rowspan="3">
            <widget class="QPushButton" name="start_btn">
             <property name="minimumSize">
              <size>
               <width>75</width>
               <height>75</height>
              </size>
             </property>
             <property name="text">
              <string>Пуск</string>
             </property>
            </widget>
           </item>
           <item row="0" column="1">
            <widget class="QLineEdit" name="expname_lineEdit"/>
           </item>
           <item row="1" column="0">
            <widget class="QLabel" name="label_2">
             <property name="text">
              <string>Среда</string>
             </property>
             <property name="alignment">
              <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
             </property>
            </widget>
           </item>
           <item row="3" column="3">
            <widget class="QLabel" name="corner_label">
             <property name="text">
              <string>концентрация:</string>
             </property>
            </widget>
           </item>
           <item row="0" column="0">
            <widget class="QLabel" name="label">
             <property name="text">
              <string>Название</string>
             </property>
             <property name="alignment">
              <set>Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter</set>
             </property>
            </widget>
           </item>
           <item row="2" column="3">
            <widget class="QLabel" name="speed_label">
             <property name="text">
              <string>масса:</string>
             </property>
            </widget>
           </item>
           <item row="3" column="4">
            <widget class="QSpinBox" name="n_spinBox">
             <property name="maximum">
              <number>999999999</number>
             </property>
            </widget>
           </item>
           <item row="1" column="3">
            <widget class="QLabel" name="mass_label">
             <property name="text">
              <string>молекулярная масса:</string>
             </property>
            </widget>
           </item>
           <item row="4" column="3">
            <widget class="QLabel" name="color_label">
             <property name="text">
              <string>объём:</string>
             </property>
            </widget>
           </item>
           <item row="3" column="0">
            <widget class="QLabel" name="label_5">
             <property name="text">
              <string>Тела:</string>
             </property>
            </widget>
           </item>
           <item row="4" column="4">
            <widget class="QSpinBox" name="V_spinBox">
             <property name="maximum">
              <number>999999999</number>
             </property>
            </widget>
           </item>
           <item row="1" column="1">
            <widget class="QComboBox" name="env_comboBox">
             <property name="cursor">
              <cursorShape>PointingHandCursor</cursorShape>
             </property>
            </widget>
           </item>
           <item row="7" column="3" rowspan="2" colspan="2">
            <widget class="QPlainTextEdit" name="comments_textEdit"/>
           </item>
           <item row="4" column="0" rowspan="4" colspan="3">
            <widget class="QTextBrowser" name="figures_textbrowser"/>
           </item>
           <item row="8" column="1">
            <widget class="QPushButton" name="add_figure_btn">
             <property name="text">
              <string>Добавить тело</string>
             </property>
            </widget>
           </item>
           <item row="5" column="3">
            <widget class="QLabel" name="label_4">
             <property name="text">
              <string>температура(К):</string>
             </property>
            </widget>
           </item>
           <item row="5" column="4">
            <widget class="QSpinBox" name="T_spinBox">
             <property name="maximum">
              <number>999999999</number>
             </property>
            </widget>
           </item>
          </layout>
         </item>
        </layout>
       </widget>
       <widget class="QWidget" name="tab_4">
        <attribute name="title">
         <string>Настройки</string>
        </attribute>
        <layout class="QGridLayout" name="gridLayout_4">
         <item row="0" column="0">
          <layout class="QGridLayout" name="gridLayout_3" rowstretch="2,0,0,0,0,0" columnstretch="1,2,1">
           <item row="0" column="1">
            <widget class="QPushButton" name="save_pushButton">
             <property name="text">
              <string>Сохранить</string>
             </property>
            </widget>
           </item>
           <item row="5" column="1">
            <spacer name="verticalSpacer">
             <property name="orientation">
              <enum>Qt::Vertical</enum>
             </property>
             <property name="sizeHint" stdset="0">
              <size>
               <width>20</width>
               <height>40</height>
              </size>
             </property>
            </spacer>
           </item>
           <item row="3" column="1">
            <widget class="QPushButton" name="help_btn">
             <property name="text">
              <string>Помощь</string>
             </property>
            </widget>
           </item>
           <item row="2" column="1">
            <widget class="QPushButton" name="open_exp_btn">
             <property name="text">
              <string>Открыть эксперимент</string>
             </property>
            </widget>
           </item>
           <item row="1" column="1">
            <widget class="QPushButton" name="delete_btn">
             <property name="text">
              <string>Удалить</string>
             </property>
            </widget>
           </item>
           <item row="1" column="0">
            <spacer name="horizontalSpacer">
             <property name="orientation">
              <enum>Qt::Horizontal</enum>
             </property>
             <property name="sizeHint" stdset="0">
              <size>
               <width>40</width>
               <height>20</height>
              </size>
             </property>
            </spacer>
           </item>
           <item row="2" column="2">
            <spacer name="horizontalSpacer_2">
             <property name="orientation">
              <enum>Qt::Horizontal</enum>
             </property>
             <property name="sizeHint" stdset="0">
              <size>
               <width>40</width>
               <height>20</height>
              </size>
             </property>
            </spacer>
           </item>
           <item row="4" column="1">
            <widget class="QPushButton" name="escape_pushButton">
             <property name="text">
              <string>Выйти</string>
             </property>
            </widget>
           </item>
          </layout>
         </item>
        </layout>
       </widget>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
