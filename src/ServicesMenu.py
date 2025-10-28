import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from .Config import Config
from .Services import Services
from .MainWindow import MainWindow
from . import Common

_ = Config._tr


class ServicesMenu:

    def __init__(self):

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

        # Label - menu title (Services)
        label = Common.menu_title_label(_("Services"))
        main_grid.attach(label, 0, 0, 1, 1)

        # Notebook
        notebook = Gtk.Notebook()
        notebook.set_hexpand(True)
        notebook.set_vexpand(True)
        main_grid.attach(notebook, 0, 1, 1, 1)

        # Tab pages and ScrolledWindow
        # "Add/Remove Columns" tab
        label = Gtk.Label()
        label.set_label(_("Add/Remove Columns"))
        self.grid_add_remove_columns_tab = Gtk.Grid()
        self.grid_add_remove_columns_tab.set_margin_top(15)
        self.grid_add_remove_columns_tab.set_margin_bottom(5)
        self.grid_add_remove_columns_tab.set_margin_start(5)
        self.grid_add_remove_columns_tab.set_margin_end(5)
        self.grid_add_remove_columns_tab.set_row_spacing(5)
        notebook.append_page(self.grid_add_remove_columns_tab, label)

        # Button (Reset)
        self.reset_button = Common.reset_button()
        main_grid.attach(self.reset_button, 0, 2, 1, 1)

        # "Add/Remove Columns" tab GUI
        self.add_remove_columns_tab_gui()

        # GUI signals
        self.gui_signals()


    def add_remove_columns_tab_gui(self):
        """
        Generate "Add/Remove Columns" tab GUI objects.
        """

        # Grid
        grid = Gtk.Grid()
        grid.set_margin_top(5)
        grid.set_margin_bottom(5)
        grid.set_margin_start(5)
        grid.set_margin_end(5)
        grid.set_column_spacing(10)
        grid.set_row_spacing(3)
        self.grid_add_remove_columns_tab.attach(grid, 0, 0, 1, 1)

        # Label - tab title (Add/Remove Columns)
        label = Common.title_label(_("Add/Remove Columns"))
        grid.attach(label, 0, 0, 2, 1)

        # CheckButton (Name)
        self.name_cb = Common.checkbutton(_("Name"), None)
        self.name_cb.set_active(True)
        self.name_cb.set_sensitive(False)
        grid.attach(self.name_cb, 0, 1, 1, 1)

        # CheckButton (State)
        self.state_cb = Common.checkbutton(_("State"), None)
        grid.attach(self.state_cb, 0, 2, 1, 1)

        # CheckButton (Main PID)
        self.main_pid_cb = Common.checkbutton(_("Main PID"), None)
        grid.attach(self.main_pid_cb, 0, 3, 1, 1)

        # CheckButton (Active State)
        self.active_state_cb = Common.checkbutton(_("Active State"), None)
        grid.attach(self.active_state_cb, 0, 4, 1, 1)

        # CheckButton (Load State)
        self.load_state_cb = Common.checkbutton(_("Load State"), None)
        grid.attach(self.load_state_cb, 1, 1, 1, 1)

        # CheckButton (Sub-State)
        self.sub_state_cb = Common.checkbutton(_("Sub-State"), None)
        grid.attach(self.sub_state_cb, 1, 2, 1, 1)

        # CheckButton (Memory (RSS))
        self.memory_rss_cb = Common.checkbutton(_("Memory (RSS)"), None)
        grid.attach(self.memory_rss_cb, 1, 3, 1, 1)

        # CheckButton (Description)
        self.description_cb = Common.checkbutton(_("Description"), None)
        grid.attach(self.description_cb, 1, 4, 1, 1)


    def gui_signals(self):
        """
        Connect GUI signals.
        """

        self.menu_po.connect("show", self.on_menu_po_show)
        self.reset_button.connect("clicked", self.on_reset_button_clicked)


    def connect_signals(self):
        """
        Connect some of the signals to be able to disconnect them for setting GUI.
        """

        self.name_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.state_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.main_pid_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.active_state_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.load_state_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.sub_state_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.memory_rss_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)
        self.description_cb.connect("toggled", self.on_add_remove_checkbuttons_toggled)


    def disconnect_signals(self):
        """
        Disconnect some of the signals for setting GUI.
        """

        self.name_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.state_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.main_pid_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.active_state_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.load_state_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.sub_state_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.memory_rss_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)
        self.description_cb.disconnect_by_func(self.on_add_remove_checkbuttons_toggled)


    def on_menu_po_show(self, widget):
        """
        Run code when customizations menu popover is shown.
        """
 
        try:
            self.disconnect_signals()
        except TypeError:
            pass
        self.set_gui()
        self.connect_signals()


    def on_reset_button_clicked(self, widget):
        """
        Reset customizations.
        """

        # Load default settings
        Config.config_default_services_func()
        Config.config_save_func()

        Common.update_tab_and_menu_gui(self, Services)


    def on_add_remove_checkbuttons_toggled(self, widget):
        """
        Run a function for adding/removing columns to treeview.
        """

        self.add_remove_columns()


    def set_gui(self):
        """
        Set GUI items.
        """

        if 0 in Config.services_treeview_columns_shown:
            self.name_cb.set_active(True)
        else:
            self.name_cb.set_active(False)
        if 1 in Config.services_treeview_columns_shown:
            self.state_cb.set_active(True)
        else:
            self.state_cb.set_active(False)
        if 2 in Config.services_treeview_columns_shown:
            self.main_pid_cb.set_active(True)
        else:
            self.main_pid_cb.set_active(False)
        if 3 in Config.services_treeview_columns_shown:
            self.active_state_cb.set_active(True)
        else:
            self.active_state_cb.set_active(False)
        if 4 in Config.services_treeview_columns_shown:
            self.load_state_cb.set_active(True)
        else:
            self.load_state_cb.set_active(False)
        if 5 in Config.services_treeview_columns_shown:
            self.sub_state_cb.set_active(True)
        else:
            self.sub_state_cb.set_active(False)
        if 6 in Config.services_treeview_columns_shown:
            self.memory_rss_cb.set_active(True)
        else:
            self.memory_rss_cb.set_active(False)
        if 7 in Config.services_treeview_columns_shown:
            self.description_cb.set_active(True)
        else:
            self.description_cb.set_active(False)


    def add_remove_columns(self):
        """
        Add/Remove columns to treeview.
        """

        Config.services_treeview_columns_shown = []

        if self.name_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(0)
        if self.state_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(1)
        if self.main_pid_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(2)
        if self.active_state_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(3)
        if self.load_state_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(4)
        if self.sub_state_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(5)
        if self.memory_rss_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(6)
        if self.description_cb.get_active() == True:
            Config.services_treeview_columns_shown.append(7)

        # Apply changes immediately (without waiting update interval).
        Common.treeview_column_order_width_row_sorting(None, None, Services)

        #Common.save_tab_settings(Services)
        Config.config_save_func()


ServicesMenu = ServicesMenu()
