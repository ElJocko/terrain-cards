import svgwrite

from collections import namedtuple

Point = namedtuple('Point', 'x y')
Size = namedtuple('Size', 'width height')
Terrain_Placement = namedtuple('Terrain_Placement', 'box_x box_y position')

# image_width = 1122
# image_height= 822
#
# cut_area_width = 1050
# cut_area_height = 750
#
# safe_area_width = 978
# safe_area_height = 678
#
# box_size = 320
# line_width = 4
# terrain_radius = 60
# terrain_edge_width = 25
# bottom_text_height = 26

card_type = 'regular-no-margin'
# card_type = 'grand6x2'

if card_type == 'regular':
    # regular triumph terrain cards are on poker size cards
    image_width = 1125
    image_height= 825

    cut_area_width = 1050
    cut_area_height = 750

    safe_area_width = 975
    safe_area_height = 675

    box_size = 320
    box_count_x = 3
    box_count_y = 2

    line_width = 4
    line_offset = line_width / 2

    terrain_radius = 60
    terrain_edge_width = 25
    bottom_text_height = 34

    terrain_label_font_size = '64px'

    terrain_edge_label_offset_x = 30
    terrain_edge_label_offset_y1 = 20
    terrain_edge_label_offset_y2 = 15
    terrain_edge_label_offset_y3 = 58

    stream_label_offset_x = 18
    stream_label_offset_y1 = 15
    stream_label_offset_y2 = 9
    stream_label_offset_y3 = 37

    stream_width = 80
    stream_height = 67

    # (left, middle, right)
    board_left_x = 74
    board_top_y = 73
    board_right_x = board_left_x + (box_count_x * box_size) + ((box_count_x - 1) * line_width)
    board_bottom_y = board_top_y + (box_count_y * box_size) + ((box_count_y - 1) * line_width)
    board_x = (board_left_x, ((board_left_x + board_right_x) / 2), board_right_x)
    board_y = (board_top_y, ((board_top_y + board_bottom_y) / 2), board_bottom_y)

    column_x = board_left_x
    column_1_x = (column_x + line_width, column_x + line_width + (box_size / 2), column_x + line_width + box_size)

    column_x = column_1_x[2] + line_width
    column_2_x = (column_x + line_width, column_x + line_width + (box_size / 2), column_x + line_width + box_size)

    column_x = column_2_x[2] + line_width
    column_3_x = (column_x + line_width, column_x + line_width + (box_size / 2), column_x + line_width + box_size)

    row_y = board_top_y
    row_1_y = (row_y + line_width, row_y + line_width + (box_size / 2), row_y + line_width + box_size)

    row_y = row_1_y[2] + line_width
    row_2_y = (row_y + line_width, row_y + line_width + (box_size / 2), row_y + line_width + box_size)

    version_number = 'v1'

elif card_type == 'regular-no-margin':
    # regular triumph terrain cards are on poker size cards
    image_width = 976
    image_height= 679

    cut_area_width = 1050
    cut_area_height = 750

    safe_area_width = 975
    safe_area_height = 675

    box_size = 320
    box_count_x = 3
    box_count_y = 2

    line_width = 4
    line_offset = line_width / 2

    terrain_radius = 60
    terrain_edge_width = 25
    bottom_text_height = 34

    terrain_label_font_size = '64px'

    terrain_edge_label_offset_x = 30
    terrain_edge_label_offset_y1 = 20
    terrain_edge_label_offset_y2 = 15
    terrain_edge_label_offset_y3 = 58

    stream_label_offset_x = 18
    stream_label_offset_y1 = 15
    stream_label_offset_y2 = 9
    stream_label_offset_y3 = 37

    stream_width = 80
    stream_height = 67

    # (left, middle, right)
    board_left_x = 0
    board_top_y = 0
    board_right_x = board_left_x + (box_count_x * box_size) + ((box_count_x - 1) * line_width)
    board_bottom_y = board_top_y + (box_count_y * box_size) + ((box_count_y - 1) * line_width)
    board_x = (board_left_x, ((board_left_x + board_right_x) / 2), board_right_x)
    board_y = (board_top_y, ((board_top_y + board_bottom_y) / 2), board_bottom_y)

    column_x = board_left_x
    column_1_x = (column_x + line_width, column_x + line_width + (box_size / 2), column_x + line_width + box_size)

    column_x = column_1_x[2] + line_width
    column_2_x = (column_x + line_width, column_x + line_width + (box_size / 2), column_x + line_width + box_size)

    column_x = column_2_x[2] + line_width
    column_3_x = (column_x + line_width, column_x + line_width + (box_size / 2), column_x + line_width + box_size)

    row_y = board_top_y
    row_1_y = (row_y + line_width, row_y + line_width + (box_size / 2), row_y + line_width + box_size)

    row_y = row_1_y[2] + line_width
    row_2_y = (row_y + line_width, row_y + line_width + (box_size / 2), row_y + line_width + box_size)

    version_number = 'v1'

elif card_type == 'grand6x2':
    # grand triumph terrain cards are on tarot size cards with a 6 x 2 layout
    image_width = 1500
    image_height = 900

    cut_area_width = 1425
    cut_area_height = 825

    safe_area_width = 1350
    safe_area_height = 750

    box_size = 225
    box_count_x = 6
    box_count_y = 2

    line_width = 4
    line_offset = line_width / 2

    terrain_radius = 44
    terrain_edge_width = 18
    bottom_text_height = 34

    terrain_label_font_size = '56px'

    terrain_edge_label_offset_x = 30
    terrain_edge_label_offset_y1 = 20
    terrain_edge_label_offset_y2 = 10
    terrain_edge_label_offset_y3 = 53

    stream_label_offset_x = 18
    stream_label_offset_y1 = 15
    stream_label_offset_y2 = 9
    stream_label_offset_y3 = 37

    stream_width = 80
    stream_height = 67

    # (left, middle, right)
    board_left_x = 63
    board_top_y = 219
    board_right_x = board_left_x + (box_count_x * box_size) + ((box_count_x - 1) * line_width)
    board_bottom_y = board_top_y + (box_count_y * box_size) + ((box_count_y - 1) * line_width)
    board_x = (board_left_x, ((board_left_x + board_right_x) / 2), board_right_x)
    board_y = (board_top_y, ((board_top_y + board_bottom_y) / 2), board_bottom_y)

    column_x = board_left_x
    column_1_x = (column_x + line_width, int(column_x + line_width + (box_size / 2)), column_x + box_size)

    column_x = column_1_x[2]
    column_2_x = (column_x, int(column_x + line_width + (box_size / 2)), column_x + box_size)

    column_x = column_2_x[2]
    column_3_x = (column_x, int(column_x + line_width + (box_size / 2)), column_x + box_size)

    row_y = board_top_y
    row_1_y = (row_y + line_width, int(row_y + line_width + (box_size / 2)), row_y + box_size)

    row_y = row_1_y[2]
    row_2_y = (row_y, int(row_y + line_width + (box_size / 2)), row_y + box_size)

    version_number = 'gt v2'

elif card_type == 'grand':
    # grand triumph terrain cards are on tarot size cards
    image_width = 1500
    image_height= 900

    cut_area_width = 1425
    cut_area_height = 825

    safe_area_width = 1350
    safe_area_height = 750

    box_size = 270
    box_count_x = 5
    box_count_y = 2

    line_width = 4
    line_offset = line_width / 2

    terrain_radius = 50
    terrain_edge_width = 20
    bottom_text_height = 34

    terrain_label_font_size = '64px'

    terrain_edge_label_offset_x = 30
    terrain_edge_label_offset_y1 = 20
    terrain_edge_label_offset_y2 = 10
    terrain_edge_label_offset_y3 = 53

    stream_label_offset_x = 18
    stream_label_offset_y1 = 15
    stream_label_offset_y2 = 9
    stream_label_offset_y3 = 37

    stream_width = 80
    stream_height = 67

    # (left, middle, right)
    board_left_x = 63
    board_top_y = 174
    board_right_x = board_left_x + (box_count_x * box_size) + ((box_count_x - 1) * line_width)
    board_bottom_y = board_top_y + (box_count_y * box_size) + ((box_count_y - 1) * line_width)
    board_x = (board_left_x, ((board_left_x + board_right_x) / 2), board_right_x)
    board_y = (board_top_y, ((board_top_y + board_bottom_y) / 2), board_bottom_y)

    column_x = board_left_x
    column_1_x = (column_x + line_width, int(column_x + line_width + (box_size / 2)), column_x + box_size)

    column_x = column_1_x[2]
    column_2_x = (column_x, int(column_x + line_width + (box_size / 2)), column_x + box_size)

    column_x = column_2_x[2]
    column_3_x = (column_x, int(column_x + line_width + (box_size / 2)), column_x + box_size)

    row_y = board_top_y
    row_1_y = (row_y + line_width, int(row_y + line_width + (box_size / 2)), row_y + box_size)

    row_y = row_1_y[2]
    row_2_y = (row_y, int(row_y + line_width + (box_size / 2)), row_y + box_size)

    version_number = 'gt v2'

coast_color = '#0067b2'
stream_color = '#0067b2'
terrain_color = '#504416'

# ( card_number, coast_pos, terrain1, t2, t3, t4, t5, t6, stream1, stream2)
# card_config = [
#     ( 1, 0, [(6, 1, 3), (6, 2, 5), (2, 1, 5), (1, 1, 3), (5, 1, 1), (1, 2, 5), (6, 1, 6), (2, 2, 4), (2, 1, 2), (5, 2, 8)], (6, 1, 1), (6, 2, 3)),
#     ( 2, 0, [(6, 2, 3), (1, 2, 3), (5, 2, 5), (2, 1, 3), (1, 1, 1), (4, 2, 2), (5, 2, 2), (6, 1, 1), (1, 1, 5), (2, 2, 4)], (6, 1, 3), (6, 2, 5)),
#     ( 3, 0, [(6, 2, 3), (6, 1, 5), (1, 2, 4), (3, 1, 6), (1, 1, 1), (5, 1, 1), (2, 2, 4), (2, 2, 1), (2, 1, 2), (5, 2, 8)], (6, 1, 1), (6, 2, 5)),
#     ( 4, 0, [(6, 2, 3), (1, 2, 1), (2, 2, 2), (5, 1, 1), (5, 2, 5), (2, 1, 2), (1, 2, 4), (1, 1, 1), (6, 1, 7), (2, 1, 7)], (6, 1, 1), (6, 2, 5)),
#     ( 5, 1, [(1, 1, 7), (2, 2, 1), (5, 2, 3), (1, 2, 6), (5, 1, 1), (6, 1, 7), (3, 1, 4), (2, 2, 4), (2, 1, 1), (1, 2, 3)], (1, 1, 1), (1, 2, 7)),
#     ( 6, 0, [(6, 1, 3), (2, 2, 4), (1, 1, 1), (4, 1, 6), (6, 2, 5), (2, 1, 2), (6, 2, 8), (1, 1, 4), (5, 1, 3), (1, 2, 5)], (5, 1, 1), (6, 2, 3)),
#     ( 7, 1, [(1, 1, 7), (2, 2, 8), (6, 2, 6), (5, 1, 8), (2, 2, 5), (3, 1, 6), (5, 2, 7), (2, 1, 2), (1, 1, 3), (6, 1, 1)], (2, 1, 1), (1, 2, 5)),
#     ( 8, 0, [(6, 1, 3), (2, 2, 7), (2, 1, 4), (5, 1, 4), (2, 1, 1), (4, 2, 2), (1, 2, 5), (5, 2, 4), (1, 1, 5), (6, 1, 8)], (6, 1, 1), (6, 2, 5)),
#     ( 9, 1, [(1, 2, 7), (5, 2, 4), (5, 1, 1), (2, 1, 8), (6, 2, 5), (1, 1, 7), (2, 1, 3), (4, 1, 4), (1, 1, 4), (6, 1, 6)], (1, 1, 1), (1, 2, 5)),
#     (10, 1, [(1, 2, 7), (6, 1, 6), (1, 1, 3), (5, 2, 3), (6, 1, 1), (2, 1, 1), (1, 2, 4), (6, 2, 5), (2, 1, 3), (4, 2, 8)], (1, 1, 7), (2, 2, 5)),
#     (11, 1, [(1, 2, 7), (5, 2, 3), (6, 1, 8), (3, 1, 6), (1, 1, 1), (6, 2, 5), (6, 1, 5), (1, 2, 4), (2, 1, 2), (2, 2, 1)], (1, 1, 7), (1, 2, 5)),
#     (12, 1, [(1, 1, 7), (6, 2, 6), (2, 2, 6), (2, 1, 6), (2, 1, 1), (5, 2, 2), (5, 2, 6), (1, 1, 2), (3, 1, 4), (6, 1, 8)], (1, 1, 1), (1, 2, 5)),
#     (13, 0, [(1, 1, 1), (6, 2, 5), (1, 1, 4), (2, 2, 5), (2, 1, 1), (3, 1, 4), (5, 1, 1), (2, 1, 4), (6, 1, 4), (1, 2, 3)], (6, 1, 3), (5, 2, 5)),
#     (14, 1, [(1, 2, 5), (6, 2, 7), (2, 2, 5), (4, 1, 4), (6, 1, 1), (2, 1, 4), (2, 1, 7), (5, 1, 1), (6, 2, 5), (5, 2, 7)], (1, 1, 1), (1, 2, 7)),
#     (15, 0, [(1, 1, 1), (1, 2, 1), (5, 2, 6), (2, 1, 6), (1, 2, 5), (5, 1, 3), (5, 1, 8), (3, 1, 4), (6, 2, 5), (6, 1, 4)], (6, 1, 1), (5, 2, 3)),
#     (16, 0, [(6, 1, 1), (1, 1, 2), (5, 2, 1), (2, 1, 5), (2, 1, 1), (4, 2, 8), (2, 2, 7), (5, 1, 8), (6, 2, 5), (2, 2, 4)], (6, 1, 3), (5, 2, 5)),
#     (17, 0, [(1, 2, 5), (2, 1, 6), (5, 2, 3), (3, 2, 8), (6, 2, 5), (5, 1, 1), (1, 2, 1), (2, 1, 3), (2, 2, 4), (1, 1, 2)], (6, 1, 1), (6, 2, 3)),
#     (18, 0, [(6, 2, 5), (2, 1, 5), (6, 1, 2), (1, 1, 1), (5, 1, 1), (1, 2, 1), (6, 1, 7), (6, 2, 2), (2, 2, 3), (5, 2, 6)], (6, 1, 1), (6, 2, 3)),
#     (19, 0, [(6, 1, 1), (5, 2, 7), (1, 2, 3), (1, 1, 2), (2, 2, 5), (2, 1, 2), (1, 1, 5), (6, 2, 4), (5, 2, 2), (6, 1, 5)], (6, 1, 3), (6, 2, 5)),
#     (20, 1, [(6, 2, 5), (2, 1, 6), (5, 2, 6), (1, 2, 5), (1, 1, 7), (6, 1, 8), (4, 1, 4), (1, 1, 2), (2, 1, 3), (2, 2, 5)], (1, 1, 1), (1, 2, 7)),
#     (21, 0, [(6, 2, 5), (2, 2, 5), (1, 2, 2), (5, 1, 7), (6, 1, 3), (3, 2, 2), (6, 1, 8), (1, 2, 5), (6, 2, 1), (5, 2, 6)], (6, 1, 1), (5, 2, 5)),
#     (22, 1, [(1, 2, 5), (6, 1, 5), (2, 1, 1), (4, 2, 8), (1, 1, 7), (1, 1, 2), (6, 2, 5), (5, 1, 7), (6, 2, 7), (1, 2, 2)], (1, 1, 1), (1, 2, 7)),
#     (23, 0, [(1, 1, 1), (5, 1, 2), (6, 2, 4), (1, 1, 4), (2, 2, 5), (5, 2, 6), (6, 1, 5), (1, 2, 5), (4, 2, 8), (2, 2, 1)], (6, 1, 1), (6, 2, 5)),
#     (24, 1, [(1, 1, 1), (6, 2, 6), (1, 2, 1), (2, 2, 5), (1, 2, 5), (6, 1, 8), (5, 1, 8), (6, 1, 5), (5, 2, 7), (3, 1, 4)], (2, 1, 1), (1, 2, 7)),
#     (25, 0, [(2, 1, 1), (1, 2, 3), (5, 1, 8), (6, 2, 4), (6, 1, 1), (6, 1, 6), (5, 2, 5), (1, 1, 3), (3, 2, 8), (1, 2, 5)], (6, 1, 3), (6, 2, 5)),
#     (26, 0, [(5, 2, 5), (1, 2, 5), (6, 2, 4), (1, 1, 2), (6, 1, 1), (4, 1, 4), (2, 2, 4), (6, 1, 6), (2, 1, 3), (1, 2, 2)], (5, 1, 1), (6, 2, 5)),
#     (27, 0, [(2, 1, 1), (1, 2, 2), (6, 2, 3), (6, 1, 6), (1, 2, 5), (5, 1, 1), (6, 2, 6), (2, 2, 3), (1, 1, 3), (5, 2, 6)], (6, 1, 1), (6, 2, 5)),
#     (28, 1, [(2, 2, 5), (6, 2, 5), (1, 1, 3), (5, 1, 5), (1, 2, 7), (5, 2, 6), (6, 2, 1), (2, 2, 8), (2, 1, 2), (4, 2, 8)], (1, 1, 1), (1, 2, 5)),
#     (29, 1, [(5, 1, 1), (5, 2, 5), (1, 1, 6), (3, 2, 2), (2, 1, 1), (6, 2, 5), (5, 2, 2), (2, 1, 5), (1, 2, 6), (5, 1, 7)], (1, 1, 7), (1, 2, 5)),
#     (30, 0, [(5, 2, 5), (2, 1, 2), (5, 1, 3), (6, 2, 3), (1, 2, 5), (3, 2, 2), (5, 2, 2), (2, 1, 7), (2, 2, 5), (2, 2, 2)], (6, 1, 1), (6, 2, 5)),
#     (31, 1, [(2, 2, 5), (2, 1, 5), (5, 1, 1), (1, 2, 5), (1, 1, 7), (6, 1, 1), (1, 1, 3), (6, 2, 8), (6, 2, 5), (2, 1, 2)], (1, 1, 1), (1, 2, 7)),
#     (32, 0, [(5, 1, 1), (2, 2, 6), (1, 1, 1), (2, 1, 6), (6, 2, 5), (6, 2, 1), (6, 1, 2), (4, 1, 6), (5, 1, 5), (2, 2, 3)], (6, 1, 1), (5, 2, 5)),
#     (33, 1, [(5, 2, 5), (2, 2, 7), (1, 1, 2), (4, 1, 6), (1, 2, 7), (2, 1, 2), (1, 1, 7), (6, 2, 5), (6, 1, 6), (6, 1, 1)], (1, 1, 1), (1, 2, 5)),
#     (34, 0, [(2, 2, 5), (6, 1, 2), (5, 2, 6), (1, 1, 3), (6, 2, 3), (4, 2, 8), (6, 2, 7), (2, 1, 2), (1, 2, 3), (6, 1, 7)], (5, 1, 1), (6, 2, 5)),
#     (35, 0, [(2, 1, 1), (5, 1, 1), (1, 2, 3), (2, 2, 4), (6, 2, 5), (5, 2, 5), (3, 2, 2), (6, 2, 2), (2, 1, 4), (1, 1, 3)], (6, 1, 1), (6, 2, 3)),
#     (36, 0, [(5, 1, 1), (1, 2, 4), (6, 1, 3), (3, 1, 6), (6, 2, 3), (2, 2, 4), (5, 2, 6), (6, 2, 8), (1, 2, 1), (1, 1, 2)], (6, 1, 1), (6, 2, 5))
#     ]

