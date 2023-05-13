from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from kivymd.uix.textfield import MDTextField

from parser import *


class Example(MDApp):
    table = None
    add_dialog = None
    button_for_search = None

    def build(self):
        Window.size = (950, 700)
        Window.top = 100
        Window.left = 200
        layout = MDFloatLayout()
        button_box = MDBoxLayout()

        for button_text in ["Add", "Remove", 'Search']:
            button_box.add_widget(MDRaisedButton(text=button_text, on_release=self.on_button_press))

        self.table = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ('ФИО Студента', dp(35)),
                ('Группа', dp(20)),
                ('По болезни', dp(20)),
                ('По другим причинам', dp(37)),
                ('Без уважительной причины', dp(50)),
                ('Итого', dp(20))
            ],
            row_data=parser()
        )
        self.list_for_delete = []
        self.table.bind(on_check_press=self.button_press)
        layout.add_widget(self.table)
        layout.add_widget(button_box)
        return layout

    def button_press(self, instance_table, instance_row):
        if not instance_row in self.list_for_delete:
            self.list_for_delete.append(instance_row)
        else:
            self.list_for_delete.remove(instance_row)

    def on_button_press(self, instance_button: MDRaisedButton) -> None:

        try:
            {
                "Add": self.add,
                "Remove": self.remove,
                'Search': self.search,
            }[instance_button.text]()
        except KeyError:
            pass

    def add(self) -> None:
        self.diolog_for_new_student()

    def remove(self) -> None:
        for i in range(len(self.list_for_delete)):
            self.table.row_data.remove(tuple(self.list_for_delete[i]))
        self.table.row_data = write(self.table.row_data)
        self.list_for_delete.clear()

    def search(self) -> None:
        self.button_for_searche()

    def button_for_searche(self, *args):
            self.button_for_search = MDDialog(
                title="Search:",
                type="custom",
                buttons=[
                    MDFlatButton(
                        text="ФИО",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.input_search_name
                    ),
                    MDFlatButton(
                        text="Группа",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.input_search_group
                    ),
                    MDFlatButton(
                        text="По виду пропуска",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.chose_pass
                    ),
                ],
            )
            self.button_for_search.open()

