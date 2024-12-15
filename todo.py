from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView


class TodoApp(App):
    def build(self):
        self.tasks = []  # List to store tasks

        # Main layout
        self.main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Text input for adding new tasks
        self.input_box = TextInput(hint_text="Enter a task", size_hint_y=None, height=50)
        self.main_layout.add_widget(self.input_box)

        # Button to add a task
        add_button = Button(text="Add Task", size_hint_y=None, height=50, on_press=self.add_task)
        self.main_layout.add_widget(add_button)

        # Scrollable list of tasks
        self.task_list = ScrollView(size_hint=(1, 1))
        self.task_container = BoxLayout(orientation="vertical", size_hint_y=None)
        self.task_container.bind(minimum_height=self.task_container.setter("height"))
        self.task_list.add_widget(self.task_container)
        self.main_layout.add_widget(self.task_list)

        return self.main_layout

    def add_task(self, instance):
        task_text = self.input_box.text.strip()
        if task_text:  # Check if input is not empty
            # Create a new task widget
            task_label = Label(text=task_text, size_hint_y=None, height=40)
            delete_button = Button(text="Delete", size_hint_y=None, height=40, size_hint_x=0.2)

            # Bind the delete button
            delete_button.bind(on_press=lambda btn: self.remove_task(task_label, btn))

            # Task layout
            task_layout = BoxLayout(size_hint_y=None, height=40)
            task_layout.add_widget(task_label)
            task_layout.add_widget(delete_button)

            # Add the task layout to the container
            self.task_container.add_widget(task_layout)
            self.tasks.append(task_text)

            # Clear the input box
            self.input_box.text = ""

    def remove_task(self, task_label, delete_button):
        for widget in self.task_container.children[:]:
            if task_label in widget.children or delete_button in widget.children:
                self.task_container.remove_widget(widget)
                break


if __name__ == "__main__":
    TodoApp().run()