# ( card_number, coast_pos, terrain1, t2, t3, t4, t5, t6, stream1, stream2)
# card_config = [
#     ( 1, 0, [(5, 1, 3), (5, 2, 5), (2, 1, 5), (1, 1, 3), (4, 1, 1), (1, 2, 5), (5, 1, 6), (2, 2, 4), (2, 1, 2), (4, 2, 8)], (5, 1, 1), (5, 2, 3)),
#     ( 2, 0, [(5, 2, 3), (1, 2, 3), (4, 2, 5), (2, 1, 3), (1, 1, 1), (3, 2, 2), (4, 2, 2), (5, 1, 1), (1, 1, 5), (2, 2, 4)], (5, 1, 3), (5, 2, 5)),
#     ( 3, 0, [(5, 2, 3), (5, 1, 5), (1, 2, 4), (3, 1, 6), (1, 1, 1), (4, 1, 1), (2, 2, 4), (2, 2, 1), (2, 1, 2), (4, 2, 8)], (5, 1, 1), (5, 2, 5)),
#     ( 4, 0, [(5, 2, 3), (1, 2, 1), (2, 2, 2), (4, 1, 1), (4, 2, 5), (2, 1, 2), (1, 2, 4), (1, 1, 1), (5, 1, 7), (2, 1, 7)], (5, 1, 1), (5, 2, 5)),
#     ( 5, 1, [(1, 1, 7), (2, 2, 1), (4, 2, 3), (1, 2, 6), (4, 1, 1), (5, 1, 7), (3, 1, 4), (2, 2, 4), (2, 1, 1), (1, 2, 3)], (1, 1, 1), (1, 2, 7)),
#     ( 6, 0, [(5, 1, 3), (2, 2, 4), (1, 1, 1), (3, 1, 6), (5, 2, 5), (2, 1, 2), (5, 2, 8), (1, 1, 4), (4, 1, 3), (1, 2, 5)], (4, 1, 1), (5, 2, 3)),
#     ( 7, 1, [(1, 1, 7), (2, 2, 8), (5, 2, 6), (4, 1, 8), (2, 2, 5), (3, 1, 6), (4, 2, 7), (2, 1, 2), (1, 1, 3), (5, 1, 1)], (2, 1, 1), (1, 2, 5)),
#     ( 8, 0, [(5, 1, 3), (2, 2, 7), (2, 1, 4), (4, 1, 4), (2, 1, 1), (3, 2, 2), (1, 2, 5), (4, 2, 4), (1, 1, 5), (5, 1, 8)], (5, 1, 1), (5, 2, 5)),
#     ( 9, 1, [(1, 2, 7), (4, 2, 4), (4, 1, 1), (2, 1, 8), (5, 2, 5), (1, 1, 7), (2, 1, 3), (3, 1, 4), (1, 1, 4), (5, 1, 6)], (1, 1, 1), (1, 2, 5)),
#     (10, 1, [(1, 2, 7), (5, 1, 6), (1, 1, 3), (4, 2, 3), (5, 1, 1), (2, 1, 1), (1, 2, 4), (5, 2, 5), (2, 1, 3), (3, 2, 8)], (1, 1, 7), (2, 2, 5)),
#     (11, 1, [(1, 2, 7), (4, 2, 3), (5, 1, 8), (3, 1, 6), (1, 1, 1), (5, 2, 5), (5, 1, 5), (1, 2, 4), (2, 1, 2), (2, 2, 1)], (1, 1, 7), (1, 2, 5)),
#     (12, 1, [(1, 1, 7), (5, 2, 6), (2, 2, 6), (2, 1, 6), (2, 1, 1), (4, 2, 2), (4, 2, 6), (1, 1, 2), (3, 1, 4), (5, 1, 8)], (1, 1, 1), (1, 2, 5)),
#     (13, 0, [(1, 5, 1), (2, 5, 6), (1, 1, 4), (2, 2, 5), (2, 1, 1), (3, 1, 4), (4, 1, 1), (2, 1, 4), (5, 1, 4), (1, 2, 3)], (5, 1, 3), (4, 2, 5)),
#     (14, 1, [(1, 2, 5), (5, 2, 7), (2, 2, 5), (3, 1, 4), (5, 1, 1), (2, 1, 4), (2, 1, 7), (4, 1, 1), (5, 2, 5), (4, 2, 7)], (1, 1, 1), (1, 2, 7)),
#     (15, 0, [(1, 1, 1), (1, 2, 1), (4, 2, 6), (2, 1, 6), (1, 2, 5), (4, 1, 3), (4, 1, 8), (3, 1, 4), (5, 2, 5), (5, 1, 4)], (5, 1, 1), (5, 2, 3)),
#     (16, 0, [(5, 1, 1), (1, 1, 2), (4, 2, 1), (2, 1, 5), (2, 1, 1), (3, 2, 8), (2, 2, 7), (4, 1, 8), (5, 2, 5), (2, 2, 4)], (5, 1, 3), (4, 2, 5)),
#     (17, 0, [(1, 2, 5), (2, 1, 6), (4, 2, 3), (3, 2, 8), (5, 2, 5), (4, 1, 1), (1, 2, 1), (2, 1, 3), (2, 2, 4), (1, 1, 2)], (5, 1, 1), (5, 2, 3)),
#     (18, 0, [(5, 2, 5), (2, 1, 5), (5, 1, 2), (1, 1, 1), (4, 1, 1), (1, 2, 1), (5, 1, 7), (5, 2, 2), (2, 2, 3), (4, 2, 6)], (5, 1, 1), (5, 2, 3)),
#     (19, 0, [(5, 1, 1), (4, 2, 7), (1, 2, 3), (1, 1, 2), (2, 2, 5), (2, 1, 2), (1, 1, 5), (5, 2, 4), (4, 2, 2), (5, 1, 5)], (5, 1, 3), (5, 2, 5)),
#     (20, 1, [(5, 2, 5), (2, 1, 6), (4, 2, 6), (1, 2, 5), (1, 1, 7), (5, 1, 8), (3, 1, 4), (1, 1, 2), (2, 1, 3), (2, 2, 5)], (1, 1, 1), (1, 2, 7)),
#     (21, 0, [(5, 2, 5), (2, 2, 5), (1, 2, 2), (4, 1, 7), (5, 1, 3), (3, 2, 2), (5, 1, 8), (1, 2, 5), (5, 2, 1), (4, 2, 6)], (5, 1, 1), (4, 2, 5)),
#     (22, 1, [(1, 2, 5), (5, 1, 5), (2, 1, 1), (3, 2, 8), (1, 1, 7), (1, 1, 2), (5, 2, 5), (4, 1, 7), (5, 2, 7), (1, 2, 2)], (1, 1, 1), (1, 2, 7)),
#     (23, 0, [(1, 1, 1), (4, 1, 2), (5, 2, 4), (1, 1, 4), (2, 2, 5), (4, 2, 6), (5, 1, 5), (1, 2, 5), (3, 2, 8), (2, 2, 1)], (5, 1, 1), (5, 2, 5)),
#     (24, 1, [(1, 1, 1), (5, 2, 6), (1, 2, 1), (2, 2, 5), (1, 2, 5), (5, 1, 8), (4, 1, 8), (5, 1, 5), (4, 2, 7), (3, 1, 4)], (2, 1, 1), (1, 2, 7)),
#     (25, 0, [(2, 1, 1), (1, 2, 3), (4, 1, 8), (5, 2, 4), (5, 1, 1), (5, 1, 6), (4, 2, 5), (1, 1, 3), (3, 2, 8), (1, 2, 5)], (5, 1, 3), (5, 2, 5)),
#     (26, 0, [(4, 2, 5), (1, 2, 5), (5, 2, 4), (1, 1, 2), (5, 1, 1), (3, 1, 4), (2, 2, 4), (5, 1, 6), (2, 1, 3), (1, 2, 2)], (4, 1, 1), (5, 2, 5)),
#     (27, 0, [(2, 1, 1), (1, 2, 2), (5, 2, 3), (5, 1, 6), (1, 2, 5), (4, 1, 1), (5, 2, 6), (2, 2, 3), (1, 1, 3), (4, 2, 6)], (5, 1, 1), (5, 2, 5)),
#     (28, 1, [(2, 2, 5), (5, 2, 5), (1, 1, 3), (4, 1, 5), (1, 2, 7), (4, 2, 6), (5, 2, 1), (2, 2, 8), (2, 1, 2), (3, 2, 8)], (1, 1, 1), (1, 2, 5)),
#     (29, 1, [(4, 1, 1), (4, 2, 5), (1, 1, 6), (3, 2, 2), (2, 1, 1), (5, 2, 5), (4, 2, 2), (2, 1, 5), (1, 2, 6), (4, 1, 7)], (1, 1, 7), (1, 2, 5)),
#     (30, 0, [(4, 2, 5), (2, 1, 2), (4, 1, 3), (5, 2, 3), (1, 2, 5), (3, 2, 2), (4, 2, 2), (2, 1, 7), (2, 2, 5), (2, 2, 2)], (5, 1, 1), (5, 2, 5)),
#     (31, 1, [(2, 2, 5), (2, 1, 5), (4, 1, 1), (1, 2, 5), (1, 1, 7), (5, 1, 1), (1, 1, 3), (5, 2, 8), (5, 2, 5), (2, 1, 2)], (1, 1, 1), (1, 2, 7)),
#     (32, 0, [(4, 1, 1), (2, 2, 6), (1, 1, 1), (2, 1, 6), (5, 2, 5), (5, 2, 1), (5, 1, 2), (3, 1, 6), (4, 1, 5), (2, 2, 3)], (5, 1, 1), (4, 2, 5)),
#     (33, 1, [(4, 2, 5), (2, 2, 7), (1, 1, 2), (3, 1, 6), (1, 2, 7), (2, 1, 2), (1, 1, 7), (5, 2, 5), (5, 1, 6), (5, 1, 1)], (1, 1, 1), (1, 2, 5)),
#     (34, 0, [(2, 2, 5), (5, 1, 2), (4, 2, 6), (1, 1, 3), (5, 2, 3), (3, 2, 8), (5, 2, 7), (2, 1, 2), (1, 2, 3), (5, 1, 7)], (4, 1, 1), (5, 2, 5)),
#     (35, 0, [(2, 1, 1), (4, 1, 1), (1, 2, 3), (2, 2, 4), (5, 2, 5), (4, 2, 5), (3, 2, 2), (5, 2, 2), (2, 1, 4), (1, 1, 3)], (5, 1, 1), (5, 2, 3)),
#     (36, 0, [(4, 1, 1), (1, 2, 4), (5, 1, 3), (3, 1, 6), (5, 2, 3), (2, 2, 4), (4, 2, 6), (5, 2, 8), (1, 2, 1), (1, 1, 2)], (5, 1, 1), (5, 2, 5))
#     ]


card_config = [
    ( 1, 1, [(1, 1, 7), (3, 1, 6), (2, 2, 8), (1, 2, 6), (3, 2, 5), (1, 1, 5)], (1, 1, 1), (1, 2, 5)),
    ( 2, 1, [(1, 2, 7), (3, 2, 8), (1, 1, 7), (2, 1, 6), (3, 1, 1), (1, 1, 2)], (1, 1, 1), (1, 2, 5)),
    ( 3, 1, [(1, 1, 7), (3, 2, 6), (2, 1, 4), (1, 2, 7), (3, 1, 1), (1, 2, 3)], (1, 1, 1), (1, 2, 5)),
    ( 4, 1, [(3, 1, 1), (1, 1, 5), (2, 2, 2), (1, 2, 5), (3, 2, 5), (1, 1, 3)], (1, 1, 1), (1, 2, 7)),
    ( 5, 1, [(3, 2, 5), (1, 2, 3), (1, 1, 2), (2, 1, 4), (3, 1, 1), (1, 1, 6)], (1, 1, 1), (1, 2, 7)),
    ( 6, 1, [(3, 1, 1), (1, 2, 6), (2, 2, 8), (1, 1, 8), (3, 2, 5), (1, 2, 1)], (1, 1, 1), (1, 2, 7)),
    ( 7, 1, [(1, 2, 7), (3, 2, 7), (2, 1, 6), (1, 2, 1), (3, 1, 1), (3, 1, 5)], (1, 1, 7), (1, 2, 5)),
    ( 8, 1, [(1, 1, 1), (3, 1, 5), (1, 2, 6), (2, 1, 6), (3, 2, 5), (3, 1, 8)], (1, 1, 7), (1, 2, 5)),
    ( 9, 1, [(1, 2, 7), (3, 1, 8), (2, 1, 4), (1, 1, 6), (3, 2, 5), (3, 2, 1)], (1, 1, 7), (1, 2, 5)),
    (10, 1, [(1, 2, 7), (3, 1, 6), (1, 1, 6), (2, 2, 8), (3, 2, 5), (3, 1, 1)], (1, 1, 7), (1, 2, 5)),
    (11, 1, [(1, 1, 1), (1, 2, 6), (2, 1, 6), (3, 2, 5), (3, 1, 1), (1, 2, 1)], (1, 1, 7), (1, 2, 5)),
    (12, 1, [(1, 2, 7), (1, 1, 1), (3, 2, 5), (2, 1, 4), (3, 1, 1), (1, 2, 3)], (1, 1, 7), (1, 2, 5)),
    (13, 1, [(3, 2, 5), (1, 1, 3), (1, 2, 8), (2, 2, 2), (3, 1, 1), (3, 1, 5)], (1, 1, 1), (1, 2, 5)),
    (14, 1, [(3, 1, 1), (3, 2, 6), (2, 1, 4), (3, 2, 1), (1, 1, 7), (1, 1, 5)], (1, 1, 1), (1, 2, 5)),
    (15, 1, [(3, 2, 5), (3, 1, 1), (1, 1, 8), (2, 1, 4), (1, 2, 7), (1, 2, 3)], (1, 1, 1), (1, 2, 5)),
    (16, 1, [(1, 1, 7), (3, 2, 7), (1, 1, 5), (2, 2, 8), (3, 1, 1), (3, 1, 5)], (1, 1, 1), (1, 2, 7)),
    (17, 1, [(1, 2, 5), (1, 1, 8), (2, 1, 4), (3, 2, 5), (3, 1, 1), (1, 2, 3)], (1, 1, 1), (1, 2, 7)),
    (18, 1, [(1, 1, 7), (1, 2, 4), (1, 2, 8), (2, 1, 6), (3, 1, 1), (3, 2, 1)], (1, 1, 1), (1, 2, 7)),
    (19, 0, [(3, 1, 3), (1, 2, 2), (3, 1, 6), (1, 1, 1), (3, 2, 3), (3, 2, 6)], (3, 1, 1), (3, 2, 5)),
    (20, 0, [(3, 2, 3), (3, 1, 6), (1, 2, 5), (1, 1, 1), (3, 1, 3), (2, 2, 8)], (3, 1, 1), (3, 2, 5)),
    (21, 0, [(1, 2, 5), (1, 1, 4), (3, 2, 1), (3, 2, 4), (1, 1, 1), (1, 2, 3)], (3, 1, 1), (3, 2, 5)),
    (22, 0, [(1, 2, 5), (3, 1, 7), (3, 2, 6), (3, 2, 1), (3, 1, 3), (1, 1, 4)], (3, 1, 1), (3, 2, 3)),
    (23, 0, [(1, 1, 1), (1, 2, 5), (3, 2, 7), (3, 1, 8), (3, 1, 3), (2, 2, 8)], (3, 1, 1), (3, 2, 3)),
    (24, 0, [(3, 2, 5), (3, 1, 8), (1, 1, 4), (3, 2, 1), (3, 1, 3), (1, 2, 5)], (3, 1, 1), (3, 2, 3)),
    (25, 0, [(3, 2, 3), (1, 1, 1), (1, 1, 4), (3, 2, 7), (3, 1, 3), (3, 1, 8)], (3, 1, 1), (3, 2, 5)),
    (26, 0, [(3, 1, 1), (3, 2, 6), (1, 1, 1), (1, 2, 1), (1, 2, 5), (2, 2, 2)], (3, 1, 3), (3, 2, 5)),
    (27, 0, [(3, 1, 1), (1, 2, 1), (3, 2, 8), (1, 1, 2), (1, 2, 5), (2, 2, 8)], (3, 1, 3), (3, 2, 5)),
    (28, 0, [(3, 1, 1), (1, 2, 2), (3, 1, 5), (1, 1, 1), (3, 2, 3), (2, 1, 4)], (3, 1, 3), (3, 2, 5)),
    (29, 0, [(3, 1, 1), (1, 1, 4), (1, 2, 3), (1, 1, 1), (1, 2, 5), (3, 1, 6)], (3, 1, 3), (3, 2, 5)),
    (30, 0, [(3, 2, 3), (1, 1, 3), (1, 2, 3), (3, 1, 1), (1, 1, 1), (2, 2, 2)], (3, 1, 3), (3, 2, 5)),
    (31, 0, [(1, 1, 1), (3, 1, 7), (3, 2, 4), (1, 2, 5), (3, 1, 3), (2, 2, 8)], (3, 1, 1), (3, 2, 5)),
    (32, 0, [(1, 2, 5), (3, 2, 8), (1, 1, 5), (3, 2, 4), (1, 1, 1), (3, 1, 3)], (3, 1, 1), (3, 2, 5)),
    (33, 0, [(1, 1, 1), (3, 2, 7), (3, 2, 4), (1, 1, 5), (1, 2, 5), (2, 1, 5)], (3, 1, 1), (3, 2, 5)),
    (34, 0, [(3, 1, 3), (1, 1, 1), (3, 2, 1), (1, 2, 5), (3, 2, 5), (2, 1, 6)], (3, 1, 1), (3, 2, 3)),
    (35, 0, [(3, 2, 5), (1, 2, 1), (1, 1, 3), (1, 1, 1), (1, 2, 5), (3, 1, 5)], (3, 1, 1), (3, 2, 3)),
    (36, 0, [(3, 1, 3), (1, 2, 1), (3, 2, 5), (1, 1, 2), (1, 2, 5), (2, 2, 2)], (3, 1, 1), (3, 2, 3))
    ]

