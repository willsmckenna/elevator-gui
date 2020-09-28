def set_dpi_awareness():
    # to make the resolution/text clearer on the gui
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass