import curses

class search:
    def search(self, last_cursor_location, cu, stdscr, buffer, window):
        found = False
        cu.col = 0
        cu.virtual_col = 0
        cu.row = curses.LINES - 1
        stdscr.erase()
        search_string = stdscr.getstr()
        for count, i in enumerate(buffer.lines):
            if search_string in i:
                cu.row = count
                window.h_c = 0
                window.h_w = window.width
                window.w_row = count
                found = True
                break
        if found == False:
            cu.row, cu.col, cu.virtual_col = last_cursor_location[0], last_cursor_location[1], last_cursor_location[2]
        