def draw_terrain_circle(dwg, terrain_number, placement):
    in_box_offset_x = 0
    in_box_offset_y = 0

    if placement[2] == 1:
        # top middle
        in_box_offset_x = box_size / 2
        in_box_offset_y = terrain_radius
    elif placement[2] == 2:
        in_box_offset_x = box_size - terrain_radius
        in_box_offset_y = terrain_radius
    elif placement[2] == 3:
        # right middle
        in_box_offset_x = box_size - terrain_radius
        in_box_offset_y = box_size / 2
    elif placement[2] == 4:
        in_box_offset_x = box_size - terrain_radius
        in_box_offset_y = box_size - terrain_radius
    elif placement[2] == 5:
        in_box_offset_x = box_size / 2
        in_box_offset_y = box_size - terrain_radius
    elif placement[2] == 6:
        in_box_offset_x = terrain_radius
        in_box_offset_y = box_size - terrain_radius
    elif placement[2] == 7:
        # left middle
        in_box_offset_x = terrain_radius
        in_box_offset_y = box_size / 2
    elif placement[2] == 8:
        in_box_offset_x = terrain_radius
        in_box_offset_y = terrain_radius

    box_offset_x = 0
    box_offset_y = 0
    if placement[0] == 1:
        box_offset_x = column_1_x[0]
    elif placement[0] == 2:
        box_offset_x = column_2_x[0]
    elif placement[0] == 3:
        box_offset_x = column_3_x[0]
