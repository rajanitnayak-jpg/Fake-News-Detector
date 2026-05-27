import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import serial  # For robot connectivity

# Arduino/Robot Connection Setup
# Replace 'COM3' with your actual robot port (e.g., 'COM3' for Windows or '/dev/ttyUSB0' for Linux)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
except Exception as e:
    ser = None
    print("Robot not connected, but you can view the App design.")

class RobotControlApp(App):
    def build(self):
        # Main Layout (Vertical)
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # App Header (Title)
        title = Label(text="Multi-Functional Robot Control", font_size=28, bold=True, size_hint_y=0.15)
        main_layout.add_widget(title)

        # 1. GRASS CUTTING SECTION
        layout1 = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.2)
        layout1.add_widget(Label(text="Grass Cutting:", font_size=18))
        btn_grass_on = Button(text="ON", background_color=(0, 1, 0, 1))
        btn_grass_on.bind(on_press=lambda x: self.send_command('G_ON'))
        btn_grass_off = Button(text="OFF", background_color=(1, 0, 0, 1))
        btn_grass_off.bind(on_press=lambda x: self.send_command('G_OFF'))
        layout1.add_widget(btn_grass_on)
        layout1.add_widget(btn_grass_off)
        main_layout.add_widget(layout1)

        # 2. SEED SPREADING SECTION
        layout2 = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.2)
        layout2.add_widget(Label(text="Seed Spreading:", font_size=18))
        btn_seed_on = Button(text="ON", background_color=(0, 1, 0, 1))
        btn_seed_on.bind(on_press=lambda x: self.send_command('S_ON'))
        btn_seed_off = Button(text="OFF", background_color=(1, 0, 0, 1))
        btn_seed_off.bind(on_press=lambda x: self.send_command('S_OFF'))
        layout2.add_widget(btn_seed_on)
        layout2.add_widget(btn_seed_off)
        main_layout.add_widget(layout2)

        # 3. PESTICIDE SPRAYING SECTION
        layout3 = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.2)
        layout3.add_widget(Label(text="Pesticide Spraying:", font_size=18))
        btn_pest_on = Button(text="ON", background_color=(0, 1, 0, 1))
        btn_pest_on.bind(on_press=lambda x: self.send_command('P_ON'))
        btn_pest_off = Button(text="OFF", background_color=(1, 0, 0, 1))
        btn_pest_off.bind(on_press=lambda x: self.send_command('P_OFF'))
        layout3.add_widget(btn_pest_on)
        layout3.add_widget(btn_pest_off)
        main_layout.add_widget(layout3)

        return main_layout

    # Function to send commands to the robot
    def send_command(self, command):
        print(f"Sent Command: {command}")
        if ser and ser.is_open:
            ser.write((command + '\n').encode())

if __name__ == '__main__':
    RobotControlApp().run()