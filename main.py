from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy_garden.mapview import MapView

# Booking screen class
class BookingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text="Vehicle Seat Booking"))

        self.seat_spinner = Spinner(
            text='Number of seats(1-4)', values=('1', '2', '3', '4'))
        layout.add_widget(self.seat_spinner)

        self.duration_spinner = Spinner(
            text='Date', values=('Tomorrow', 'One Week', 'One Month'))
        layout.add_widget(self.duration_spinner)

        self.time_spinner = Spinner(
            text='Time', values=('8 AM', '9 AM', '5 PM','6 PM'))
        layout.add_widget(self.time_spinner)

        book_button = Button(text="Book Seat")
        book_button.bind(on_press=self.book_seat)
        layout.add_widget(book_button)

        switch_button = Button(text="Go to Tracking Screen")
        switch_button.bind(on_press=self.switch_to_tracking)
        layout.add_widget(switch_button)

        self.add_widget(layout)

    def book_seat(self, instance):
        print(f"Seats: {self.seat_spinner.text}, "
              f"Duration: {self.duration_spinner.text}, "
              f"Timing: {self.time_spinner.text}")

    def switch_to_tracking(self, instance):
        self.manager.current = 'tracking'  # Switch to tracking screen

# Tracking screen class
class TrackingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
         # Initialize MapView widget, replace with appropriate latitude/longitude
        self.map_view = MapView(zoom=10, lat=37.7749, lon=-122.4194)  # Example: San Francisco
        layout.add_widget(self.map_view)
        
        back_button = Button(text="Go to Booking Screen")
        back_button.bind(on_press=self.switch_to_booking)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def switch_to_booking(self, instance):
        self.manager.current = 'booking'  # Switch back to booking screen

# Main app class
class BookingApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BookingScreen(name='booking'))
        sm.add_widget(TrackingScreen(name='tracking'))
        return sm

if __name__ == '__main__':
    BookingApp().run()