#    elif placement[0] == 4:
#        box_offset_x = column_4_x[0]
#    elif placement[0] == 5:
#        box_offset_x = column_5_x[0]
#    elif placement[0] == 6:
#        box_offset_x = column_6_x[0]

    if placement[1] == 1:
        box_offset_y = row_1_y[0]
    elif placement[1] == 2:
        box_offset_y = row_2_y[0]

    center_x = box_offset_x + in_box_offset_x
    center_y = box_offset_y + in_box_offset_y
    dwg.add(dwg.circle(center=(center_x, center_y), r=terrain_radius, fill=terrain_color, stroke='none'))

    terrain_label_vertical_offset = 20
    label_text = '{:d}'.format(terrain_number)
    dwg.add(dwg.text(label_text, insert=(center_x, center_y + terrain_label_vertical_offset), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size=terrain_label_font_size, font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))

def draw_terrain_edge(dwg, terrain_number, placement):
    m = (0, 0)
    ln1 = (0, 0)
    a = (0, 0)
    ln2 = (0, 0)
    lx = 0
    ly = 0

    if placement[2] == 7:
        x = column_1_x[0]
        cy = 0
        if placement[1] == 1:
            cy = row_1_y[1]
        elif placement[1] == 2:
            cy = row_2_y[1]
        m = (x, cy + terrain_radius)
        ln1 = (x + terrain_edge_width, cy + terrain_radius)
        a = (x + terrain_edge_width, cy - terrain_radius)
        ln2 = (x, cy - terrain_radius)
        lx = x + terrain_edge_label_offset_x
        ly = cy + terrain_edge_label_offset_y1

    if placement[2] == 3:
        x = column_3_x[2]
        cy = 0
        if placement[1] == 1:
            cy = row_1_y[1]
        elif placement[1] == 2:
            cy = row_2_y[1]
        m = (x, cy - terrain_radius)
        ln1 = (x - terrain_edge_width, cy - terrain_radius)
        a = (x - terrain_edge_width, cy + terrain_radius)
        ln2 = (x, cy + terrain_radius)
        lx = x - terrain_edge_label_offset_x
        ly = cy + terrain_edge_label_offset_y1

    if placement[2] == 1:
        cx = 0
        y = row_1_y[0]
        if placement[0] == 1:
            cx = column_1_x[1]
        elif placement[0] == 2:
            cx = column_2_x[1]
        elif placement[0] == 3:
            cx = column_3_x[1]
        m = (cx - terrain_radius, y)
        ln1 = (cx - terrain_radius, y + terrain_edge_width)
        a = (cx + terrain_radius, y + terrain_edge_width)
        ln2 = (cx + terrain_radius, y)
        lx = cx
        ly = y + terrain_edge_label_offset_y3

    if placement[2] == 5:
        cx = 0
        y = row_2_y[2]
        if placement[0] == 1:
            cx = column_1_x[1]
        elif placement[0] == 2:
            cx = column_2_x[1]
        elif placement[0] == 3:
            cx = column_3_x[1]
        m = (cx + terrain_radius, y)
        ln1 = (cx + terrain_radius, y - terrain_edge_width)
        a = (cx - terrain_radius, y - terrain_edge_width)
        ln2 = (cx - terrain_radius, y)
        lx = cx
        ly = y - terrain_edge_label_offset_y2

    move = 'M {:d},{:d} '.format(m[0], m[1])
    line1 = 'L {:d},{:d} '.format(ln1[0], ln1[1])
    arc = 'A {:d} {:d}, 0, 1, 0, {:d},{:d} '.format(terrain_radius, terrain_radius, a[0], a[1])
    line2 = 'L {:d},{:d} Z'.format(ln2[0], ln2[1])
    pathCommand = move + line1 + arc + line2
    print(terrain_number, placement[0], placement[1], pathCommand)
    dwg.add(dwg.path(d=pathCommand, fill=terrain_color, stroke='none'))

    label_text = '{:d}'.format(terrain_number)
    dwg.add(dwg.text(label_text, insert=(lx, ly), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='64px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))

def old_draw_stream_marker(dwg, placement):
    p1 = (0, 0)
    p2 = (0, 0)
    p3 = (0, 0)
    lx = 0
    ly = 0

    if placement[1] == 7:
        x = column_1_x[0]
        cy = 0
        if placement[0] == 1:
            cy = row_1_y[1]
        elif placement[0] == 4:
            cy = row_2_y[1]
        p1 = (x, cy - (stream_width / 2))
        p2 = (x + stream_height, cy)
        p3 = (x, cy + (stream_width / 2))
        lx = x + stream_label_offset_x
        ly = cy + stream_label_offset_y1

    if placement[1] == 3:
        x = column_3_x[2]
        cy = 0
        if placement[0] == 3:
            cy = row_1_y[1]
        elif placement[0] == 6:
            cy = row_2_y[1]
        p1 = (x, cy - (stream_width / 2))
        p2 = (x - stream_height, cy)
        p3 = (x, cy + (stream_width / 2))
        lx = x - stream_label_offset_x
        ly = cy + stream_label_offset_y1

    if placement[1] == 1:
        cx = 0
        y = row_1_y[0]
        if placement[0] == 1:
            cx = column_1_x[1]
        elif placement[0] == 2:
            cx = column_2_x[1]
        elif placement[0] == 3:
            cx = column_3_x[1]
        p1 = (cx - (stream_width / 2), y)
        p2 = (cx, y + stream_height)
        p3 = (cx + (stream_width / 2), y)
        lx = cx
        ly = y + stream_label_offset_y3

    if placement[1] == 5:
        cx = 0
        y = row_2_y[2]
        if placement[0] == 4:
            cx = column_1_x[1]
        elif placement[0] == 5:
            cx = column_2_x[1]
        elif placement[0] == 6:
            cx = column_3_x[1]
        m = (cx + terrain_radius, y)
        p1 = (cx - (stream_width / 2), y)
        p2 = (cx, y - stream_height)
        p3 = (cx + (stream_width / 2), y)
        lx = cx
        ly = y - stream_label_offset_y2

    trianglePoints = [p1, p2, p3]
    dwg.add(dwg.polygon(points=trianglePoints, fill=stream_color, stroke='none'))

    dwg.add(dwg.text('S', insert=(lx, ly), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='40px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))


def draw_background(dwg, image_width, image_height):
    dwg.add(dwg.rect(insert=(0, 0), size=(image_width, image_height), fill='#ffffff', stroke='none'))


def draw_box_outline(dwg, board_offset, box_count, box_size, line_width):
    line_offset = line_width / 2
    stroke_width = str(line_width) + 'px'

    # Outline of game board
    board_rect_origin = Point(board_offset.x + line_offset, board_offset.y + line_offset)
    board_rect_size = Size((box_count.x * box_size.width) + (box_count.x * line_width), (box_count.y * box_size.height) + (box_count.y * line_width))

    dwg.add(dwg.rect(insert=(board_rect_origin.x, board_rect_origin.y), size=(board_rect_size.width, board_rect_size.height), fill='#ffffff', stroke='#000000', stroke_width=stroke_width))

    # Horizontal lines
    for number in range(1, box_count.y):
        line_y = board_offset.y + (number * (box_size.height + line_width)) + line_offset
        line_start = Point(board_offset.x + line_width, line_y)
        line_end = Point(board_offset.x + (box_count.x * (box_size.width + line_width)), line_y)

        dwg.add(dwg.line((line_start.x, line_start.y), (line_end.x, line_end.y), stroke='#000000', stroke_width=stroke_width))

    # Vertical lines
    for number in range(1, box_count.x):
        line_x = board_offset.x + (number * (box_size.width + line_width)) + line_offset
        line_start = Point(line_x, board_offset.y + line_width)
        line_end = Point(line_x, board_offset.y + (box_count.y * (box_size.height + line_width)))

        dwg.add(dwg.line((line_start.x, line_start.y), (line_end.x, line_end.y), stroke='#000000', stroke_width=stroke_width))


def draw_coast_marker(dwg, coast_width, coast_position, board_offset, box_count, box_size, line_width):
    coast_label_height = 30

    if coast_position == 0:
        # Left side
        coast_rect_origin = Point(board_offset.x + line_width, board_offset.y + line_width)
        coast_rect_size = Size(coast_width, (box_count.y * (box_size.height + line_width)) - line_width)
    elif coast_position == 1:
        # Right side
        coast_rect_origin = Point(board_offset.x + (box_count.x * (box_size.width + line_width)) - coast_width, board_offset.y + line_width)
        coast_rect_size = Size(coast_width, (box_count.y * (box_size.height + line_width)) - line_width)

    dwg.add(dwg.rect(insert=(coast_rect_origin.x, coast_rect_origin.y), size=(coast_rect_size.width, coast_rect_size.height), fill=coast_color, stroke='none'))
    dwg.add(dwg.text('C', insert=(coast_rect_origin.x + (coast_width / 2), board_offset.y + line_width + (coast_rect_size.height / 2) + (coast_label_height / 2)), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='40px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))


def draw_terrain_marker(dwg, terrain_number, terrain_placement, board_offset, box_size, line_width):
    box_origin = Point(board_offset.x + line_width + ((terrain_placement.box_x - 1) * (box_size.width + line_width)), board_offset.y + line_width + ((terrain_placement.box_y - 1) * (box_size.height + line_width)))
    if terrain_number == 1 or terrain_number == 5:
        draw_terrain_edge_in_box(dwg, terrain_number, terrain_placement.position, box_origin, box_size)
    else:
        draw_terrain_circle_in_box(dwg, terrain_number, terrain_placement.position, box_origin, box_size)


def draw_terrain_edge_in_box(dwg, terrain_number, position, box_origin, box_size):
    m = (0, 0)
    ln1 = (0, 0)
    a = (0, 0)
    ln2 = (0, 0)
    lx = 0
    ly = 0

    if position == 7:
        # left middle
        x = 0
        cy = box_size.height / 2
        m = Point(x, cy + terrain_radius)
        ln1 = Point(x + terrain_edge_width, cy + terrain_radius)
        a = Point(x + terrain_edge_width, cy - terrain_radius)
        ln2 = Point(x, cy - terrain_radius)
        lx = x + terrain_edge_label_offset_x
        ly = cy + terrain_edge_label_offset_y1

    elif position == 3:
        x = box_size.width
        cy = box_size.height / 2
        m = Point(x, cy - terrain_radius)
        ln1 = Point(x - terrain_edge_width, cy - terrain_radius)
        a = Point(x - terrain_edge_width, cy + terrain_radius)
        ln2 = Point(x, cy + terrain_radius)
        lx = x - terrain_edge_label_offset_x
        ly = cy + terrain_edge_label_offset_y1

    elif position == 1:
        cx = box_size.width / 2
        y = 0
        m = Point(cx - terrain_radius, y)
        ln1 = Point(cx - terrain_radius, y + terrain_edge_width)
        a = Point(cx + terrain_radius, y + terrain_edge_width)
        ln2 = Point(cx + terrain_radius, y)
        lx = cx
        ly = y + terrain_edge_label_offset_y3

    elif position == 5:
        cx = box_size.width / 2
        y = box_size.height
        m = Point(cx + terrain_radius, y)
        ln1 = Point(cx + terrain_radius, y - terrain_edge_width)
        a = Point(cx - terrain_radius, y - terrain_edge_width)
        ln2 = Point(cx - terrain_radius, y)
        lx = cx
        ly = y - terrain_edge_label_offset_y2

    move = 'M {:d},{:d} '.format(int(m.x + box_origin.x), int(m.y + box_origin.y))
    line1 = 'L {:d},{:d} '.format(int(ln1.x + box_origin.x), int(ln1.y + box_origin.y))
    arc = 'A {:d} {:d}, 0, 1, 0, {:d},{:d} '.format(terrain_radius, terrain_radius, int(a.x + box_origin.x), int(a.y + box_origin.y))
    line2 = 'L {:d},{:d} Z'.format(int(ln2.x + box_origin.x), int(ln2.y + box_origin.y))
    pathCommand = move + line1 + arc + line2
    dwg.add(dwg.path(d=pathCommand, fill=terrain_color, stroke='none'))

    label_text = '{:d}'.format(terrain_number)
    dwg.add(dwg.text(label_text, insert=(lx + box_origin.x, ly + box_origin.y), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='64px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))


def draw_terrain_circle_in_box(dwg, terrain_number, position, box_origin, box_size):
    in_box_offset_x = 0
    in_box_offset_y = 0

    if position == 1:
        # top middle
        in_box_offset_x = box_size.width / 2
        in_box_offset_y = terrain_radius
    elif position == 2:
        in_box_offset_x = box_size.width - terrain_radius
        in_box_offset_y = terrain_radius
    elif position == 3:
        # right middle
        in_box_offset_x = box_size.width - terrain_radius
        in_box_offset_y = box_size.height / 2
    elif position == 4:
        in_box_offset_x = box_size.width - terrain_radius
        in_box_offset_y = box_size.height - terrain_radius
    elif position == 5:
        in_box_offset_x = box_size.width / 2
        in_box_offset_y = box_size.height - terrain_radius
    elif position == 6:
        in_box_offset_x = terrain_radius
        in_box_offset_y = box_size.height - terrain_radius
    elif position == 7:
        # left middle
        in_box_offset_x = terrain_radius
        in_box_offset_y = box_size.height / 2
    elif position == 8:
        in_box_offset_x = terrain_radius
        in_box_offset_y = terrain_radius

    center_x = box_origin.x + in_box_offset_x
    center_y = box_origin.y + in_box_offset_y
    dwg.add(dwg.circle(center=(center_x, center_y), r=terrain_radius, fill=terrain_color, stroke='none'))

    terrain_label_vertical_offset = 20
    label_text = '{:d}'.format(terrain_number)
    if terrain_number == 6 or terrain_number == 9:
        dwg.add(dwg.text(label_text, insert=(center_x, center_y + terrain_label_vertical_offset), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', text_decoration='underline', font_size='64px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))
    else:
        dwg.add(dwg.text(label_text, insert=(center_x, center_y + terrain_label_vertical_offset), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='64px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))


def draw_stream_marker(dwg, terrain_placement, board_offset, box_size, line_width):
    box_origin = Point(board_offset.x + line_width + ((terrain_placement.box_x - 1) * (box_size.width + line_width)), board_offset.y + line_width + ((terrain_placement.box_y - 1) * (box_size.height + line_width)))
    draw_stream_marker_in_box(dwg, terrain_placement.position, box_origin, box_size)


def draw_stream_marker_in_box(dwg, position, box_origin, box_size):
    if position == 7:
        x = 0
        cy = box_size.height / 2
        p1 = Point(x, cy - (stream_width / 2))
        p2 = Point(x + stream_height, cy)
        p3 = Point(x, cy + (stream_width / 2))
        lx = x + stream_label_offset_x
        ly = cy + stream_label_offset_y1

    if position == 3:
        x = box_size.width
        cy = box_size.height / 2
        p1 = Point(x, cy - (stream_width / 2))
        p2 = Point(x - stream_height, cy)
        p3 = Point(x, cy + (stream_width / 2))
        lx = x - stream_label_offset_x
        ly = cy + stream_label_offset_y1

    if position == 1:
        cx = box_size.width / 2
        y = 0
        p1 = Point(cx - (stream_width / 2), y)
        p2 = Point(cx, y + stream_height)
        p3 = Point(cx + (stream_width / 2), y)
        lx = cx
        ly = y + stream_label_offset_y3

    if position == 5:
        cx = box_size.width / 2
        y = box_size.height
        p1 = Point(cx - (stream_width / 2), y)
        p2 = Point(cx, y - stream_height)
        p3 = Point(cx + (stream_width / 2), y)
        lx = cx
        ly = y - stream_label_offset_y2

    trianglePoints = [(p1.x + box_origin.x, p1.y + box_origin.y), (p2.x + box_origin.x, p2.y + box_origin.y), (p3.x + box_origin.x, p3.y + box_origin.y)]
    dwg.add(dwg.polygon(points=trianglePoints, fill=stream_color, stroke='none'))

    dwg.add(dwg.text('S', insert=(lx + box_origin.x, ly + box_origin.y), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='40px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))


def draw_card(card_number, card_config):
    # Open the file
    if card_type == 'regular':
        filename = './card-files/front{:02d}.svg'.format(card_number)
    elif card_type == 'regular-no-margin':
        filename = './card-files-no-margin/front{:02d}.svg'.format(card_number)
    elif card_type == 'grand':
        filename = './grand-terrain-card-images/front{:02d}.svg'.format(card_number)
    elif card_type == 'grand6x2':
        filename = './grand-terrain-6x2-card-images/front{:02d}.svg'.format(card_number)

    image_width_px = str(image_width) + 'px'
    image_height_px = str(image_height) + 'px'
    dwg = svgwrite.Drawing(filename, size=(image_width_px, image_height_px))

    draw_background(dwg, image_width, image_height)

    #box_size = Size(box_size, box_size)
    draw_box_outline(dwg, Point(board_left_x, board_top_y), Point(box_count_x, box_count_y), Size(box_size, box_size), 4)

    # # Outline of game board
    # board_rect_width = (board_x[2] - board_x[0]) - line_width
    # board_rect_height = (board_y[2] - board_y[0]) - line_width
    # dwg.add(dwg.rect(insert=(board_x[0] + line_offset, board_y[0] + line_offset), size=(board_rect_width, board_rect_height), fill='#ffffff', stroke='#000000', stroke_width='4px'))
    #
    # # Horizontal line for game board boxes
    # dwg.add(dwg.line((column_1_x[0], board_y[1]), (column_3_x[2], board_y[1]), stroke='#000000', stroke_width='4px'))
    #
    # # Vertical lines for game board boxes
    # dwg.add(dwg.line((column_1_x[2] + line_offset, row_1_y[0]), (column_1_x[2] + line_offset, row_2_y[2]), stroke='#000000', stroke_width='4px'))
    # dwg.add(dwg.line((column_2_x[2] + line_offset, row_1_y[0]), (column_2_x[2] + line_offset, row_2_y[2]), stroke='#000000', stroke_width='4px'))

    coast_width = 40
    draw_coast_marker(dwg, coast_width, card_config[1], Point(board_left_x, board_top_y), Point(box_count_x, box_count_y), Size(box_size, box_size), 4)

    # # Coast
    # coast_width = 40
    # coast_height = row_2_y[2] - row_1_y[0]
    # coast_label_vertical_offset = 14
    #
    # if card_config[1] == 0:
    #     dwg.add(dwg.rect(insert=(column_1_x[0], row_1_y[0]), size=(coast_width, coast_height), fill=coast_color, stroke='none'))
    #     dwg.add(dwg.text('C', insert=(column_1_x[0] + (coast_width / 2), board_y[1] + coast_label_vertical_offset), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='40px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))
    # else:
    #     dwg.add(dwg.rect(insert=(column_3_x[2] - coast_width, row_1_y[0]), size=(coast_width, coast_height), fill=coast_color, stroke='none'))
    #     dwg.add(dwg.text('C', insert=(column_3_x[2] - (coast_width / 2), board_y[1] + coast_label_vertical_offset), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='40px', font_family='sans-serif', text_anchor='middle', fill='#ffffff', fill_opacity='1'))

    # # Terrain piece
    # terrain_list = card_config[2]
    # for terrain_index in range(6):
    #     placement = terrain_list[terrain_index]
    #     terrain_piece = terrain_index + 1
    #     if terrain_piece == 1 or terrain_piece == 5:
    #         draw_terrain_edge(dwg, terrain_piece, placement)
    #     else:
    #         draw_terrain_circle(dwg, terrain_piece, placement)

    terrain_index = 1
    for config in card_config[2]:
        terrain_placement = Terrain_Placement(config[0], config[1], config[2])
        draw_terrain_marker(dwg, terrain_index, terrain_placement, Point(board_left_x, board_top_y), Size(box_size, box_size), 4)
        terrain_index = terrain_index + 1

    # # Stream markers
    # draw_stream_marker(dwg, card_config[3])
    # draw_stream_marker(dwg, card_config[4])

    stream_config_1 = card_config[3]
    draw_stream_marker(dwg, Terrain_Placement(stream_config_1[0], stream_config_1[1], stream_config_1[2]), Point(board_left_x, board_top_y), Size(box_size, box_size), 4)

    stream_config_2 = card_config[4]
    draw_stream_marker(dwg, Terrain_Placement(stream_config_2[0], stream_config_2[1], stream_config_2[2]), Point(board_left_x, board_top_y), Size(box_size, box_size), 4)

    # Version number
    dwg.add(dwg.text(version_number, insert=(board_x[0], board_y[2] + bottom_text_height), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='26px', font_family='sans-serif', text_anchor='start', fill='#000000', fill_opacity='1'))

    # Card number
    card_number_text = '#{:02d}'.format(card_number)
    dwg.add(dwg.text(card_number_text, insert=(board_x[2], board_y[2] + bottom_text_height), font_style='normal', font_variant='normal', font_weight='normal', font_stretch='normal', font_size='26px', font_family='sans-serif', text_anchor='end', fill='#000000', fill_opacity='1'))

    # Save the file
    dwg.save()

for card_number in range(36):
    print('Drawing card ', card_number + 1)
    draw_card(card_number + 1, card_config[card_number])

print('Done drawing cards')

