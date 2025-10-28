import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from .Config import Config
from .Gpu import Gpu
from .MainWindow import MainWindow
from . import Common
from . import Libsysmon

_ = Config._tr


class GpuMenu:

    def __init__(self):

        self.name = "GpuMenu"

        self.menu_gui()


    def menu_gui(self):
        """
        Generate menu GUI.
        """

        # Popover
        self.menu_po = Gtk.Popover()

        # Grid (main)
        main_grid = Common.menu_main_grid()
        self.menu_po.set_child(main_grid)

        # Label - menu title (GPU)
        label = Common.menu_title_label(_("GPU"))
        main_grid.attach(label, 0, 0, 2, 1)

        # Button (Graph Color)
        self.graph_color_button = Common.graph_color_button(self)
        main_grid.attach(self.graph_color_button, 0, 1, 2, 1)

        # Separator
        separator = Common.menu_separator()
        main_grid.attach(separator, 0, 2, 2, 1)

        # Button (Reset)
        self.reset_button = Common.reset_button()
        main_grid.attach(self.reset_button, 0, 3, 2, 1)

        # Connect signals
        self.reset_button.connect("clicked", self.on_reset_button_clicked)


    def on_reset_button_clicked(self, widget):
        """
        Reset all tab settings.
        """

        Config.config_default_performance_gpu_func()
        Config.config_save_func()
        Libsysmon.gpu_set_selected_gpu(Gpu.selected_gpu, Gpu.default_gpu, Gpu.gpu_list)

        # Reset device list between Performance tab sub-tabs because selected device is reset.
        MainWindow.main_gui_device_selection_list()

        Common.update_tab_and_menu_gui(self, Gpu)


GpuMenu = GpuMenu()
