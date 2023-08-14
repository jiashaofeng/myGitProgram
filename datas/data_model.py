import aiqdata as tb
import json

def _define(table_name):

    mktadjfaf_str = {
            "table_name": "",
            "table_show_name": "",
            "table_comment": "",
            "table_category1": "1",
            "table_category2": "2",
            "table_category3": "3",
            "columns": [
                {
                        "col_name": "",
                        "col_show_name": "",
                        "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }
                ,
                {
                    "col_name": "",
                    "col_show_name": "",
                    "col_comment": "-√Ë ˆ"
                }

            ]
        }
    define_json = json.dumps(_str, ensure_ascii=False, separators=(',', ': '))
    tb.overwrite_table_meta(table_name, define_json)