# Pass start
    button_for_pass = None

    def chose_pass(self, *args):
        self.button_for_search.dismiss()
        if not self.button_for_pass:
            self.button_for_pass = MDDialog(
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='pass_count_min',
                        hint_text='Количество пропусков(минимальное)',
                    ),
                    MDTextField(
                        id='pass_count_max',
                        hint_text='Количество пропусков(максимальное)',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="100dp"
                ),
                buttons=[
                    MDFlatButton(
                        text="По болезни",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.table_of_search_pass_first
                    ),
                    MDFlatButton(
                        text="По другим причинам",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.table_of_search_pass_second
                    ),
                    MDFlatButton(
                        text="Без уважительной причины",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.table_of_search_pass_third
                    ),
                ],
            )
            self.button_for_pass.open()

    def if_not_pass(self):
        min, max = 0, 1000
        if not self.button_for_pass.content_cls.ids.pass_count_max.text == '':
            max = int(self.button_for_pass.content_cls.ids.pass_count_max.text)
        if not self.button_for_pass.content_cls.ids.pass_count_min.text == '':
            min = int(self.button_for_pass.content_cls.ids.pass_count_min.text)
        return max, min

    # По болезни start

    def return_students_of_pass_first(self):
        max, min = self.if_not_pass()
        rez_of_searching = []
        for i in range(len(self.table.row_data)):
            if int(self.table.row_data[i][2]) >= min and int(self.table.row_data[i][2]) <= max:
                rez_of_searching.append(self.table.row_data[i])
        return rez_of_searching

    search_diolog_for_pass_first = None

    def table_of_search_pass_first(self, *args):
        self.button_for_pass.dismiss()
        rez_of_search = self.return_students_of_pass_first()
        if not self.search_diolog_for_pass_first:
            self.search_diolog_for_pass_first = MDDialog(
                title='По болезни',
                type="custom",
                size_hint_x="0.999",
                content_cls=MDBoxLayout(
                    MDDataTable(
                        use_pagination=True,
                        column_data=[
                            ('ФИО Студента', dp(35)),
                            ('Группа', dp(20)),
                            ('По болезни', dp(20)),
                            ('По другим причинам', dp(37)),
                            ('Без уважительной причины', dp(50)),
                            ('Итого', dp(20))
                        ],
                        row_data=rez_of_search,
                    ),
                    spacing="15dp",
                    size_hint_y=None,
                    height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Remove",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_from_search_table_pass_first
                    ),
                ],
            )
        self.search_diolog_for_pass_first.open()

    def remove_from_search_table_pass_first(self, *args):
        list_for_del = self.return_students_of_pass_first()
        for i in range(len(list_for_del)):
            self.table.row_data.remove(list_for_del[i])
        self.table.row_data = write(self.table.row_data)
        list_for_del.clear()
        self.search_diolog_for_pass_first.dismiss()

    # По болезни end
    # По Другим причинам start
    def return_students_of_pass_second(self):
        max, min = self.if_not_pass()
        rez_of_searching = []
        for i in range(len(self.table.row_data)):
            if int(self.table.row_data[i][3]) >= min and int(self.table.row_data[i][3]) <= max:
                rez_of_searching.append(self.table.row_data[i])
        return rez_of_searching

    search_diolog_for_pass_second = None

    def table_of_search_pass_second(self, *args):
        self.button_for_pass.dismiss()
        rez_of_search = self.return_students_of_pass_second()
        if not self.search_diolog_for_pass_second:
            self.search_diolog_for_pass_second = MDDialog(
                title='По другим причинам',
                type="custom",
                size_hint_x="0.999",
                content_cls=MDBoxLayout(
                    MDDataTable(
                        use_pagination=True,
                        column_data=[
                            ('ФИО Студента', dp(35)),
                            ('Группа', dp(20)),
                            ('По болезни', dp(20)),
                            ('По другим причинам', dp(37)),
                            ('Без уважительной причины', dp(50)),
                            ('Итого', dp(20))
                        ],
                        row_data=rez_of_search,
                    ),
                    spacing="15dp",
                    size_hint_y=None,
                    height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Remove",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_from_search_table_pass_second
                    ),
                ],
            )
        self.search_diolog_for_pass_second.open()

    def remove_from_search_table_pass_second(self, *args):
        list_for_del = self.return_students_of_pass_second()
        for i in range(len(list_for_del)):
            self.table.row_data.remove(list_for_del[i])
        self.table.row_data = write(self.table.row_data)
        list_for_del.clear()
        self.search_diolog_for_pass_second.dismiss()

    # По Другим причинам end
    # Без уважительной причины start
    def return_students_of_pass_third(self):
        max, min = self.if_not_pass()
        rez_of_searching = []
        for i in range(len(self.table.row_data)):
            if int(self.table.row_data[i][4]) >= min and int(self.table.row_data[i][4]) <= max:
                rez_of_searching.append(self.table.row_data[i])
        return rez_of_searching

    search_diolog_for_pass_third = None

    def table_of_search_pass_third(self, *args):
        self.button_for_pass.dismiss()
        rez_of_search = self.return_students_of_pass_third()
        if not self.search_diolog_for_pass_third:
            self.search_diolog_for_pass_third = MDDialog(
                title='По другим причинам',
                type="custom",
                size_hint_x="0.999",
                content_cls=MDBoxLayout(
                    MDDataTable(
                        use_pagination=True,
                        column_data=[
                            ('ФИО Студента', dp(35)),
                            ('Группа', dp(20)),
                            ('По болезни', dp(20)),
                            ('По другим причинам', dp(37)),
                            ('Без уважительной причины', dp(50)),
                            ('Итого', dp(20))
                        ],
                        row_data=rez_of_search,
                    ),
                    spacing="15dp",
                    size_hint_y=None,
                    height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Remove",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_from_search_table_pass_third
                    ),
                ],
            )
        self.search_diolog_for_pass_third.open()

    def remove_from_search_table_pass_third(self, *args):
        list_for_del = self.return_students_of_pass_third()
        for i in range(len(list_for_del)):
            self.table.row_data.remove(list_for_del[i])
        self.table.row_data = write(self.table.row_data)
        list_for_del.clear()
        self.search_diolog_for_pass_third.dismiss()

    # Без уважительной причины end
# Pass end

#Group start

    search_group_diolog = None

    def input_search_group(self, *args):
        self.button_for_search.dismiss()
        if not self.search_group_diolog:
            self.search_group_diolog = MDDialog(
                title='Search',
                type='custom',
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='search_group',
                        hint_text='Группа',
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="100dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Ok",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.table_of_search_group
                    )
                ]
            )

        self.search_group_diolog.open()

    def return_student_of_group(self):
        task = self.search_group_diolog.content_cls.ids.search_group.text
        res_of_search = []
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][1] == task:
                res_of_search.append(self.table.row_data[i])
        return res_of_search

    search_diolog_for_group = None

    def table_of_search_group(self, *args):
        self.search_group_diolog.dismiss()
        rez_of_search = self.return_student_of_group()
        if not self.search_diolog_for_group:
            self.search_diolog_for_group = MDDialog(
                title='Group',
                type="custom",
                size_hint_x="0.999",
                content_cls=MDBoxLayout(
                    MDDataTable(
                        use_pagination=True,
                        column_data=[
                            ('ФИО Студента', dp(25)),
                            ('Группа', dp(20)),
                            ('По болезни', dp(20)),
                            ('По другим причинам', dp(37)),
                            ('Без уважительной причины', dp(50)),
                            ('Итого', dp(20))
                        ],
                        row_data=rez_of_search,
                    ),
                    spacing="15dp",
                    size_hint_y=None,
                    height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Remove",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_from_search_table_group
                    ),
                ],
            )
        self.search_diolog_for_group.open()

    def remove_from_search_table_group(self, *args):
        list_for_del = self.return_student_of_group()
        for i in range(len(list_for_del)):
            self.table.row_data.remove(list_for_del[i])
        self.table.row_data = write(self.table.row_data)
        list_for_del.clear()
        self.search_diolog_for_group.dismiss()

