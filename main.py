from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock

class ChatBox(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Scrollable chat history area
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.chat_history = Label(size_hint_y=None, markup=True)
        self.chat_history.bind(texture_size=self.update_chat_height)
        self.scroll.add_widget(self.chat_history)
        self.add_widget(self.scroll)

        # Input and send button
        input_area = BoxLayout(size_hint=(1, 0.1))
        self.input = TextInput(multiline=False, hint_text="Type a message...")
        send_btn = Button(text="Send", size_hint=(0.2, 1))
        send_btn.bind(on_press=self.send_message)
        input_area.add_widget(self.input)
        input_area.add_widget(send_btn)
        self.add_widget(input_area)

    def update_chat_height(self, instance, value):
        self.chat_history.height = self.chat_history.texture_size[1]
        Clock.schedule_once(self.scroll_to_bottom, 0)

    def scroll_to_bottom(self, dt):
        # ScrollView.scroll_y ranges from 0 (bottom) to 1 (top) :contentReference[oaicite:0]{index=0}
        self.scroll.scroll_y = 0

    def send_message(self, _):
        text = self.input.text.strip()
        if text:
            self.chat_history.text += f"[b]You:[/b] {text}\n"
            self.input.text = ""

class ChatApp(App):
    def build(self):
        return ChatBox()

if __name__ == "__main__":
    ChatApp().run()
