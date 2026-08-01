"""Shared look-and-feel for the Hotel Management System.

Every window imports from here so fonts, colours and spacing stay consistent
instead of being re-invented (differently) in each file.
"""

from tkinter import (BOTH, FLAT, RIDGE, SOLID, Button, Frame, Label, LabelFrame,
                     Canvas, Toplevel, Tk)
from tkinter import ttk

# ---------------------------------------------------------------- palette ---
INK = "#14171C"          # near-black used for headers and primary buttons
INK_DEEP = "#000000"     # true black, matches the logo artwork's own background
INK_LIGHT = "#2A2F38"    # hover / active state for dark surfaces
GOLD = "#C3B499"         # the brand accent this project already used
GOLD_BRIGHT = "#E0D4BC"  # hover state for gold text
PAGE = "#F2EFE9"         # warm off-white page background
CARD = "#FFFFFF"         # panels sitting on the page
BORDER = "#D6CFC2"
TEXT = "#1F2328"
MUTED = "#6E665A"
DANGER = "#8C2F27"

# ------------------------------------------------------------------ fonts ---
# "fantasy" and "times new roman" resolved to inconsistent faces on Windows;
# a single UI family plus one serif display face reads far cleaner.
DISPLAY = ("Georgia", 19, "bold")
TITLE = ("Georgia", 15, "bold")
LABEL = ("Segoe UI Semibold", 10)
BODY = ("Segoe UI", 10)
ENTRY = ("Segoe UI", 10)
BUTTON = ("Segoe UI Semibold", 10)
SMALL = ("Segoe UI", 9)

PAD = 10          # standard gap between elements
ROW_H = 30        # treeview row height


def apply_theme(root):
    """Configure ttk styles once per window."""
    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except Exception:
        pass

    style.configure("Treeview",
                    background=CARD, fieldbackground=CARD, foreground=TEXT,
                    rowheight=ROW_H, font=BODY, borderwidth=0)
    style.configure("Treeview.Heading",
                    background=INK, foreground=GOLD, font=LABEL,
                    relief=FLAT, padding=(6, 8))
    style.map("Treeview.Heading", background=[("active", INK_LIGHT)])
    style.map("Treeview",
              background=[("selected", GOLD)], foreground=[("selected", INK)])

    style.configure("TEntry", fieldbackground=CARD, bordercolor=BORDER,
                    padding=5, relief=FLAT)
    style.configure("TCombobox", fieldbackground=CARD, background=CARD,
                    bordercolor=BORDER, padding=4, arrowsize=14)
    style.map("TCombobox", fieldbackground=[("readonly", CARD)])

    style.configure("Vertical.TScrollbar", background=PAGE, troughcolor=PAGE,
                    bordercolor=PAGE, arrowcolor=MUTED)
    style.configure("Horizontal.TScrollbar", background=PAGE, troughcolor=PAGE,
                    bordercolor=PAGE, arrowcolor=MUTED)

    root.configure(bg=PAGE)
    return style


def fit_window(root, width, height, center=True):
    """Size a window so it always fits on the actual screen, then centre it.

    The old code hardcoded 1550x800, which is wider than many screens -- the
    right-hand edge simply got cut off. This clamps to the usable desktop.
    """
    avail_w = root.winfo_screenwidth()
    avail_h = root.winfo_screenheight() - 60   # leave room for the taskbar
    w = min(width, avail_w)
    h = min(height, avail_h)
    if center:
        x = max(0, (avail_w - w) // 2)
        y = max(0, (avail_h - h) // 3)
    else:
        x = y = 0
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.minsize(min(900, w), min(600, h))
    return w, h


def header(parent, text, width, logo_img=None, height=58):
    """The dark title bar used at the top of every window."""
    bar = Frame(parent, bg=INK, height=height)
    bar.place(x=0, y=0, width=width, height=height)
    if logo_img is not None:
        logo = Label(bar, image=logo_img, bg=INK, bd=0)
        logo.place(x=12, y=4, width=88, height=height - 8)
    Label(bar, text=text, font=DISPLAY, bg=INK, fg=GOLD).place(
        x=118, y=0, height=height)
    return bar


def panel(parent, text):
    """A titled card panel."""
    return LabelFrame(parent, text=" %s " % text, font=TITLE, fg=INK, bg=CARD,
                      bd=1, relief=SOLID, padx=PAD, pady=6)


def primary_button(parent, text, command, width=11):
    return Button(parent, text=text, command=command, font=BUTTON,
                  bg=INK, fg=GOLD, activebackground=INK_LIGHT,
                  activeforeground=GOLD_BRIGHT, relief=FLAT, bd=0,
                  width=width, pady=6, cursor="hand2")


def ghost_button(parent, text, command, width=8):
    return Button(parent, text=text, command=command, font=SMALL,
                  bg=PAGE, fg=INK, activebackground=BORDER,
                  relief=SOLID, bd=1, width=width, pady=1, cursor="hand2")


def field_label(parent, text):
    return Label(parent, text=text, font=LABEL, bg=CARD, fg=TEXT, anchor="w")
