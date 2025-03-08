import menu
import loading_screen

def main():
    loading_window = loading_screen.build_loading_screen()
    loading_window.destroy()
    menu.build_menu()
    loading_window.mainloop()

if __name__ == '__main__':
    main()