#Group end

#Name start
    search_name_diolog = None

    def input_search_name(self, *args):
            self.button_for_search.dismiss()
            if not self.search_name_diolog:
                self.search_name_diolog = MDDialog(
                        title='Search',
                        type='custom',
                        content_cls=MDBoxLayout(
                            MDTextField(
                                id='search_name',
                                hint_text='ФИО Студента',
                            ),
                            orientation="vertical",
                            spacing="15dp",
                            size_hint_y=None,
                            height="100dp",
                        ),
                        buttons=[
                            MDFlatButton(
                                text="Ok",
                                theme_text_color="Custom",
                                text_color=self.theme_cls.primary_color,
                                on_release=self.table_of_search_name
                            )
                        ]
                    )

            self.search_name_diolog.open()

    def return_student_of_name(self):
        task = self.search_name_diolog.content_cls.ids.search_name.text
        res_of_search = []
        for i in range(len(self.table.row_data)):
            if self.table.row_data[i][0] == task:
                res_of_search.append(self.table.row_data[i])
        return res_of_search

    search_diolog_for_name = None

    def table_of_search_name(self, *args):
        self.search_name_diolog.dismiss()
        rez_of_search = self.return_student_of_name()
        if not self.search_diolog_for_name:
            self.search_diolog_for_name = MDDialog(
                title='Name',
                type="custom",
                size_hint_x="0.999",
                content_cls=MDBoxLayout(
                        MDDataTable(
                            use_pagination=True,
                            column_data=[
                                ('ФИО Студента', dp(35)),
                                ('Группа', dp(20)),
                                ('По болезни', dp(20)),
                                ('По другим причинам', dp(37)),
                                ('Без уважительной причины', dp(50)),
                                ('Итого', dp(20))
                            ],
                            row_data=rez_of_search,
                        ),
                        spacing="15dp",
                        size_hint_y=None,
                        height="505dp",
                ),
                buttons=[
                    MDFlatButton(
                        text="Remove",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.remove_from_search_table_name
                    ),
                ],
            )
        self.search_diolog_for_name.open()

    def remove_from_search_table_name(self, *args):
        list_for_del = self.return_student_of_name()
        for i in range(len(list_for_del)):
            self.table.row_data.remove(list_for_del[i])
        self.table.row_data = write(self.table.row_data)
        list_for_del.clear()
        self.search_diolog_for_name.dismiss()

#Name end

    def diolog_for_new_student(self, *args):
        if not self.add_dialog:
            self.add_dialog = MDDialog(
                title="Add",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        id='name',
                        hint_text="ФИО Студента",
                    ),
                    MDTextField(
                        id='group',
                        hint_text="Группа",
                    ),
                    MDTextField(
                        id='first',
                        hint_text="По болезни",
                    ),
                    MDTextField(
                        id='second',
                        hint_text="По другим причинам",
                    ),
                    MDTextField(
                        id='third',
                        hint_text="Без уважительной причины",
                    ),
                    orientation="vertical",
                    spacing="15dp",
                    size_hint_y=None,
                    height="470dp"
                ),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.close_add_diolog
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.take_info_about_new_student
                    ),
                ],
            )
        self.add_dialog.open()

    def close_add_diolog(self, *args):
        self.add_dialog.dismiss()

    def check_for_clear_add(self):
        temp = []
        for i in self.add_dialog.content_cls.ids:
            if self.add_dialog.content_cls.ids[i].text == '':
                if (i == 'first' or i == 'second' or i == 'third') and self.add_dialog.content_cls.ids[i].text == '':
                    self.add_dialog.content_cls.ids[i].text = '0'
                    continue
                return False
        return True

    def take_info_about_new_student(self, *args):
        if self.check_for_clear_add():
            temp = self.table.row_data
            all = str(int(self.add_dialog.content_cls.ids.second.text) + int(self.add_dialog.content_cls.ids.first.text) + int(self.add_dialog.content_cls.ids.third.text))
            new_student = [self.add_dialog.content_cls.ids.name.text, self.add_dialog.content_cls.ids.group.text, self.add_dialog.content_cls.ids.first.text, self.add_dialog.content_cls.ids.second.text, self.add_dialog.content_cls.ids.third.text, all]
            if not new_student in self.table.row_data:
                temp.append(tuple(new_student))
                temp = write(temp)
                self.table.row_data.clear()
                self.table.row_data = temp
                self.add_dialog.dismiss()
            else:
                self.add_dialog.dismiss()
        else:
            pass



Example().run()