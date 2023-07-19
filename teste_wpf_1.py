from wpf import *

# Create window
my_window = Window()
my_window.Title = 'Welcome to IronPython'

# Create StackPanel to Layout UI elements 
my_stack = StackPanel()
my_stack.Margin = Thickness(15)
my_window.Content = my_stack

# Create Button and add a Button Click event handler
my_button = Button()
my_button.Content = 'Push Me'
my_button.FontSize = 24
my_button.BitmapEffect = DropShadowBitmapEffect()

def clicker(sender, args):

   # Create new label
   my_message = Label()
   my_message.FontSize = 48
   my_message.Content = 'Welcome to IronPython!'

   # Add label into stack panel of controls
   my_stack.Children.Add (my_message)

my_button.Click += clicker

my_stack.Children.Add (my_button)

# Run application
my_app = Application()
my_app.Run (my_window)
